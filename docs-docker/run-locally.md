# Running locally

### Requirements:
- Dockerfile

1. To build the image locally, run the following command:

```bash
docker build -t my-image-name .
```

Replace "my-image-name" with a name of your choice.

2. Now, run a container from the image:

```bash
docker run -it --name my-container-name my-image-name
```

**Flag meanings:**
- `-it`: interactive mode, for terminals

- `--name`: specify a unique name for the container to refer to by later

- `--rm`: to auto-remove container when its stopped

**To stop or remove a container:**

First run `docker ps` to list the running containers in order to acquire the desired <container_id_or_name>

```bash
docker rm <container_id_or_name>
```

```bash
docker stop <container_id_or_name>
```