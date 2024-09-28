import pandas as pd

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)

# Read the persona.csv file and display general information about the dataset.
df = pd.read_csv("persona.csv")
df.info
df.shape

# Display the number of unique SOURCE values and their frequencies.
df["SOURCE"].nunique()
df["SOURCE"].value_counts()

# Display the number of unique PRICE values.
df["PRICE"].nunique()

# Display the sales count for each PRICE value.
df["PRICE"].value_counts()

# Display the sales count for each country.
df["COUNTRY"].value_counts()

# Display the total revenue from sales by country.
# agg function accepts a dictionary and apply certain functions to the indicated variable.
df.groupby("COUNTRY").agg({"PRICE": "sum"})

# Display the sales counts by SOURCE types.
df["SOURCE"].value_counts()

# Display the average PRICE values by country.
df.groupby("COUNTRY").agg({"PRICE": "mean"})

# Display the average PRICE values by SOURCE.
df.groupby("SOURCE").agg({"PRICE": "mean"})

# Display the average PRICE values by COUNTRY-SOURCE breakdown.
df.groupby(["COUNTRY", "SOURCE"]).agg({"PRICE": "mean"})

# Display the average earnings by COUNTRY, SOURCE, SEX, and AGE breakdown.
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})

# Sort the output by PRICE in descending order and save it as agg_df.
df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False)

# Convert the names in the index to variable names.
agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values("PRICE", ascending=False).reset_index()

# Convert the AGE variable into a categorical variable and add it to agg_df.
bins = [0, 18, 23, 30, 40, agg_df["AGE"].max()]
names = ['0_18', '19_23', '24_30', '31_40', '40+']
agg_df["AGE_CAT"] = pd.cut(agg_df["AGE"], bins, labels=names)

agg_df.head()

# Define new level-based customers (persona) and add them as a variable to the dataset.
agg_df["customers_level_based"] = [row[0].upper() + "_" + row[1].upper() + "_" + row[2].upper() + "_" + row[5].upper() for row in agg_df.values]
# Grouping by the new "customers_level_based" variable, we are able the get an average amount of the specific customers persona
# since its values are unique.
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"}).reset_index()
agg_df.head()

# Segment the new customers into 4 segments based on PRICE and add the segments as a variable.
# since qcuts ranks the data from the lowest to the highest, we use labels in the order ["D", "C", "B", "A"]
agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])

# Classify the new customers and predict how much revenue they can generate.
# For example, check which segment a 33-year-old Turkish woman using ANDROID belongs to and the expected average revenue.
new_user = "TUR_ANDROID_FEMALE_31_40"
agg_df[agg_df["customers_level_based"] == new_user]

agg_df.head(20)
