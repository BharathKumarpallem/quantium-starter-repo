import pandas as pd
df = pd.read_csv("formatted_sales.csv")
print(df.head())
files = glob.glob("data/*.csv")

all_data = []

for file in files:
    df = pd.read_csv(file)

    # keep pink morsel only
    df = df[df["product"] == "pink morsel"]

    # ✅ REMOVE $
    df["price"] = df["price"].replace('[\$,]', '', regex=True).astype(float)

    # calculate numeric sales
    df["Sales"] = df["quantity"] * df["price"]

    all_data.append(df[["Sales", "date", "region"]])

combined = pd.concat(all_data)

# daily totals
daily_sales = (
    combined.groupby(["date", "region"], as_index=False)["Sales"]
    .sum()
)

daily_sales.to_csv("formatted_sales.csv", index=False)

print("✅ Correct formatted data created")