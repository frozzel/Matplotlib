import pandas as pd
import matplotlib.pyplot as plt


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

print(df.groupby('TAG').sum())  # Group by 'TAG' and count the number of posts for each tag

print(df.groupby("TAG").count())  # Count the number of posts for each tag

df.DATE  = pd.to_datetime(df.DATE)  # Convert 'DATE' column to datetime format
print(df.DATE)  # Print the earliest date in the 'DATE' column

reshaped_df = df.pivot(index='DATE', columns='TAG', values='POSTS')  # Reshape the DataFrame
print(reshaped_df.head())  # Display the first few rows of the reshaped Data

reshaped_df.count()  # Count the number of non-null entries in each column of the reshaped DataFrame
print(reshaped_df.shape)  # Print the dimensions of the reshaped DataFrame

reshaped_df.fillna(0, inplace=True) 
print(reshaped_df.fillna(0))  # Display the first few rows after filling NaN values with 0

print(reshaped_df.isna().values.any())  # Check if there are any NaN values in the reshaped DataFrame

print(plt.plot(reshaped_df.index, reshaped_df.java))  # Plot the reshaped DataFrame
plt.figure(figsize=(16,10)) # make chart larger
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.xlabel('Date', fontsize=14)
plt.ylabel('Number of Posts', fontsize=14)
plt.ylim(0, 35000)
 
plt.plot(reshaped_df.index, reshaped_df.java)
plt.plot(reshaped_df.index, reshaped_df.python) # Tadah!

for column in reshaped_df.columns:
    plt.plot(reshaped_df.index, reshaped_df[column], 
             linewidth=3, label=reshaped_df[column].name)
 
plt.legend(fontsize=16) 

plt.show()  # Show the plot
