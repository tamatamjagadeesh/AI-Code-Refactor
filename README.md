# 🚀 Autonomous AI Code Refactoring Agent (Gemini-Powered)

An **autonomous AI agent** that analyzes a codebase, detects code smells, refactors code using **Google Gemini**, and automatically creates **GitHub pull requests** — with safe Git workflows and real-world constraints handled.

---

## 📌 Overview

This project demonstrates an **agentic AI system** that operates on a real GitHub repository:

- Clones a target repository
- Analyzes committed source code
- Detects code smells using rule-based static analysis
- Uses **Gemini LLM** to refactor code while preserving behavior
- Creates or updates Git branches
- Pushes changes and opens GitHub Pull Requests automatically
- Avoids duplicate PRs and unnecessary commits

The system is designed to be **extensible, safe, and production-oriented**, not just a demo script.

---

## ✨ Key Features

- 🤖 **Autonomous Refactoring Agent**  
  Runs without manual intervention once configured.

- 🧠 **LLM-Powered Refactoring (Gemini)**  
  Uses prompt-driven refactoring while preserving original logic.

- 🔍 **Rule-Based Code Smell Detection**  
  Currently supports nested conditional detection (extensible by design).

- 🌿 **Safe Git Automation**
  - Branch creation & reuse
  - Forced or idempotent commits
  - Push protection handling
  - PR lifecycle management

- 🔁 **Multiple File Support**  
  Can refactor multiple files in a single run.

- 🚫 **PR Spam Prevention**  
  Updates existing PRs instead of creating duplicates.

---

## 🏗️ Architecture

```text
gemini-code-refactor-agent/
│
├── agent/
│   ├── analyzer.py        # Detects code smells
│   ├── decision.py        # Decides whether to refactor
│   └── refactor.py        # Gemini-based refactoring
│
├── core/
│   └── repo_manager.py    # Git operations (clone, commit, push)
│
├── github_api/
│   └── pr_creator.py      # GitHub PR automation (PyGithub)
│
├── main.py                # Orchestrates the agent workflow
├── requirements.txt
├── .env.example           # Environment variable template
├── .gitignore
└── README.md
