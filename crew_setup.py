# crew_setup.py - Multi-Agent Data Science Crew
from crewai import Crew, Process, Task
from agents import (
    project_planner_agent,
    data_analyst_agent,
    modelling_agent,
    report_writer_agent,
)

# ============================================================================
# TASK 1: PROJECT PLANNING
# ============================================================================
planning_task = Task(
    description=(
        "Given business context: {business_context}\n"
        "Dataset path: {csv_path}\n\n"
        "Create a detailed project plan that:\n"
        "1. Summarizes the business problem and dataset scope\n"
        "2. Outlines EDA steps (data quality, distributions, patterns)\n"
        "3. Recommends modeling approaches (classification/regression/clustering)\n"
        "4. Defines success metrics and evaluation strategy\n"
        "5. Lists potential challenges and mitigation strategies"
    ),
    agent=project_planner_agent,
    expected_output=(
        "A structured project plan (5-7 paragraphs) with clear steps and milestones."
    ),
)

# ============================================================================
# TASK 2: EXPLORATORY DATA ANALYSIS
# ============================================================================
eda_task = Task(
    description=(
        "Based on the project plan from Task 1, perform exploratory data analysis:\n"
        "1. Use csv_reader tool to inspect the dataset structure and columns\n"
        "2. Use data_stats tool to compute statistics on numeric and categorical columns\n"
        "3. Identify data quality issues (missing values, outliers, imbalance)\n"
        "4. Detect patterns, correlations, and anomalies\n"
        "5. Provide actionable insights for modeling\n"
        "Dataset path: {csv_path}"
    ),
    agent=data_analyst_agent,
    expected_output=(
        "A comprehensive EDA report (4-6 paragraphs) with statistics, insights, "
        "and recommendations for data preprocessing and feature engineering."
    ),
    context=[planning_task],
)

# ============================================================================
# TASK 3: MODEL PROPOSAL & EVALUATION STRATEGY
# ============================================================================
modelling_task = Task(
    description=(
        "Based on the project plan and EDA findings, propose baseline models:\n"
        "1. Suggest 2-3 appropriate baseline models (e.g., Logistic Regression, "
        "Random Forest, Decision Tree based on task type)\n"
        "2. Define evaluation metrics:\n"
        "   - For classification: accuracy, precision, recall, F1-score, ROC-AUC\n"
        "   - For regression: MAE, RMSE, R²\n"
        "   - For clustering: silhouette score, inertia\n"
        "3. Outline validation strategy (train-test split, cross-validation)\n"
        "4. Discuss hyperparameter tuning approach\n"
        "5. Identify potential model improvements and ensemble approaches"
    ),
    agent=modelling_agent,
    expected_output=(
        "A model proposal document (3-5 paragraphs) detailing chosen models, "
        "metrics, validation strategy, and expected performance ranges."
    ),
    context=[planning_task, eda_task],
)

# ============================================================================
# TASK 4: TECHNICAL REPORT GENERATION
# ============================================================================
report_task = Task(
    description=(
        "Synthesize all previous work into a professional technical report:\n"
        "1. Introduction: business context and objectives from planning\n"
        "2. Data Exploration: key findings from EDA\n"
        "3. Modeling Strategy: proposed models and metrics from modeling task\n"
        "4. Evaluation Plan: validation approach and success criteria\n"
        "5. Discussion: limitations, next steps, and recommendations\n"
        "6. Conclusion: summary and key takeaways\n\n"
        "Format as markdown with proper section headers and clear structure."
    ),
    agent=report_writer_agent,
    expected_output=(
        "A complete technical report in markdown format (6-8 sections) ready for "
        "stakeholder presentation. Include brief executive summary at the top."
    ),
    context=[planning_task, eda_task, modelling_task],
)

# ============================================================================
# CREW SETUP
# ============================================================================
data_science_crew = Crew(
    agents=[
        project_planner_agent,
        data_analyst_agent,
        modelling_agent,
        report_writer_agent,
    ],
    tasks=[
        planning_task,
        eda_task,
        modelling_task,
        report_task,
    ],
    process=Process.sequential,
    verbose=True,
)