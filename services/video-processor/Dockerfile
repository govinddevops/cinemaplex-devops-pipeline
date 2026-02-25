# Stage 1: Builder
FROM python:3.11-alpine AS builder
WORKDIR /app
RUN apk add --no-cache \
    ffmpeg \
    gcc \
    musl-dev \
    libffi-dev
COPY requirements.txt .
RUN pip install --no-cache-dir --user -r requirements.txt

# Stage 2: Production
FROM python:3.11-alpine AS production
LABEL maintainer="govinddevopsdocker"
LABEL description="Cinemaplex Video Processor - FFmpeg Pipeline"
RUN apk add --no-cache ffmpeg
WORKDIR /app
COPY --from=builder /root/.local /root/.local
COPY . .
RUN addgroup -S appgroup && adduser -S appuser -G appgroup
RUN mkdir -p /tmp/videos && chown appuser:appgroup /tmp/videos
USER appuser
ENV PATH=/root/.local/bin:$PATH
ENV PYTHONUNBUFFERED=1
EXPOSE 5001
HEALTHCHECK --interval=30s --timeout=10s --retries=3 \
  CMD wget --spider http://localhost:5001/health || exit 1
CMD ["gunicorn", "--bind", "0.0.0.0:5001", "--workers", "2", "processor:app"]
