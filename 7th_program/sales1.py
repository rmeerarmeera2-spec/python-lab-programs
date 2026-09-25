import pandas as pd
import numpy as np
data = {
    "Product": ["Fridge", "Phone", "Tablet", "Laptop", "Ac"],
    "Sales": [50000, 30000, 20000, 45000, 35000]
}
df = pd.DataFrame(data)
print("Sales Data:")
print(df)
print("\nTotal Sales:", np.sum(df["Sales"]))
print("Average Sales:", np.mean(df["Sales"]))
print("Highest Sales:", np.max(df["Sales"]))
print("Lowest Sales:", np.min(df["Sales"]))