import pandas as pd
import matplotlib.pyplot as plt

# Load the sales data
df = pd.read_csv("sales_data.csv")

# Show the complete dataset
print("Sales Data:")
print(df)

# Show basic information
print("\nDataset Information:")
print(df.info())

# Show summary statistics
print("\nSummary Statistics:")