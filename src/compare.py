import json
import os

def compare_metrics():
    metrics_file = 'metrics.json'
    
    if not os.path.exists(metrics_file):
        print("Error: metrics.json not found!")
        return

    with open(metrics_file, 'r') as f:
        current = json.load(f)


    print("## Training Results Summary")
    print(f"| Metric | Value |")
    print(f"| :--- | :--- |")
    print(f"| RMSE | {current.get('rmse', 'N/A')} |")
    print(f"| R² | {current.get('r2', 'N/A')} |")
    print(f"| Dataset Size | {current.get('dataset_size', 'N/A')} |")

if __name__ == "__main__":
    compare_metrics()