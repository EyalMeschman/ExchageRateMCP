# McpServer Development Container
FROM mcr.microsoft.com/devcontainers/python:3.12

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

# Set working directory
WORKDIR /workspace

# Copy project files from workspace root (build context is parent directory)
COPY pyproject.toml uv.lock ./

# Install dependencies with uv
RUN uv sync --group dev --frozen
