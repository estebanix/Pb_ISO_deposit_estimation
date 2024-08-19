#from functions.calculate_overlap_percentage import calculate_overlap_percentage as cop
from functions.load_data import load_data

def run_model(your_data_file, comparison_data_file):
    your_data_dfs = load_data(your_data_file, globals())
    comparison_data_dfs = load_data(comparison_data_file, globals())
    
    return your_data_dfs, comparison_data_dfs  