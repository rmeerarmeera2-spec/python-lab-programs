import pandas as pd
import numpy as np
data = {
    "Name": ["Anu", "Bala", "Chandru", "Dharani"],
    "Attendance": [85, 90, 75, 95]
}
df = pd.DataFrame(data)
print(df)
print("Average:", np.mean(df["Attendance"]))
print("Highest:", np.max(df["Attendance"]))
print("Lowest:", np.min(df["Attendance"]))