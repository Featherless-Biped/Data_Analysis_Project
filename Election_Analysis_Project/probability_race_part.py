import pandas as pd
import os

# Load the combined dataset
df_combined = pd.read_csv('data/combined_winners_census_data.csv')

# Ensure the output directory exists
output_dir = 'output'
os.makedirs(output_dir, exist_ok=True)

# Function to calculate the probability for each race voting for each party
def calculate_probabilities(df, race_column='majority_race', party_column='winning_party'):
    # Get the total number of counties for each majority race
    race_counts = df[race_column].value_counts()

    # Calculate the number of counties for each race that voted for REP and DEM
    race_party_counts = df.groupby([race_column, party_column]).size().unstack(fill_value=0)

    # Calculate the probabilities
    probabilities = race_party_counts.div(race_counts, axis=0)

    return probabilities

# Calculate the probabilities
probabilities = calculate_probabilities(df_combined)

# Save the probabilities to a CSV file in the output directory
output_file = os.path.join(output_dir, 'race_voting_probabilities.csv')
probabilities.to_csv(output_file)

print(f"Probabilities saved to {output_file}")
