# Bolt New LLM Proxy

This project provides an **LLM proxy** that intelligently routes requests to either a local LLM or the OpenAI API based on token usage.

## Features
- Route requests locally if within token limits.
- Use OpenAI's GPT-4 when tokens exceed the threshold.
- Logs requests and responses for auditing.

## Setup

### Prerequisites
- Python 3.x
- `pip` (Python package manager)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your_username/bolt-new-llm-proxy.git
   cd bolt-new-llm-proxy