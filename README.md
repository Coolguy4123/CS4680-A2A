# CS 4680 A2A Assignment

This repo contains a simple A2A setup with:
- an Echo agent
- a Reverse agent
- a small Python client
- deployment scripts for Cloud Run and Agent Engine

## Environment Setup

Start by creating a virtual environment and installing the dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r server/requirements.txt
pip install -r reverse_server/requirements.txt
pip install flake8
```

## Running Locally

To run the Echo server locally:

```bash
cd server
uvicorn main:app --reload
```

To run the Reverse server locally on a different port:

```bash
cd reverse_server
uvicorn main:app --reload --port 8001
```

To test the client against the Echo server:

```bash
python3 client/demo.py http://localhost:8000
```

To chain Echo into Reverse with the coordinator:

```bash
python3 client/coordinator.py http://localhost:8000 http://localhost:8001 "Hello World"
```

## Cloud Deployment

To deploy the Echo agent to Cloud Run:

```bash
bash cloud/deploy_cloud_run.sh
```

To deploy the Reverse agent to Cloud Run:

```bash
bash cloud/deploy_reverse_cloud_run.sh
```

To deploy the Agent Engine version:

```bash
python3 cloud/deploy_agent_engine.py
```

## Cloud Run URL

Current Echo Cloud Run service URL:

```text
https://echo-a2a-agent-dl52rreheq-uc.a.run.app
```

## Linting

To check that the Python files pass flake8:

```bash
flake8 .
```
