import numpy as np

def country_ratios(comparison_results):
    country_ratios = {}

# Extract and organize data
    for ratio, entries in comparison_results.items():
        for country, value in entries:
            if country not in country_ratios:
                country_ratios[country] = [None, None, None]
            
            # Determine index for the ratio
            if ratio == '208Pb/204Pb':
                country_ratios[country][0] = value
            elif ratio == '207Pb/204Pb':
                country_ratios[country][1] = value
            elif ratio == '206Pb/204Pb':
                country_ratios[country][2] = value

    # Print the arrays for each country
    for country, ratios in country_ratios.items():  
            mean = np.mean(ratios)
            
            print(f"{country}: {mean:.2f}%")