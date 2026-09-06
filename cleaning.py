import pandas as pd

# Load dataset
df = pd.read_csv("Employee.csv")

print("Original Shape:", df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

duplicates = df.duplicated().sum()
print("\nDuplicate Records:", duplicates)

# Remove duplicates
df = df.drop_duplicates()

print("\nShape After Removing Duplicates:", df.shape)

print("\nData Types:")
print(df.dtypes)

# Save cleaned dataset
df.to_csv("Employee_Cleaned.csv", index=False)

print("\nCleaning Completed Successfully!")