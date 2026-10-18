import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/iris.csv")

setosa = df[df["variety"] == "Setosa"]
versicolor = df[df["variety"] == "Versicolor"]
virginica = df[df["variety"] == "Virginica"]

for species, color in [
    ("Setosa", "blue"),
    ("Versicolor", "red"),
    ("Virginica", "green")
]:
    subset = df[df["variety"] == species]
    plt.scatter(
        subset["petal.length"],
        subset["petal.width"],
        color=color,
        label=species
    )
plt.title("Petal Length vs Petal Width")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
plt.legend()

plt.show()