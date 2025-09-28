# Stage 0 – common base with uv binaries available
FROM python:3.12-slim-bookworm AS base
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/

#using the environment variables
ENV UV_PROJECT_ENV=.venv \
    UV_CACHE_DIR=/root/.cache/uv \
    PATH="/app/.venv/bin:${PATH}"

# the working directory
WORKDIR /app

# Stage 1 – build dependencies and create the virtualenv
FROM base AS builder
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    default-libmysqlclient-dev \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*
COPY pyproject.toml uv.lock ./
RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --locked --no-dev

# copy the source code
COPY . .

# Stage 2 – slim runtime image
FROM python:3.12-slim-bookworm AS runtime
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/
ENV UV_PROJECT_ENV=.venv \
    PATH="/app/.venv/bin:${PATH}"
WORKDIR /app
COPY --from=builder /app /app
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    libmysqlclient21 \
    && rm -rf /var/lib/apt/lists/*
EXPOSE 5001
CMD ["uv", "run", "python", "app.py"]
