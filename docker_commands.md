# Docker Commands

Fill in the Docker commands you used to complete the test.

## Volume
 
### Create the volume
volume create fastapi-db 
```bash

```

### Seed the volume (via Docker Desktop)
docker run -it --name fastapi-app -v fastapi-db:/app/db alpine sh
```bash

```

## Server 1

### Build the image
build -t shopping-server1:v1 .
```bash

```

### Run the container
docker run -i -t shopping-server2:v1 /bin/bash
```bash

```

## Server 2

### Build the image
docker build -t shopping-server2:v1 .
```bash

```

### Run the container
docker run -it --name shopping-server2 -v fastapi-db:/data alpine sh 
```bash

```
