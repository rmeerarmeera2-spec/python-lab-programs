import matplotlib.pyplot as plt
days = ["Mon", "Tue", "Wed", "Thu", "Fri"]
temperature = [30, 32, 31, 34, 33]
plt.plot(days, temperature, marker="o")
plt.title("Weekly Temperature")
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.savefig("temperature.png")
print("Temperature chart created successfully!")