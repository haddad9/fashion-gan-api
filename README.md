# Fashion GAN API

This repository contains a Flask application for generating fashion designs using a Generative Adversarial Network (GAN). The application is containerized using Docker and deployed on a Kubernetes cluster.

## Project Structure

- **src/**: Contains the source code for the application.
  - **app.py**: Main Flask application file.
  - **ingestion.py**: Handles data ingestion.
  - **data_preprocessing.py**: Preprocesses data for training.
  - **model_building.py**: Contains functions to build the GAN models.
  - **training.py**: Compiles and trains the GAN.
  - **deployment.py**: Deploys the model to Google Vertex AI.
  - **inference.py**: Generates fashion designs using the trained generator.

- **k8s/**: Contains Kubernetes configuration files.
  - **deployment.yaml**: Defines the deployment for the GAN inference service.
  - **service.yaml**: Exposes the GAN inference service.
  - **autoscaler.yaml**: Configures horizontal pod autoscaling.
  - **ingress.yaml**: Manages external access to the service.

- **Dockerfile**: Defines the Docker image for the application.

- **requirements.txt**: Lists Python dependencies.

- **run.sh**: Script to apply Kubernetes configurations.


## Building the Docker Image

1. **Build the Docker Image**:
   ```bash
   docker build -t your-docker-repo/fashion-gan-api:latest .
   ```

2. **Push the Docker Image**:
   ```bash
   docker push your-docker-repo/fashion-gan-api:latest
   ```

## Deploying to Kubernetes

1. **Update Kubernetes Configurations**:
   - Replace `<PUT-THE-DOCKER-IMAGE-HERE🐋🐋>` in `k8s/deployment.yaml` with your Docker image name.
   - Update the domain in `k8s/ingress.yaml` if using a custom domain.

2. **Apply Configurations**:
   Run the `run.sh` script to apply all Kubernetes configurations:
   ```bash
   ./run.sh
   ```

3. **Verify Deployment**:
   - Check the status of your pods:
     ```bash
     kubectl get pods
     ```
   - Check the status of your services:
     ```bash
     kubectl get services
     ```
   - Check the status of your ingress:
     ```bash
     kubectl get ingress
     ```

## Accessing the Application

- If using a LoadBalancer service, access the application via the external IP.
- If using Ingress, access the application via the specified domain and path (e.g., `http://your-domain.com/generate`).

## Notes

- Ensure your Kubernetes cluster has an Ingress controller installed (e.g., NGINX).
- For HTTPS, configure TLS in the Ingress resource and manage certificates using a tool like Cert-Manager.
