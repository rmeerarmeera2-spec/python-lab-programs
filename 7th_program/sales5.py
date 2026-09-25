import pandas as pd
import numpy as np
data = {
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Expense": [5000, 4500, 6000, 5500]
}
df = pd.DataFrame(data)
print(df)
print("Total Expense:", np.sum(df["Expense"]))
print("Average Expense:", np.mean(df["Expense"]))
print("Highest Expense:", np.max(df["Expense"]))