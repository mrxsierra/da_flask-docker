# README.Docker.md

## Building and Running Your Application

When you're ready, start your application by running:

```bash
docker compose up --build
```

Your application will be available at [http://localhost:5000](http://localhost:5000).

## Deploying Your Application to the Cloud

1. First, build your image:

   ```bash
   docker build -t myapp .
   ```

   If your cloud uses a different CPU architecture than your development machine (e.g., you are on a Mac M1 and your cloud provider is amd64), you'll want to build the image for that platform:

   ```bash
   docker build --platform=linux/amd64 -t myapp .
   ```

2. Then, push it to your registry:

   ```bash
   docker push myregistry.com/myapp
   ```

   Replace `myregistry.com` with your actual registry.

Consult Docker's [getting started](https://docs.docker.com/go/get-started-sharing/) docs for more detail on building and pushing.

## References

* [Docker's Python Guide](https://docs.docker.com/language/python/)