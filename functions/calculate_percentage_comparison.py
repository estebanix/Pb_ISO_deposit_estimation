import pandas as pd
from functions.calculate_overlap_percentage import calculate_overlap_percentage as cop

def calculate_percentage_comparison(your_data, tabs, isotope_column):
    results = []
    for sheet in tabs:
        df_name = f"df_{sheet}" 
        df = globals()[df_name]
        
        your_data_clean = pd.to_numeric(your_data[isotope_column], errors='coerce').dropna()
        df_clean = pd.to_numeric(df[isotope_column], errors='coerce').dropna()
        
        # Calculate the overlap percentage
        overlap_percentage = cop(your_data_clean, df_clean)
        results.append((sheet, overlap_percentage))
    
    return results