FROM python:3.10.7
RUN apt-get update && apt-get -q install -y --no-install-recommends \
    curl python3-pip

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade setuptools && \
    python3 -m pip install grpcio grpcio-tools

ENV PROTOCOL_BUFFERS_PYTHON_IMPLEMENTATION=python
WORKDIR /source/greeter
COPY . .

ENTRYPOINT ["python3", "greeter_client.py"]

