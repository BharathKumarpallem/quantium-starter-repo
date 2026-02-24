import pandas as pd
import glob

# read all csv files
files = glob.glob("data/*.csv")

cleaned_data = []

for file in files:
    df = pd.read_csv(file)

    # KEEP ONLY pink morsel
    df = df[df["product"] == "pink morsel"]

    cleaned_data.append(df)

# combine filtered data
final_df = pd.concat(cleaned_data)

# save cleaned file
final_df.to_csv("pink_morsels_only.csv", index=False)

print("Pink morsels extracted successfully ✅")