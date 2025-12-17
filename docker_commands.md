# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume
 
### Create the volume

```bash
volume create fastapi-db
```

### Seed the volume (via Docker Desktop)
i used Docker Desktop
```bash

```

## Server 1

### Build the image

```bash
build -t shopping-server1:v1 .
```

### Run the container

```bash
docker run -it --name shopping-server1 -p 8000:8000 -v fastapi-db:/app/db alpine sh
```

## Server 2

### Build the image

```bash
docker build -t shopping-server2:v1 .
```

### Run the container

```bash
docker run -it --name shopping-server2 -p 8000:8000 -v fastapi-db:/data alpine sh
```
