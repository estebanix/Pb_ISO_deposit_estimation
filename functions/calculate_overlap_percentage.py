import numpy as np
from scipy.stats import gaussian_kde

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