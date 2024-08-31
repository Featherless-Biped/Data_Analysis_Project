import os
import pandas as pd
import numpy as np
from scipy import stats
from statsmodels.stats.proportion import proportions_ztest
from sklearn.preprocessing import LabelEncoder
import matplotlib.pyplot as plt
import seaborn as sns

# Create the output directory if it doesn't exist
output_dir = "output"
os.makedirs(output_dir, exist_ok=True)

# Load the cleaned data
df_combined = pd.read_csv('data/combined_winners_census_data.csv')

# Ensure that we have no NaN values in relevant columns
df_combined = df_combined.dropna(subset=['majority_race', 'winning_party'])

# Encode race and party for easier analysis
label_encoder = LabelEncoder()
df_combined['majority_race_encoded'] = label_encoder.fit_transform(df_combined['majority_race'])
df_combined['winning_party_encoded'] = label_encoder.fit_transform(df_combined['winning_party'])

# 1. Proportion Test: Likelihood of a county voting REP based on the majority race being White
df_combined['is_white_majority'] = df_combined['majority_race'] == 'White'
white_majority_rep = df_combined[(df_combined['is_white_majority']) & (df_combined['winning_party_encoded'] == 1)].shape[0]
total_white_majority = df_combined[df_combined['is_white_majority']].shape[0]

stat, p_value_prop = proportions_ztest(white_majority_rep, total_white_majority, value=0.5)
with open(os.path.join(output_dir, 'proportion_test_output.txt'), 'w') as f:
    f.write(f"Z-statistic: {stat}\n")
    f.write(f"P-value for Proportion Test: {p_value_prop}\n")

# 2. Chi-Square Test: Is there a significant association between race and voting pattern?
contingency_table = pd.crosstab(df_combined['majority_race'], df_combined['winning_party'])
chi2_stat, p_val, dof, ex = stats.chi2_contingency(contingency_table)
with open(os.path.join(output_dir, 'chi_square_test_output.txt'), 'w') as f:
    f.write(f"Chi-Square Statistic: {chi2_stat}\n")
    f.write(f"P-value for Chi-Square Test: {p_val}\n")

# 3. T-Test: Comparing the likelihood of voting REP between White-majority and Non-White-majority counties
white_majority = df_combined[df_combined['is_white_majority']]['winning_party_encoded']
non_white_majority = df_combined[~df_combined['is_white_majority']]['winning_party_encoded']

t_statistic, p_value = stats.ttest_ind(white_majority, non_white_majority, equal_var=False)
with open(os.path.join(output_dir, 't_test_output.txt'), 'w') as f:
    f.write(f"T-statistic for Equality of Means: {t_statistic}\n")
    f.write(f"P-value for Equality of Means: {p_value}\n")

# Visualization 1: Count of Winning Party by Majority Race
plt.figure()
sns.countplot(x='majority_race', hue='winning_party', data=df_combined)
plt.title('Count of Winning Party by Majority Race')
plt.xlabel('Majority Race')
plt.ylabel('Number of Counties')
plt.legend(title='Winning Party', loc='upper right', labels=['DEM', 'REP'])
plt.savefig(os.path.join(output_dir, 'count_by_race.png'))
plt.close()

# Visualization 2: Proportion of REP vs DEM for each Race
df_race_party = df_combined.groupby(['majority_race', 'winning_party']).size().unstack()
plt.figure()
df_race_party.plot(kind='bar', stacked=True)
plt.title('Proportion of REP vs DEM by Race')
plt.xlabel('Majority Race')
plt.ylabel('Number of Counties')
plt.savefig(os.path.join(output_dir, 'proportion_by_race.png'))
plt.close()

# Visualization 3: Pie Chart of Voting Outcomes in White-Majority Counties
df_white_majority = df_combined[df_combined['is_white_majority']]['winning_party'].value_counts()
plt.figure()
df_white_majority.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['blue', 'red'])
plt.title('Voting Outcomes in White-Majority Counties')
plt.ylabel('')
plt.savefig(os.path.join(output_dir, 'pie_chart_white_majority.png'))
plt.close()
