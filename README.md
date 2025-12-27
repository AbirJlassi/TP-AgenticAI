# Multi‑Agent Data Science Crew

AgenticAI is a small multi-agent data science project that coordinates specialized agents (planner, data analyst, modelling specialist, report writer) to analyze CSV datasets and produce a structured technical report.

**Key Features**
- Multi-agent orchestration using `crewai` agents and crew
- Simple data tools: CSV reader and basic column statistics
- Pluggable LLM backend via Hugging Face (configured in `settings.py` / `llama_llm.py`)

**Repository Structure**
- `main.py` — example runner that kicks off the crew
- `crew_setup.py` — defines agents, tasks, and the crew process
- `agents.py` — agent definitions and configurations
- `tools.py` — `csv_reader` and `data_stats` tools (Pydantic inputs)
- `llama_llm.py` — LLM wrapper configuration
- `settings.py` — loads environment variables (Hugging Face & Serper keys)
- `data/` — example CSV files (e.g., `Iris.csv`)

**Requirements**
The project depends on a few third-party packages.:

```
crewai
pydantic
python-dotenv
```

See `requirements.txt` for an exact list.

**Environment variables**
Create a `.env` file (or set environment variables) with the following keys:

- `HUGGINGFACE_API_KEY` — your Hugging Face API token
- `HF_MODEL` — optional model identifier (default set in `settings.py`)
- `SERPER_API_KEY` — Serper (search) API key used by some tools


**Setup (Windows PowerShell)**

```powershell
# Create and activate a virtual environment (if needed)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
pip install -r requirements.txt
```

**Run**

```powershell
python main.py
```

By default `main.py` expects a CSV path at `data/iris.csv` — update `csv_path` in `main.py` or pass your own dataset.

**Configuration Notes**
- `settings.py` uses `python-dotenv` to load a `.env` file. It raises a `RuntimeError` if required keys are missing.
- `llama_llm.py` creates an `LLM` instance using `HUGGINGFACE_API_KEY` and `HF_MODEL` — change these to switch models or providers.
- Tools are implemented as subclasses of `crewai.tools.BaseTool` in `tools.py`.

**Next steps / Tips**
- To add custom tools, follow the `CSVReaderTool` and `DataStatsTool` patterns in `tools.py`.

**License**
This repository contains example code; add a license file if you plan to publish.
