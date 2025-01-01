# Stage 1: Use Node.js for building TailwindCSS
FROM node:20 AS node-build

WORKDIR /app/theme/static_src

# Copy the necessary files for TailwindCSS
COPY ./app/theme/static_src/package*.json ./
RUN echo "Checking copied package files:" && ls -l ./ && cat package.json

COPY ./app/theme/static_src ./
RUN echo "Checking copied source files:" && ls -R ./src

# Install dependencies and log the process
RUN echo "Installing Node.js dependencies..." && \
  npm install && \
  echo "Dependencies installed successfully."

# Run the build process and log outputs
RUN echo "Building TailwindCSS assets..." && \
  npm run build --loglevel verbose && \
  echo "Build completed successfully. Checking output files:" && \
  ls -l /app/theme/static/css/dist

# Stage 2: Use Python for the Django app
FROM python:3.9-alpine3.13
LABEL maintainer="metalbrain.net"

COPY ./requirements.txt /tmp/requirements.txt
COPY ./requirements.dev.txt /tmp/requirements.dev.txt
COPY ./scripts /scripts
COPY ./app /app
WORKDIR /app

# Copy built static files from node-build stage
COPY --from=node-build /app/theme/static /app/theme/static

EXPOSE 3000

ARG DEV=true


# RUN apk add --update --no-cache nodejs npm
# Upgrade npm to the latest version
# RUN npm install -g npm@latest

RUN python -m venv /py && \
  /py/bin/pip install --upgrade pip && \
  apk add --update --no-cache postgresql-client && \
  apk add --update --no-cache --virtual .tmp-build-deps \
  build-base postgresql-dev musl-dev zlib zlib-dev linux-headers && \
  /py/bin/pip install -r /tmp/requirements.txt && \
  if [ "$DEV" = "true" ]; \
  then /py/bin/pip install -r /tmp/requirements.dev.txt; \
  fi && \
  rm -rf /tmp && \
  apk del .tmp-build-deps && \
  adduser \
  --disabled-password \
  --no-create-home \
  django-user && \
  mkdir -p /vol/web/media && \
  mkdir -p /vol/web/static && \
  chown -R django-user:django-user /vol && \
  chmod -R 755 /vol && \
  chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER django-user

CMD ["run.sh"]