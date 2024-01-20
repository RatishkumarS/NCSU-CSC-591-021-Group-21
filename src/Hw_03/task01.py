import pandas as pd
from tabulate import tabulate

def generate_ascii_table(csv_file_path):
    # Read CSV file into a pandas DataFrame
    df = pd.read_csv(csv_file_path)

    # Count the number of rows for each class
    total_rows=len(df)
    print("Total number of Rows in the dataset",total_rows)
    class_counts = df['class!'].value_counts().reset_index()
    class_counts.columns = ['Class', 'Number of Rows']
    class_counts['Class Percentage']=(class_counts['Number of Rows']/total_rows)*100

    # Generate and print ASCII table
    ascii_table = tabulate(class_counts, headers='keys', tablefmt='grid')
    print(ascii_table)
    return(ascii_table)

# Replace 'your_csv_file.csv' with the actual path to your CSV file
csv_file_path = '../Data/soybeans.csv'

# Generate ASCII table
generate_ascii_table(csv_file_path)