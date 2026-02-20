# AgenticOdyssey 🤖

Welcome to **AgenticOdyssey** — the FY26-H2 hands-on workshop for building intelligent AI agents with Azure OpenAI, GitHub Copilot, and the latest agentic frameworks.

## 🎯 Workshop Overview

This workshop guides participants through the end-to-end journey of understanding, building, and deploying AI agents. Whether you're new to agentic AI or looking to level up your skills, this workshop has something for you.

**Duration:** ~4 hours (full-day option available)  
**Audience:** Developers, AI practitioners, and architects  
**Level:** Intermediate (some Python and Azure familiarity recommended)

---

## 📋 Prerequisites

Before attending the workshop, ensure you have:

- [Python 3.10+](https://www.python.org/downloads/) installed
- An [Azure subscription](https://azure.microsoft.com/free/) with Azure OpenAI access
- [Azure CLI](https://docs.microsoft.com/cli/azure/install-azure-cli) installed and configured
- [VS Code](https://code.visualstudio.com/) with the [GitHub Copilot extension](https://marketplace.visualstudio.com/items?itemName=GitHub.copilot)
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (for containerized demos)
- Git installed and a GitHub account

See [docs/SETUP.md](docs/SETUP.md) for detailed environment setup instructions.

---

## 🗂️ Workshop Structure

```
AgenticOdyssey/
├── docs/                          # Workshop slides and setup guides
│   ├── SETUP.md                   # Environment setup guide
│   └── slides/                    # Presentation slides
├── labs/                          # Hands-on labs
│   ├── lab01-intro-to-agents/     # Lab 1: Introduction to AI Agents
│   ├── lab02-first-agent/         # Lab 2: Building Your First Agent
│   ├── lab03-multi-agent/         # Lab 3: Multi-Agent Orchestration
│   └── lab04-rag-agents/          # Lab 4: RAG-Powered Agents
└── demos/                         # Live demonstrations
    ├── demo01-coding-agent/       # Demo 1: Autonomous Coding Agent
    └── demo02-research-pipeline/  # Demo 2: Multi-Agent Research Pipeline
```

---

## 🧪 Labs

| Lab | Title | Duration | Topics |
|-----|-------|----------|--------|
| [Lab 01](labs/lab01-intro-to-agents/README.md) | Introduction to AI Agents | 30 min | Agent concepts, ReAct pattern, tool use |
| [Lab 02](labs/lab02-first-agent/README.md) | Building Your First Agent | 45 min | Azure OpenAI, function calling, memory |
| [Lab 03](labs/lab03-multi-agent/README.md) | Multi-Agent Orchestration | 60 min | AutoGen, agent roles, conversation patterns |
| [Lab 04](labs/lab04-rag-agents/README.md) | RAG-Powered Agents | 45 min | Vector search, grounding, Azure AI Search |

---

## 🎬 Demos

| Demo | Title | Topics |
|------|-------|--------|
| [Demo 01](demos/demo01-coding-agent/README.md) | Autonomous Coding Agent | GitHub Copilot Agent, code generation, testing |
| [Demo 02](demos/demo02-research-pipeline/README.md) | Multi-Agent Research Pipeline | Orchestration, web search, summarization |

---

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/lapate/AgenticOdyssey.git
   cd AgenticOdyssey
   ```

2. **Set up your environment**
   ```bash
   # Create and activate a virtual environment
   python -m venv .venv
   source .venv/bin/activate      # Linux/macOS
   .venv\Scripts\activate         # Windows

   # Install shared dependencies
   pip install -r requirements.txt
   ```

3. **Configure Azure credentials**
   ```bash
   cp .env.example .env
   # Edit .env with your Azure OpenAI keys and endpoints
   ```

4. **Start with Lab 01**
   ```bash
   cd labs/lab01-intro-to-agents
   ```

---

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding new labs, fixing issues, or improving documentation.

---

## 📚 Resources

- [Azure OpenAI Documentation](https://learn.microsoft.com/azure/ai-services/openai/)
- [AutoGen Documentation](https://microsoft.github.io/autogen/)
- [Semantic Kernel Documentation](https://learn.microsoft.com/semantic-kernel/)
- [GitHub Copilot Docs](https://docs.github.com/copilot)
- [LangChain Documentation](https://python.langchain.com/)

---

## 📄 License

This project is licensed under the MIT License — see [LICENSE](LICENSE) for details.
