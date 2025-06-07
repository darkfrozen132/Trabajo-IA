import kagglehub
import os
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("edumagalhaes/quality-prediction-in-a-mining-process")

print("Path to dataset files:", path)

# Split the dataset into two parts of approximately 80 MB each
dataset_file = os.path.join(path, "MiningProcess_Flotation_Plant_Database.csv")
output_dir = os.path.dirname(dataset_file)

# Check if the dataset file exists
if not os.path.exists(dataset_file):
    raise FileNotFoundError(f"The dataset file '{dataset_file}' does not exist.")

try:
    # Load the dataset
    df = pd.read_csv(dataset_file)
except Exception as e:
    raise ValueError(f"Error loading the dataset: {e}")

# Calculate approximate row split based on file size
total_rows = len(df)
split_index = total_rows // 2

# Save the first part
part1_path = os.path.join(output_dir, "MiningProcess_Flotation_Plant_Database_Part1.csv")
df.iloc[:split_index].to_csv(part1_path, index=False)

# Save the second part
part2_path = os.path.join(output_dir, "MiningProcess_Flotation_Plant_Database_Part2.csv")
df.iloc[split_index:].to_csv(part2_path, index=False)

print(f"Dataset split into:\n{part1_path}\n{part2_path}")