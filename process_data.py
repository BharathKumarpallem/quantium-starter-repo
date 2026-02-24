import pandas as pd
import glob

# read all csv files from data folder
files = glob.glob("data/*.csv")

dataframes = []

for file in files:
    df = pd.read_csv(file)

    # keep only pink morsel
    df = df[df["product"] == "pink morsel"]

    # calculate sales
    df["Sales"] = df["quantity"] * df["price"]

    # keep required columns
    df = df[["Sales", "date", "region"]]

    dataframes.append(df)

# combine all datasets
final_df = pd.concat(dataframes)

# save output
final_df.to_csv("formatted_sales.csv", index=False)

print("Data processing completed ✅")