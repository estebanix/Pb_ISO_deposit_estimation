import pandas as pd
import numpy as np
from scipy.stats import gaussian_kde

def run_model():
    
    def load_data(file_path):
        df = pd.read_csv(file_path)
        
        # Get unique values from the 'Deposit' column
        unique_values = df['Deposit'].unique()
        
        # Create a dictionary to store DataFrames based on unique values in 'Deposit'
        data_frames = {value: df[df['Deposit'] == value] for value in unique_values}
        
        return unique_values, data_frames

    # Load data and get the unique deposits
    tabs, tab_data = load_data("data/comparison_synthetic_data.csv")
    oppida, oppida_data = load_data("data/your_synthetic_data.csv")

    def calculate_overlap_percentage(data1, data2, bw="silverman"):
        data1 = data1.dropna()
        data2 = data2.dropna()
        
        kde1 = gaussian_kde(data1, bw_method=bw)
        kde2 = gaussian_kde(data2, bw_method=bw)

        common_grid = np.linspace(
            min(min(data1), min(data2)), max(max(data1), max(data2)), 1000)

        density1_interp = kde1.evaluate(common_grid)
        density2_interp = kde2.evaluate(common_grid)
        
        overlap_area = np.trapz(np.minimum(density1_interp, density2_interp), common_grid)
        
        total_area1 = np.trapz(density1_interp, common_grid)
        total_area2 = np.trapz(density2_interp, common_grid)
        
        overlap_percentage = (2 * overlap_area) / (total_area1 + total_area2) * 100
        
        return overlap_percentage
    
    def calculate_percentage_comparison(your_data, tabs, isotope_column):
        results = []
        for sheet in tabs:
            df = tab_data[sheet]  # Access the correct DataFrame from the dictionary
            
            your_data_clean = pd.to_numeric(your_data[isotope_column], errors='coerce').dropna()
            df_clean = pd.to_numeric(df[isotope_column], errors='coerce').dropna()
            
            # Calculate the overlap percentage
            overlap_percentage = calculate_overlap_percentage(your_data_clean, df_clean)
            results.append((sheet, overlap_percentage))
        
        return results
    
    def get_comparison_results(isotope_ratios):
        comparison_data = {isotope: calculate_percentage_comparison(oppida_data[oppida[0]], tabs, isotope) for isotope in isotope_ratios}
        return comparison_data
    
    isotope_ratios = ["208Pb/204Pb", "207Pb/204Pb", "206Pb/204Pb"]

    comparison_results = get_comparison_results(isotope_ratios)
    return comparison_results
