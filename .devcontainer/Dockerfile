# McpServer Development Container
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install Python development dependencies
COPY requirements.dev.txt /tmp/requirements.dev.txt
RUN pip install -r /tmp/requirements.dev.txt

# Install project dependencies
COPY requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
