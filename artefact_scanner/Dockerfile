FROM ubuntu:22.04

ENV SQLALCHEMY_DATABASE_URI=postgresql://administrator:verySecretPassword@host.docker.internal:5432/db
ENV AWS_ACCESS_KEY_ID=""
ENV AWS_SECRET_ACCESS_KEY=""
ENV AWS_SESSION_TOKEN=""

# Installing dependencies for running a python application
RUN apt-get update && \
        apt-get install -y python3 python3-pip postgresql-client libpq-dev wget && \
        apt-get clean && \
        rm -rf /var/lib/apt/lists/*

WORKDIR /artefact_scanner

# Install poetry dependencies
COPY requirements.txt ./
RUN pip3 install -r requirements.txt

# Copying our application into the container
COPY src src


CMD ["python3", "-u", "src/main.py"]
