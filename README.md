# MCP-Sim Starter Kit

This repository is the official developer starter kit for MCP-Sim, a platform for creating and composing scientific micro-models. It provides all the tools and documentation needed to build and contribute new models to the ecosystem.

## What's Inside?

This repository contains all the public-facing assets for the MCP-Sim platform:

- **`/mcp_node_sdk/`**: The core Python SDK required to build a new model node. It provides the base classes and utilities for handling the Model Control Protocol (MCP).
- **`/docs_site/`**: The source code for our official documentation website, built with Docusaurus.
- **`/templates/`**: The default project templates used by the `create-mcp-node` CLI tool.

**Note:** The private, core infrastructure for the MCP-Sim router and platform is maintained in a separate repository. This starter kit is designed for public use and contributions.

## 🚀 Getting Started

The best way to begin is by following the [Quick Start Guide](https://AJ-EN.github.io/mcp-sim-starter-kit/docs/quick-start) on our documentation site.

You can create your first model node in under 10 minutes.

### 1. Install the SDK from PyPI

```bash
pip install mcp-node-sdk
```

### 2. Scaffold a New Model Node

```bash
npx create-mcp-node your-new-model
cd your-new-model
```

From here, follow the tutorials on our [documentation site](https://AJ-EN.github.io/mcp-sim-starter-kit/) to add your logic and deploy your model.

## 🛠️ Contributing to the Documentation

We welcome contributions to improve our documentation! If you find a typo, want to clarify a section, or add a new guide, you can run the documentation site locally.

### 1. Navigate to the Docs Site Directory

```bash
cd docs_site
```

### 2. Install Dependencies

```bash
npm install
```

### 3. Start the Local Development Server

```bash
npm start
```

This will open the documentation site in your browser at `http://localhost:3000`. Most changes are reflected live without needing to restart the server.

## 🤝 Contributing

We are actively looking for contributors to build new scientific models for the MCP-Sim ecosystem. Whether your expertise is in climate science, hydrology, economics, or another field, you can package your model as a node and add it to the platform.

To get started, please read our [Contributing Guide](https://AJ-EN.github.io/mcp-sim-starter-kit/docs/contributing) for guidelines on code standards, pull requests, and the contribution process.

## 📄 License

This project is licensed under the MIT License. See the LICENSE file for details.
