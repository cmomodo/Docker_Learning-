FROM python:3.12-slim-bookworm
COPY --from=docker.io/astral/uv:latest /uv /uvx /bin/


#set working directory
WORKDIR /app

#install mysql client 
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        default-libmysqlclient-dev \
        default-mysql-client \
        pkg-config \
    && rm -rf /var/lib/apt/lists/*

   #Install dependencies
RUN --mount=type=cache,target=/root/.cache \
    --mount=type=bind,source=uv.lock,target=uv.lock \
    --mount=type=bind,source=pyproject.toml,target=pyproject.toml \
    uv sync \
        --locked \
        --no-dev \
        --no-install-project

#Copy 
COPY . .

#Expose the port
EXPOSE 5001
#Run the application
CMD ["uv", "run", "python", "app.py"]
