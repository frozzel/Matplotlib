import pandas as pd

def load_data(file_path):
    """
    Load data from a CSV file into a pandas DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: DataFrame containing the loaded data.
    """
    try:
        data = pd.read_csv(file_path, names=['DATE', 'TAG', 'POSTS'], header=0)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None
    
df = load_data("QueryResults.csv")

print(df.head())  # Display the first few rows of the DataFrame

print(df.tail())  # Display the last few rows of the DataFrame

print(f"DataFrame dimensions: {df.shape}")  # Print the dimensions of the DataFrame
print(f"Number of rows: {df.shape[0]}, Number of columns: {df.shape[1]}")  # Print number of rows and columns

print(df.count())  # Count the number of non-null entries in each column

