import pandas as pd
try:
    data = pd.read_csv("iris.csv")
    if data.isnull().values.any():
        print("Warning: Missing data detected. Filling with mean values.")
        data = data.fillna(data.mean(numeric_only=True))
except FileNotFoundError:
    print("Error: File not found. Please check the file path.")
except pd.errors.ParserError:
    print("Error: File parsing failed. Check file format.")
except Exception as e:
    print(f"Unexpected error: {e}")