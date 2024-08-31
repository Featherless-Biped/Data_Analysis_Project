import pandas as pd
import numpy as np

# Load the election data
df_president = pd.read_csv('data/president_county_candidate.csv')

# Filter out the rows where the candidate did not win
df_winners = df_president[df_president['won'] == True]

# Select only the necessary columns: state, county, party, and total_votes
df_winners = df_winners[['state', 'county', 'party', 'total_votes']]

# Drop duplicates just in case (ensures one winner per county)
df_winners = df_winners.drop_duplicates(subset=['state', 'county'])

# Rename columns to be more descriptive
df_winners = df_winners.rename(columns={"party": "winning_party", "total_votes": "votes_for_winner"})

# Load the census data
df_census = pd.read_csv('data/acs2017_county_data.csv')

# Rename columns for consistency
df_census = df_census.rename(columns={"State": "state", "County": "county"})

# Find the majority race
race_columns = ['Hispanic', 'White', 'Black', 'Native', 'Asian', 'Pacific']
df_census['majority_race'] = df_census[race_columns].idxmax(axis=1)

# Aggregate the census data
vars_to_merge = [x for x in df_census.columns if x not in ['CountyId', 'state', 'county']]
df_census_agg = pd.DataFrame(df_census.groupby(['state', 'county'])[vars_to_merge].sum())

# Merge the election winners data with the census data
df_combined = pd.merge(df_winners, df_census_agg, on=['state', 'county'], how='left')

# Handle NaN values by dropping rows or filling them
df_combined = df_combined.dropna()  # Drop rows with any NaN values
# Alternatively, you could fill NaN values: df_combined.fillna(df_combined.mean(), inplace=True)

# Save the cleaned and combined data to a new CSV file
df_combined.to_csv('data/combined_winners_census_data.csv', index=False)

print("Data preparation and cleaning complete. The cleaned data of county winners, their votes, and census information is saved as 'combined_winners_census_data.csv'.")
