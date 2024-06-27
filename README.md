# Ingestion Service for Cloud Native Applications

## Abstract
Large web applications face the challenge of serving a massive influx of requests, leading to variable loads on servers. During peak hours, servers must manage many requests, which can lead to performance delays. This project builds an ingestion service for cloud-native applications, acting as a proxy to handle client requests efficiently. The proxy forwards client requests to an Envoy proxy, which sends them to Kafka before finally reaching the service (an SQL service in this case).

## Motivation
Our motivation stems from challenges faced by Twitter customers interacting directly with Elasticsearch for real-time indexing. At large scales, this approach caused significant performance bottlenecks. To address this, we created an ingestion service to manage server loads more efficiently, ensuring high stability and performance for end-users.

## Implementation
Our proxy is built on Envoy, with services using gRPC instead of HTTP to enhance performance. Kafka handles data ingestion with one topic per cluster, and rate-limiting and buffering are employed to manage queries effectively.

### Features
- Internal authenticated requests
- Load balancing using the Weighted Least Request Algorithm
- Database replication with a Master/Slave pattern
- Configurable rate limiting to the end service
- Retries and backfill for failed requests

## Testing
We performed extensive load testing using ApacheBench and Siege to evaluate our service. The results demonstrated significant improvements in stability and performance with our ingestion service.

## Conclusion and Future Work
Our ingestion service successfully manages server loads and ensures high stability and performance for end-users. Future work includes testing with different backend services and more extensive testing.

## Watch the YouTube Video
For a detailed walkthrough of the project, watch our YouTube video: [Ingestion Service for Cloud Native Applications](https://www.youtube.com/watch?v=b0ZJNw2IsAM)
