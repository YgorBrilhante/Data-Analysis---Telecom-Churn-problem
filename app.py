import pandas as pd
import plotly.express as px

table = pd.read_csv("telecom_users.csv")

table = table.drop("Unnamed: 0", axis=1)
print(table)


table["TotalSpend"] = pd.to_numeric(table["TotalSpend"], errors="coerce")


table = table.dropna(how="all", axis=1)

table = table.dropna(how="any", axis=0)

print(table.info())


print(table["Churn"].value_counts())
print(table["Churn"].value_counts(normalize=True).map("{:.1%}".format))

for column in table.columns:
    chart = px.histogram(table, x=column, color="Churn")
    chart.show()