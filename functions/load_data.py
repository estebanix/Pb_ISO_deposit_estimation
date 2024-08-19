import pandas as pd

def load_data(file_path, global_vars):
    df = pd.read_csv(file_path)
    
    # Get unique values from the 'Deposit' column
    unique_values = df['Deposit'].unique()
    
    # Create DataFrames based on unique values in 'Deposit'
    for i, value in enumerate(unique_values):
        global_vars[f'df_{value}'] = df[df['Deposit'] == value]
    
    return unique_values
