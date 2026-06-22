import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("train.csv")

# Gender Distribution
gender = df["Sex"].value_counts()

plt.bar(gender.index, gender.values)
plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Count")
plt.savefig("gender_distribution.png")
plt.show()

# Age Distribution
plt.hist(df["Age"].dropna(), bins=10)
plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.savefig("age_distribution.png")
plt.show()