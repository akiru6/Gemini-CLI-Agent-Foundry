
# Gemini-CLI Agent Foundry

Welcome to the Gemini Agent Foundry! This repository showcases a powerful, prompt-driven workflow I developed for building sophisticated AI agents using the Gemini CLI. It demonstrates a refined methodology for taking a product idea from a requirement document to a fully functional, multi-tool conversational agent through a structured, automated process.

This project was inspired by the **Product Requirement Prompt (PRP)** framework originally proposed by [Wirasm's PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng). I have extended this concept by creating a comprehensive, end-to-end workflow tailored specifically for the **Gemini CLI**, demonstrating my unique approach to agentic programming.


---

## The Core Philosophy: From Requirement to Reality

The central idea of this repository is to treat AI agent development not as a single, monolithic task, but as a structured, two-phase process orchestrated by distinct meta-prompts:

1.  **`generate-prp.md` (The Architect):** This process acts as an AI architect. It consumes a high-level product requirement, researches internal blueprints and external documentation, and produces a detailed, executable **Product Requirement Prompt (PRP)**. This PRP is the master plan for the entire project.

2.  **`execute-prp.md` (The Builder):** This process acts as an AI software engineer. It takes the PRP generated in the first step and follows its instructions precisely to write, test, and validate the full application code.

This separation of concerns—planning then executing—allows for a more robust, predictable, and scalable way to build complex agents.

## The Three-Layer Agent Architecture

At the heart of my methodology is the **"Conversational Analyst"** architecture, a three-layer model that I enforce through my project templates (`PRPs/templates/Architectural_Blueprint_Base.md`):

1.  **Orchestration Layer (The Brain):** An LLM-driven core (`agent_orchestrator.py`) responsible for reasoning, understanding user intent, selecting the correct tool, and synthesizing data into human-friendly responses.
2.  **Capability Layer (The Skills):** A collection of discrete, single-purpose tools (`tools/`) that represent the agent's abilities, such as planning an activity or fetching a weather report.
3.  **Service Layer (The Senses):** The lowest-level clients (`services/`) that provide a direct, simple connection to external APIs (e.g., Google Calendar, Open-Meteo).

This layered approach hides complexity from the LLM, making its decision-making (tool selection) task simpler and more reliable.

## How to Use This Workflow

This repository is designed to be a working example and a template for your own projects. Here's how you can replicate the process using the Gemini CLI:

### Step 1: Define Your Vision

Start by writing a high-level product requirement for your agent in a `product_requirement.md` file. Define what the agent should do, its core capabilities, and any dependencies.

### Step 2: Generate the Master Plan (PRP)

Use the `generate-prp.md` meta-prompt as the instruction set for the Gemini CLI. This will create your detailed PRP file.

```bash
# Example command to instruct Gemini CLI
gemini -p Process/generate-prp.md \
  --prompt-vars requirement="PRPs/product_requirement.md" \
  --prompt-vars template="PRPs/templates/*.md" \
  --prompt-vars output="PRPs/kai_weather_advisor.prp.md"
```

*This command tells the AI to act as an architect, using the product requirement and available templates to generate the `kai_weather_advisor.prp.md` file.*

### Step 3: Build the Agent

Once the PRP is generated, use the `execute-prp.md` meta-prompt to instruct the Gemini CLI to build the application.

```bash
# Example command to instruct Gemini CLI
gemini -p Process/execute-prp.md \
  --prompt-vars prp="PRPs/kai_weather_advisor.prp.md"```

*This command tells the AI to act as a builder, following the detailed instructions within the PRP to write the code, set up the project structure, and create the necessary tests.*

### Step 4: Validate and Run

After the AI completes the build process, you can validate and run the application.

1.  **Set up your environment:**
    ```bash
    # Create and activate a virtual environment
    python3 -m venv venv
    source venv/bin/activate

    # Install dependencies
    pip install -e .
    # (This installs dependencies from pyproject.toml in editable mode)
    ```

2.  **Configure your secrets:**
    -   Copy `.env.example` to `.env`.
    -   Fill in your API keys and credentials as detailed in the PRP's "Prerequisites & Setup Guide".

3.  **Run the application:**
    ```bash
    streamlit run app.py
    ```

## The Example: "Kai" Weather Advisor

This repository contains a complete, working example of this process applied to create **"Kai," a conversational weather advisor.** Kai can understand user requests, plan activities based on weather, provide direct forecasts, and schedule events on Google Calendar after receiving user confirmation. The entire `src/` directory is the output of this AI-driven workflow.

I hope this repository serves as a valuable resource for anyone interested in the future of agentic programming and building reliable AI systems with modern tools.
````


# Gemini-CLI Agent Foundry (Gemini 智能体铸造厂)

欢迎来到 Gemini-CLI 智能体铸造厂！本仓库展示了一套我使用 Gemini CLI 开发的、强大的、由 Prompt 驱动的工作流，用于构建复杂的 AI 智能体。它演示了一套经过优化的方法论，通过结构化、自动化的流程，将一个产品构想从需求文档转化为一个功能齐全、拥有多工具能力的对话式智能体。

本项目的设计灵感来源于 [Wirasm 的 PRPs-agentic-eng](https://github.com/Wirasm/PRPs-agentic-eng) 仓库所提出的 **PRP (产品需求 Prompt)** 框架。我扩展了这一概念，创建了一套专门为 **Gemini CLI** 量身定制的、端到端的完整工作流，展示了我在“智能体编程 (Agentic Programming)”领域的独特实践。

---

## 核心理念：从需求到现实

本仓库的核心思想，是将 AI 智能体的开发视为一个结构化的、分两阶段的流程，而非单一的、庞杂的任务。整个流程由两个不同的“元指令 (Meta-Prompts)”来编排：

1.  **`generate-prp.md` (扮演架构师):** 此流程扮演 AI 架构师的角色。它接收一个高阶的产品需求，研究内部的技术蓝图和外部的官方文档，最终生成一份详尽的、可执行的 **PRP (产品需求 Prompt)**。这份 PRP 是整个项目的总蓝图。

2.  **`execute-prp.md` (扮演构建者):** 此流程扮演 AI 软件工程师的角色。它接收第一步生成的 PRP，并严格遵循其中的指令来编写、测试和验证完整的应用程序代码。

这种“规划”与“执行”相分离的模式，使得构建复杂的智能体变得更加健壮、可预测和可扩展。

## 三层智能体架构

我这套方法论的核心是 **“对话式分析师 (Conversational Analyst)”** 架构，这是一个三层模型，我通过项目模板 (`PRPs/templates/Architectural_Blueprint_Base.md`) 来强制执行：

1.  **编排层 (大脑):** 由 LLM 驱动的核心 (`agent_orchestrator.py`)，负责推理、理解用户意图、选择正确的工具，并将原始数据整合为人类友好的响应。
2.  **能力层 (技能):** 一系列离散的、单一用途的工具 (`tools/`)，代表了智能体的各项能力，例如规划活动或获取天气报告。
3.  **服务层 (感官):** 最底层的客户端 (`services/`)，提供与外部 API (如 Google Calendar, Open-Meteo) 的直接、简单的连接。

这种分层架构对 LLM 隐藏了底层的复杂性，使其核心决策（工具选择）任务变得更简单、更可靠。

## 如何使用此工作流

本仓库既是一个可运行的范例，也是一个可供您自己项目使用的模板。您可以按照以下步骤，使用 Gemini CLI 来复现整个流程：

### 第一步：定义你的构想

首先，在一个 `product_requirement.md` 文件中，为你的智能体编写一份高阶的产品需求。定义智能体应该做什么、其核心能力以及任何依赖项。

### 第二步：生成总蓝图 (PRP)

使用 `generate-prp.md` 这个元指令作为 Gemini CLI 的输入。这将为您创建详细的 PRP 文件。

```bash
# 指示 Gemini CLI 的示例命令
gemini -p Process/generate-prp.md \
  --prompt-vars requirement="PRPs/product_requirement.md" \
  --prompt-vars template="PRPs/templates/*.md" \
  --prompt-vars output="PRPs/kai_weather_advisor.prp.md"
```

*该命令指示 AI 扮演架构师的角色，使用产品需求和可用的模板来生成 `kai_weather_advisor.prp.md` 文件。*

### 第三步：构建智能体

PRP 生成后，使用 `execute-prp.md` 元指令来指示 Gemini CLI 构建应用程序。

```bash
# 指示 Gemini CLI 的示例命令
gemini -p Process/execute-prp.md \
  --prompt-vars prp="PRPs/kai_weather_advisor.prp.md"
```

*该命令指示 AI 扮演构建者的角色，遵循 PRP 中的详细指令来编写代码、设置项目结构并创建必要的测试。*

### 第四步：验证与运行

在 AI 完成构建过程后，您可以验证并运行应用程序。

1.  **设置您的环境:**
    ```bash
    # 创建并激活虚拟环境
    python3 -m venv venv
    source venv/bin/activate

    # 安装依赖
    pip install -e .
    # (该命令会以可编辑模式从 pyproject.toml 安装依赖)
    ```

2.  **配置您的密钥:**
    -   将 `.env.example` 复制为 `.env`。
    -   根据 PRP 文件中“先决条件与设置指南”部分的详细说明，填入您的 API 密钥和凭据。

3.  **运行应用程序:**
    ```bash
    streamlit run app.py
    ```

## 范例项目: "Kai" 天气顾问

本仓库包含了一个应用此流程的完整范例，用于创建 **"Kai"——一个对话式天气顾问**。Kai 能够理解用户请求，根据天气规划活动，提供直接的天气预报，并在获得用户确认后在 Google Calendar 上创建日程。整个 `src/` 目录就是这个由 AI 驱动的工作流的最终产物。

我希望这个仓库能为所有对“智能体编程”的未来以及使用现代工具构建可靠 AI 系统感兴趣的人，提供一份宝贵的资源。
````

