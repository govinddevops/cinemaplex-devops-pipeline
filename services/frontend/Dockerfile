FROM node:18-alpine AS production
LABEL maintainer="govinddevopsdocker"
LABEL description="Cinemaplex Frontend"
WORKDIR /app
COPY package*.json ./
RUN npm install --silent
COPY . .
EXPOSE 3000
CMD ["npm", "start"]
