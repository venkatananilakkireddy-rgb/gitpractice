import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [1000, 1500, 1200, 1800, 2000]
}

df = pd.DataFrame(data)

print(df)

print("\nTotal Sales =", df["Sales"].sum())
print("Average Sales =", df["Sales"].mean())

plt.plot(df["Month"], df["Sales"])
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()