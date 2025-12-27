# tools.py - Data Science Tools
import os
import csv
import json
from typing import Type, Any
from pathlib import Path
from pydantic import BaseModel, Field
from crewai.tools import BaseTool
from settings import SERPER_API_KEY

os.environ["SERPER_API_KEY"] = SERPER_API_KEY

# ============================================================================
# CSV READER TOOL
# ============================================================================

class CSVReaderInput(BaseModel):
    csv_path: str = Field(..., description="Path to the CSV file to read.")
    num_rows: int = Field(default=5, description="Number of rows to display (default: 5).")

class CSVReaderTool(BaseTool):
    name: str = "csv_reader"
    description: str = (
        "Read and display basic info about a CSV file: column names, data types, "
        "and first N rows. Use this to understand data structure."
    )
    args_schema: Type[BaseModel] = CSVReaderInput

    def _run(self, csv_path: str, num_rows: int = 5) -> str:
        """Read CSV file and return column info + sample rows."""
        try:
            path = Path(csv_path)
            if not path.exists():
                return f"Error: File {csv_path} does not exist."
            
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                if reader.fieldnames is None:
                    return "Error: CSV file is empty or malformed."
                
                columns = reader.fieldnames
                rows = []
                for i, row in enumerate(reader):
                    if i >= num_rows:
                        break
                    rows.append(row)
            
            result = f"CSV File: {csv_path}\n"
            result += f"Columns: {', '.join(columns)}\n"
            result += f"Number of columns: {len(columns)}\n\n"
            result += f"First {num_rows} rows:\n"
            result += json.dumps(rows, indent=2, ensure_ascii=False)
            return result
        except Exception as e:
            return f"Error reading CSV: {str(e)}"

# ============================================================================
# DATA STATS TOOL
# ============================================================================

class DataStatsInput(BaseModel):
    csv_path: str = Field(..., description="Path to the CSV file.")
    columns: str = Field(
        default="all",
        description="Comma-separated list of columns to analyze, or 'all' for all columns."
    )

class DataStatsTool(BaseTool):
    name: str = "data_stats"
    description: str = (
        "Calculate basic statistics on CSV columns: count, missing values, "
        "unique values, numeric stats (mean, min, max), and cardinality for categoricals."
    )
    args_schema: Type[BaseModel] = DataStatsInput

    def _run(self, csv_path: str, columns: str = "all") -> str:
        """Calculate statistics for CSV columns."""
        try:
            path = Path(csv_path)
            if not path.exists():
                return f"Error: File {csv_path} does not exist."
            
            # Read all data
            data = []
            column_names = []
            with open(path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                column_names = reader.fieldnames
                for row in reader:
                    data.append(row)
            
            if not data:
                return "Error: CSV file is empty."
            
            # Determine which columns to analyze
            if columns == "all":
                cols_to_analyze = column_names
            else:
                cols_to_analyze = [c.strip() for c in columns.split(',')]
            
            stats = {}
            total_rows = len(data)
            
            for col in cols_to_analyze:
                if col not in column_names:
                    continue
                
                values = [row[col] for row in data if row[col] is not None]
                missing = total_rows - len(values)
                unique_count = len(set(values))
                
                col_stats = {
                    "column": col,
                    "total_rows": total_rows,
                    "missing_count": missing,
                    "missing_percent": round((missing / total_rows) * 100, 2),
                    "unique_values": unique_count,
                }
                
                # Try numeric stats
                try:
                    numeric_values = [float(v) for v in values if v]
                    if numeric_values:
                        col_stats["type"] = "numeric"
                        col_stats["mean"] = round(sum(numeric_values) / len(numeric_values), 4)
                        col_stats["min"] = round(min(numeric_values), 4)
                        col_stats["max"] = round(max(numeric_values), 4)
                except:
                    col_stats["type"] = "categorical"
                    # Show top categories
                    from collections import Counter
                    counts = Counter(values)
                    col_stats["top_categories"] = dict(counts.most_common(5))
                
                stats[col] = col_stats
            
            return json.dumps(stats, indent=2, ensure_ascii=False)
        except Exception as e:
            return f"Error calculating stats: {str(e)}"

# ============================================================================
# INSTANTIATE TOOLS
# ============================================================================

csv_reader_tool = CSVReaderTool()
data_stats_tool = DataStatsTool()