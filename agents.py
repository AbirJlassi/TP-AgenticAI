# agents.py - Multi-Agent Data Science System
from crewai import Agent
from llama_llm import llama_llm
from tools import csv_reader_tool, data_stats_tool

# Agent 1: Project Planner
project_planner_agent = Agent(
    role="Data Science Project Planner",
    goal=(
        "Transform business description into structured work plan. "
        "Decompose analysis into logical steps: EDA, modeling, evaluation."
    ),
    backstory=(
        "Experienced project manager in data science. You structure complex "
        "analyses into clear, sequential steps with success criteria."
    ),
    llm=llama_llm,
    tools=[],
    verbose=True,
    max_iterations=3,
    max_token_limit=4000,
)

# Agent 2: Data Analyst
data_analyst_agent = Agent(
    role="Data Analyst",
    goal=(
        "Perform exploratory data analysis using tools to read and analyze CSV data. "
        "Produce structured textual insights on data quality, distributions, patterns."
    ),
    backstory=(
        "Skilled data scientist with expertise in statistical analysis and visualization. "
        "You uncover insights from raw data and explain them clearly."
    ),
    llm=llama_llm,
    tools=[csv_reader_tool, data_stats_tool],
    verbose=True,
    max_iterations=4,
    max_token_limit=5000,
)

# Agent 3: Modelling Agent
modelling_agent = Agent(
    role="Machine Learning Modelling Specialist",
    goal=(
        "Propose multiple baseline models with relevant metrics. "
        "Define evaluation strategy: accuracy, F1, RMSE, AUC based on task type."
    ),
    backstory=(
        "ML engineer experienced in selecting and tuning models. "
        "You understand trade-offs between model complexity and interpretability."
    ),
    llm=llama_llm,
    tools=[],
    verbose=True,
    max_iterations=3,
    max_token_limit=4500,
)

# Agent 4: Report Writer
report_writer_agent = Agent(
    role="Technical Report Writer",
    goal=(
        "Assemble all previous outputs into a cohesive technical report. "
        "Format as markdown/LaTeX with proper sections and narrative flow."
    ),
    backstory=(
        "Expert technical writer. You synthesize complex findings into clear, "
        "structured reports suitable for stakeholder presentation."
    ),
    llm=llama_llm,
    tools=[],
    verbose=True,
    max_iterations=2,
    max_token_limit=6000,
)