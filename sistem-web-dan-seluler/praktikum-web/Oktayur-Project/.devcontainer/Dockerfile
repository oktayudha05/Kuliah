FROM mcr.microsoft.com/devcontainers/php:8.4

RUN apt-get update \
 && apt-get install -y docker.io docker-compose \
 && rm -rf /var/lib/apt/lists/*

COPY --from=composer:2 /usr/bin/composer /usr/bin/composer

WORKDIR /workspace
