import pandas as pd
import os

# Define the path to the data folder
data_folder = "data"

# Load all CSV files into a list of dataframes
csv_files = [f for f in os.listdir(data_folder) if f.endswith(".csv")]
dataframes = [pd.read_csv(os.path.join(data_folder, f)) for f in csv_files]

# Combine them into a single dataframe
combined_df = pd.concat(dataframes)

# Filter for only "Pink Morsel"
pink_df = combined_df[combined_df["product"] == "pink morsel"]

# Clean the price column (remove $ and convert to float)
pink_df["price"] = pink_df["price"].replace('[\$,]', '', regex=True).astype(float)

# Create a new 'sales' column = price * quantity (numeric)
pink_df.loc[:, "sales"] = pink_df["price"] * pink_df["quantity"]


# Keep only the required columns
final_df = pink_df[["sales", "date", "region"]]

# Save the formatted output
output_path = os.path.join("data", "formatted_output.csv")
final_df.to_csv(output_path, index=False)

print(f"✅ File saved to {output_path}")
print(final_df.head())
