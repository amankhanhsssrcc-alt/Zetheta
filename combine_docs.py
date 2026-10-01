import os

docs_dir = r"c:\Users\HP\OneDrive\Desktop\kothak bank\docs"
output_file = os.path.join(docs_dir, "Bayesian_Regime_Detection_Complete_Documentation.md")

files_to_combine = [
    "Main_Report.md",
    "Final_Presentation.md",
    "Demo_Script.md",
    "model_cards/ensemble_model_card.md",
    "phase14_final_project_audit.md",
    "phase13_final_document_audit.md",
    "phase13_documentation_audit.md",
    "phase12_reconciliation_summary.md",
    "phase12_reconciliation_audit.md",
    "python_r_difference_report.md"
]

with open(output_file, "w", encoding="utf-8") as outfile:
    outfile.write("# BAYESIAN REGIME DETECTION ENGINE - COMPLETE MASTER DOCUMENTATION\n\n")
    outfile.write("This document aggregates all major reports, presentations, and audits generated during the final phases of the project.\n\n")
    outfile.write("---\n\n")
    
    for filename in files_to_combine:
        filepath = os.path.join(docs_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, "r", encoding="utf-8") as infile:
                outfile.write(f"<!-- START OF {filename} -->\n")
                outfile.write(infile.read())
                outfile.write(f"\n\n<!-- END OF {filename} -->\n\n")
                outfile.write("---\n\n")
        else:
            outfile.write(f"<!-- File {filename} not found -->\n\n")

print(f"Combined documentation saved to {output_file}")
