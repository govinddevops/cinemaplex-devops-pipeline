import os
import subprocess
import boto3
import json
import logging
from pathlib import Path

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# AWS S3 Config
S3_BUCKET = os.environ.get('S3_BUCKET_NAME', 'cinemaplex-videos')
AWS_REGION = os.environ.get('AWS_REGION', 'us-east-1')

s3_client = boto3.client(
    's3',
    region_name=AWS_REGION,
    aws_access_key_id=os.environ.get('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key=os.environ.get('AWS_SECRET_ACCESS_KEY')
)

RESOLUTIONS = {
    '480p':  {'width': 854,  'height': 480,  'bitrate': '800k'},
    '720p':  {'width': 1280, 'height': 720,  'bitrate': '2500k'},
    '1080p': {'width': 1920, 'height': 1080, 'bitrate': '5000k'},
}

def process_video(input_path: str, video_id: str) -> dict:
    logger.info(f"Processing video: {video_id}")
    output_dir = f"/tmp/{video_id}"
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    results = {}

    for quality, settings in RESOLUTIONS.items():
        output_path = f"{output_dir}/{quality}.mp4"
        logger.info(f"Generating {quality} version...")

        cmd = [
            'ffmpeg', '-i', input_path,
            '-vf', f"scale={settings['width']}:{settings['height']}",
            '-b:v', settings['bitrate'],
            '-c:v', 'libx264',
            '-c:a', 'aac',
            '-movflags', '+faststart',
            '-y', output_path
        ]

        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            logger.info(f"Successfully generated {quality}")
            s3_key = f"videos/{video_id}/{quality}.mp4"
            upload_to_s3(output_path, s3_key)
            results[quality] = {
                'status': 'success',
                's3_key': s3_key,
                's3_url': f"https://{S3_BUCKET}.s3.amazonaws.com/{s3_key}"
            }
        else:
            logger.error(f"Failed to generate {quality}: {result.stderr}")
            results[quality] = {'status': 'failed', 'error': result.stderr}

    generate_thumbnail(input_path, video_id, output_dir)
    return results

def upload_to_s3(file_path: str, s3_key: str) -> bool:
    try:
        logger.info(f"Uploading {s3_key} to S3...")
        s3_client.upload_file(
            file_path, S3_BUCKET, s3_key,
            ExtraArgs={'ContentType': 'video/mp4', 'ACL': 'public-read'}
        )
        logger.info(f"Successfully uploaded {s3_key}")
        return True
    except Exception as e:
        logger.error(f"S3 upload failed: {e}")
        return False

def generate_thumbnail(input_path: str, video_id: str, output_dir: str):
    thumbnail_path = f"{output_dir}/thumbnail.jpg"
    cmd = [
        'ffmpeg', '-i', input_path,
        '-ss', '00:00:05',
        '-vframes', '1',
        '-vf', 'scale=640:360',
        '-y', thumbnail_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        s3_key = f"videos/{video_id}/thumbnail.jpg"
        upload_to_s3(thumbnail_path, s3_key)
        logger.info(f"Thumbnail generated and uploaded")

def get_video_info(input_path: str) -> dict:
    cmd = [
        'ffprobe', '-v', 'quiet',
        '-print_format', 'json',
        '-show_streams', '-show_format',
        input_path
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return json.loads(result.stdout)
    return {}

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: python processor.py <input_video> <video_id>")
        sys.exit(1)
    input_path = sys.argv[1]
    video_id = sys.argv[2]
    results = process_video(input_path, video_id)
    print(json.dumps(results, indent=2))
