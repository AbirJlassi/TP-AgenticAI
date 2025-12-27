from pathlib import Path
from crew_setup import data_science_crew

def main() -> None:
    # Example: Business context and CSV path
    business_context = (
        "We need to analyze the morphological measurements of Iris flowers "
        "(sepal length, sepal width, petal length, petal width) to classify each sample "
        "into species (setosa, versicolor, virginica). The goal is to identify which "
        "measurements best distinguish species and to build a reliable model to predict "
        "species from these measurements, helping botanists and educators demonstrate "
        "pattern differences across species and support downstream classification tasks."
    )
    csv_path = "data/Iris.csv" 

    
    print("=" * 70)
    print("MULTI-AGENT DATA SCIENCE ANALYSIS")
    print("=" * 70)
    print(f"Business Context: {business_context[:100]}...")
    print(f"CSV Path: {csv_path}")
    print("=" * 70)
    print()
    
    # Run the crew with the provided inputs
    result = data_science_crew.kickoff(
        inputs={
            "business_context": business_context,
            "csv_path": csv_path,
        }
    )
    
    # Save report to markdown file
    output_path = Path("report_final.md")
    output_path.write_text(str(result), encoding="utf-8")
    print("\n" + "=" * 70)
    print(f"✓ Report saved to {output_path.name}")
    print("=" * 70)

if __name__ == "__main__":
    main()