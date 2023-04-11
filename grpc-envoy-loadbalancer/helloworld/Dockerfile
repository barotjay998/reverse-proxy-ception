FROM grpc/python
FROM envoyproxy/envoy:v1.18.3
RUN apt-get update && apt-get -q install -y --no-install-recommends \
    curl python3-pip

RUN python3 -m pip install --upgrade pip && \
    python3 -m pip install --upgrade setuptools && \
    python3 -m pip install grpcio grpcio-tools

WORKDIR /source/greeter
COPY . .

ENTRYPOINT ["/source/greeter/start_service.sh"]

