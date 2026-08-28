FROM ubuntu:latest

LABEL maintainer="MLOpsLabs <tgvae1122@gmail.com>"

WORKDIR /mlops

COPY . .

RUN apt-get update \
    && apt-get install -y python3 python3-pip python3-venv \
    && python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip \
    && /opt/venv/bin/pip install fastapi uvicorn \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

ENV PATH="/opt/venv/bin:$PATH"

EXPOSE 80

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "80"]