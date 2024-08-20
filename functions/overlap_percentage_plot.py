import numpy as np
import matplotlib.pyplot as plt

def overlap_percentage_plot(comparison_results, isotope_ratios):
    countries = [result[0] for result in comparison_results[isotope_ratios[0]]] 
    values_by_isotope = {isotope: [result[1] for result in comparison_results[isotope]] for isotope in isotope_ratios}

    x = np.arange(len(countries)) 
    width = 0.2 

    fig, ax = plt.subplots(figsize=(12, 6))

    for i, isotope in enumerate(isotope_ratios):
        bars = ax.bar(x + i * width, values_by_isotope[isotope], width, label=isotope)
        
        for bar in bars:
            height = bar.get_height()
            ax.annotate(f'{height:.1f}%',
                        xy=(bar.get_x() + bar.get_width() / 2, height), 
                        xytext=(0, 3), 
                        textcoords="offset points",
                        ha='center', va='bottom')

    ax.set_xlabel('Countries')
    ax.set_ylabel('Overlap Percentage')
    ax.set_title('Comparison of Overlap Percentages by Isotope and Country')
    ax.set_xticks(x + width)
    ax.set_xticklabels(countries, rotation=45, ha='right')
    ax.legend()

    plt.tight_layout()
    plt.show()