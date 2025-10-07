# Kit Bot Chatbot

This is an AI chatbot powered by Ollama's local LLMs (e.g. Mistral), built in Python and containerized with Docker.

## Prerequisites

- Docker installed
- [Ollama](https://ollama.com) installed locally and running
- Download a model (e.g. mistral): `ollama run mistral`

## Run the Bot

```bash
docker-compose run --rm -it chatbot
