import pandas as pd
import numpy as np
data = {
    "Name": ["Meera", "Aadhira", "Mithran", "Mathi"],
    "Mark": [85, 90, 78, 95]
}
df = pd.DataFrame(data)
print(df)
print("Total:", np.sum(df["Mark"]))
print("Average:", np.mean(df["Mark"]))
print("Highest:", np.max(df["Mark"]))
print("Lowest:", np.min(df["Mark"]))