import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from config import MSDConfig

config = MSDConfig()
file_path = config.flattened_output_csv_path
df = pd.read_csv(file_path)

output_dir = 'eda_img/'
os.makedirs(output_dir, exist_ok=True)

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns

sns.set_theme(style="whitegrid")

for column in numeric_columns:
    print(f"Plot distribtion for {column}...")
    plt.figure(figsize=(8, 5))   
    sns.histplot(df[column].dropna(), kde=True, bins=30, color='skyblue')
    plt.title(f'Distribution of {column}', fontsize=14)
    plt.xlabel(column, fontsize=12)
    plt.ylabel('Frequency', fontsize=12)
    save_path = os.path.join(output_dir, f"{column}.png")
    plt.savefig(save_path, bbox_inches='tight', dpi=150)
    plt.close()

print(f"Finish plotting. {len(numeric_columns)} of distribution image in total saved under {output_dir}.")