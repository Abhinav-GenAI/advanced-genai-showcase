# Project 04: Autonomous "DevOps" or "Coder" Agent

## Overview
An agent that doesn't just write code, but lives in the terminal. It can navigate directories, run build commands, inspect logs, and self-correct based on error messages.

## Key Features
- **Self-Correction**: Loops through (Write -> Test -> Error -> Fix) cycles.
- **Environment Aware**: Can execute `bash` or `powershell` commands.
- **Context Management**: Reads entire folder structures to understand project dependencies.

## Tech Stack
- **Agent Framework**: LangGraph (for complex loops)
- **LLM**: GPT-4o / Claude 3.5 Sonnet (Strong coding ability)
- **Runtime**: Local Docker/Sandbox environment
- **Tools**: `FileEditTool`, `TerminalTool`, `LinterTool`

## Key Challenges
- **Infinite Loops**: Preventing the agent from trying the same fix repeatedly.
- **Safety**: Ensuring commands don't harm the host system (Sandboxing).
