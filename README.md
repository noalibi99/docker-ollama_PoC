# Docker/Ollama Demo Project

A proof-of-concept project demonstrating how to run Ollama (Large Language Model) in a Docker container and interact with it through a Python CLI application.

## Overview

This project sets up a complete environment for running and testing Ollama models using Docker Compose. It includes:
- Ollama server running in a Docker container
- Automatic model downloading (TinyLlama)
- Python CLI application to interact with the model

## Prerequisites

- Docker and Docker Compose installed on your system

## Quick Start

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd docker_ollama_PoC
   ```

2. **Start the services:**
   ```bash
   docker-compose run --rm app
   ```

3. **Wait for the setup to complete:**
   - Ollama server will start and become healthy
   - TinyLlama model will be downloaded automatically
   - The Python CLI will start and ask a sample question

## Project Structure

```
docker_ollama_PoC/
├── docker-compose.yml    # Main orchestration file
├── Dockerfile           # Python app container definition
├── README.md           # This file
├── app/
│   ├── cli.py          # Python CLI application
│   └── requirements.txt # Python dependencies
└── env/                # Python virtual environment (local development)
```