# Weather with Docker and K8S

This is a simple Django application that provides weather data for a given city using the weatherstack API. The application is Dockerized and can be deployed to Kubernetes.

The full description of the project can be found in [instructions.pdf](instructions.pdf) and [report.pdf](report.pdf) (in Persian).

## Endpoints
- `/ping` - Health check.
- `/weather` - Returns weather data for a configured city by calling the `weather-url` set in the configuration file.

## Using the project

- Run the project locally by running `python manage.py server`
- Use the dockerized version by running:
```bash
  docker build -t weatherapp -f Dockerfile .
  docker run -p 8000:8000 weatherapp
```
- Deploy using kubernetes with `kubectl apply -f k8s/`

The configuration file is assumed to be at where `CONFIG_PATH` environment variable points to (default `src/config/conf.yml`). A template for this file is available at [config/conf.template.yml](src/config/conf.template.yml).

## Course Information
- **Course**: Cloud Computing
- **University**: Amirkabir University of Technology  
- **Semester**: Spring 2022

Let me know if you have any questions!

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)