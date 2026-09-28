import matplotlib.pyplot as plt

# -------------------------
# KCL Simulation
# -------------------------

entering = [2, 3, 4]
leaving = [4, 5]

total_entering = sum(entering)
total_leaving = sum(leaving)

plt.figure()

plt.bar(
    ["Entering Current", "Leaving Current"],
    [total_entering, total_leaving]
)

plt.title("Kirchhoff's Current Law (KCL)")
plt.ylabel("Current (A)")

plt.show()


# -------------------------
# KVL Simulation
# -------------------------

voltage_source = 12
voltage_drops = [2, 4, 6]

total_drop = sum(voltage_drops)

plt.figure()

plt.bar(
    ["Source Voltage", "Voltage Drops"],
    [voltage_source, total_drop]
)

plt.title("Kirchhoff's Voltage Law (KVL)")
plt.ylabel("Voltage (V)")

plt.show()