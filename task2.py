import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Employee_Cleaned.csv")

print(df.head())
print(df.shape)
print(df.columns)
print(df.info())
print(df.describe())
print("\nEducation Count:")
print(df["Education"].value_counts())

print("\nCity Count:")
print(df["City"].value_counts())

print("\nGender Count:")
print(df["Gender"].value_counts())

print("\nPayment Tier Count:")
print(df["PaymentTier"].value_counts())

print("\nLeave Count:")
print(df["LeaveOrNot"].value_counts())
plt.figure(figsize=(6,4))
df["Education"].value_counts().plot(kind="bar")

plt.title("Education Distribution")
plt.xlabel("Education")
plt.ylabel("Number of Employees")

plt.show()
plt.figure(figsize=(6,4))
df["City"].value_counts().plot(kind="bar")

plt.title("City Distribution")
plt.xlabel("City")
plt.ylabel("Number of Employees")

plt.show()
# Gender Distribution
df["Gender"].value_counts().plot(kind="bar")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Employees")
plt.show()
# Payment Tier Distribution
plt.figure(figsize=(6,4))
df["PaymentTier"].value_counts().plot(kind="bar")

plt.title("Payment Tier Distribution")
plt.xlabel("Payment Tier")
plt.ylabel("Number of Employees")
plt.show()
# Employee Leave Distribution
plt.figure(figsize=(6,4))
df["LeaveOrNot"].value_counts().plot(kind="bar")

plt.title("Employee Leave Distribution")
plt.xlabel("Leave Status (0 = No, 1 = Yes)")
plt.ylabel("Number of Employees")
plt.show()