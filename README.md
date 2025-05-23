# k8s-assistant

A natural language interface for Kubernetes troubleshooting powered by AI

## Features

- 🤖 Natural language queries for Kubernetes operations
- 🔒 Safe operations - prevents destructive commands
- 📊 AI-powered analysis and root cause identification
- 🎯 Intelligent command suggestions
- 📝 Detailed troubleshooting reports
- 🖥️ Cross-platform support (Windows, macOS, Linux)

## Prerequisites

1. Python 3.10+
2. kubectl installed and configured
3. Anthropic API key (Claude)
4. OpenAI API key (GPT)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/k8s-assistant.git
   ```

2. Navigate to the project directory:
   ```bash
   cd k8s-assistant
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Install the package:
   ```bash
   pip install -e .
   ```


## Run the assistant

```bash
k8s-assistant
```

## Usage Examples

- "List all pods in the kube-system namespace"
- "Show me pods that are not running" 
- "Check the status of my deployments"
- "What's wrong with my cluster?"
- "Show me resource usage"

## Configuration

Set your API keys in the configuration files:
- Edit `k8s_assistant/llms/claude.py` - add your Anthropic API key
- Edit `k8s_assistant/llms/gpt.py` - add your OpenAI API key

Or use environment variables:
```bash
export ANTHROPIC_API_KEY="your-claude-key"
export GPT_API_KEY="your-openai-key"
```
