import pandas as pd
import numpy as np
data = {
    "Name": ["Arun", "Priya", "Ravi", "Meena"],
    "Salary": [25000, 30000, 28000, 35000]
}
df = pd.DataFrame(data)
print(df)
print("Average Salary:", np.mean(df["Salary"]))
print("Maximum Salary:", np.max(df["Salary"]))
print("Minimum Salary:", np.min(df["Salary"]))