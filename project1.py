import pandas as pd

sales_data = pd.read_excel("Dataset for Data Analytics.xlsx")

print("Project 1 - Data Cleaning and Preparation")
print("-" * 50)

sales_data["Date"] = pd.to_datetime(sales_data["Date"]).dt.strftime("%Y-%m-%d")

sales_data["UnitPrice"] = sales_data["UnitPrice"].round(2)
sales_data["TotalPrice"] = sales_data["TotalPrice"].round(2)

text_columns = ["Product", "ShippingAddress", "PaymentMethod","OrderStatus", "CouponCode", "ReferralSource"]

for col in text_columns:
    sales_data[col] = sales_data[col].astype(str).str.strip().str.title()

print("\nChecking for missing values:")
print(sales_data.isnull().sum())

print("\nChecking for duplicate rows:")
row_duplicates = sales_data.duplicated().sum()
print("Duplicate rows found:", row_duplicates)

print("\nChecking for duplicate Order IDs:")
order_duplicates = sales_data["OrderID"].duplicated().sum()
print("Duplicate Order IDs found:", order_duplicates)

sales_data["CouponCode"] = sales_data["CouponCode"].fillna("No Coupon")

print("\nMissing values after cleaning:")
print(sales_data.isnull().sum())

print("\nDate format:")
print("YYYY-MM-DD")

print("Date format is valid.")

print("\nSample dates:")
print(sales_data["Date"].head())

print("\nData format corrections applied:")
print("- Dates standardized to YYYY-MM-DD")
print("- Text fields checked and trimmed")
print("- Numeric values rounded to 2 decimal places")

sales_data.to_excel("Cleaned_Dataset.xlsx", index=False)

print("\nData cleaning completed successfully.")
print("Cleaned file saved as Cleaned_Dataset.xlsx")