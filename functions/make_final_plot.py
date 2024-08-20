import matplotlib.pyplot as plt
import numpy as np

def make_final_plot(comparison_results):
    
    # Define prior probabilities (example: uniform prior if no prior knowledge)
    def get_prior_probabilities(countries):
        num_countries = len(countries)
        return {country: 1/num_countries for country in countries}

    def extract_ratios(data):
        countries = set([country for ratio_list in data.values() for country, _ in ratio_list])
        country_ratios = {country: [] for country in countries}

        for ratio_type, ratio_list in data.items():
            for country, ratio in ratio_list:
                country_ratios[country].append(ratio / 100) 
        
        return country_ratios

    def calculate_likelihood(match_ratios):
        return np.exp(-np.sum((1 - np.array(match_ratios))**2))

    def calculate_probabilities(data):
        country_ratios = extract_ratios(data)
        
        # Get prior probabilities
        prior_probabilities = get_prior_probabilities(country_ratios.keys())
        
        # Calculate likelihoods
        likelihoods = {country: calculate_likelihood(ratios) for country, ratios in country_ratios.items()}
        
        # Calculate posteriors by multiplying likelihoods by priors
        posteriors = {country: likelihoods[country] * prior_probabilities[country] for country in likelihoods}
        
        # Normalize the posteriors to sum to 1
        total_posterior = sum(posteriors.values())
        probabilities = {country: posterior / total_posterior for country, posterior in posteriors.items()}
        
        return probabilities

    # Calculate posterior probabilities
    probabilities = calculate_probabilities(comparison_results)

    # Visualization
    cmap = plt.get_cmap('RdYlGn')
    norm = plt.Normalize(vmin=min(probabilities.values()), vmax=max(probabilities.values()))

    fig, ax = plt.subplots(figsize=(8, 5.4))

    colors = [cmap(norm(value)) for value in probabilities.values()]
    bars = ax.bar(probabilities.keys(), probabilities.values(), color=colors)

    ax.set_xlabel("Country")
    ax.set_ylabel("Posterior Probability")
    ax.set_title("Posterior Probabilities of Country of Origin")

    ax.set_xticklabels(probabilities.keys(), rotation=45, ha='right')

    ax.grid(axis='y', linestyle='--', alpha=0.7)

    plt.tight_layout()
    plt.show()
