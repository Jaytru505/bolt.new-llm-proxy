# .gitpod.Dockerfile
FROM gitpod/workspace-full:latest

# Install Python and mitmproxy
RUN apt-get update && \
    apt-get install -y python3 python3-pip && \
    pip install mitmproxy openai tiktoken requests

# Expose the necessary port
EXPOSE 8080
