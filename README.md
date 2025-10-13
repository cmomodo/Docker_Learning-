# Docker Learning

## Overview
This is the docker module from codeco. we go through containerisation using the flask app.

## Repository Structure
- `hello_flask/` &mdash; minimal Flask web app we containerise as the first exercise
- `data/` &mdash; assorted reference files created while experimenting

## Prerequisites
- Docker Engine (Desktop or CLI)
- Optional: Docker Compose if you want to extend the exercises

## Getting Started
1. Explore the `hello_flask/` folder and review the Dockerfile provided there.
2. Build the image: `docker build -t my-flask-app hello_flask`.
3. Run the container locally: `docker run -p 5000:5000 my-flask-app`.
4. Open your browser at `http://localhost:5001` to verify the app is running.

## Docker Networking Walkthrough
Use these steps to try out container-to-container communication.

1. Create a custom network: `docker network create my-custom-network`.
2. Run the Flask container on that network: `docker run -d --name web --network my-custom-network -p 5000:5000 my-flask-app`.
3. Start a MySQL backend container on the same network:
   `docker run -d --name mydb --network my-custom-network -e MYSQL_ROOT_PASSWORD=my-secret-pw mysql:8`.
4. Interact with the containers using `docker exec` or your browser at `http://localhost:5000`.

## Docker Compose

Docker Compose is a tool for defining and running multi-container Docker applications. It uses a YAML file to configure the application's services, networks, and volumes. This allows you to manage your entire application stack with a single command.

### 1. The `docker-compose.yaml` File

A `docker-compose.yaml` file is included in the `hello_flask` directory.The docker-compose file tells the container what to do.

### 2. Running the Application

To run the application using Docker Compose, navigate to the `hello_flask` directory and run the following command:

```bash
docker-compose up
```

This command will build the images (if they don't exist), create and start the containers, and attach your terminal to the container logs.

### 3. Stopping the Application

To stop and remove the containers, networks, and volumes created by `docker-compose up`, run the following command from the `hello_flask` directory:

```bash
docker-compose down
```
## The docker challenge:
This was the docker challenge , it shows how we use docker not only to deploy applications but also to manage them. we made the website stylish and responsive using docker-compose.

It follows the same principles as the docker challenge principles.
