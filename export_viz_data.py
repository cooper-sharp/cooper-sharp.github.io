"""
Data Export Script for Gambling & Mental Health Visualization Dashboard
========================================================================
Run this script in the same directory as your combined-scoring.csv file.
It will create a 'viz_data' folder with all necessary JSON files.
"""

import pandas as pd
import numpy as np
import json
from pathlib import Path

# Create output directory
Path('viz_data').mkdir(exist_ok=True)

# Load data
print("Loading data...")
df = pd.read_csv('data/combined-scoring.csv')
print(f"✓ Loaded {len(df):,} participants")

df['demo_state'] = (
    pd.to_numeric(df['demo_state'], errors='coerce')
      .dropna()
      .astype(int)
      .astype(str)
)

# Normalize coded survey variables (fixes 1.0 → "1")
coded_cols = [
    'demo_state',
    'demo_sab',   # gender
    'demo_race',
    'ses_edu',
    'ses_thi',
    'ses_tpi'
]

for col in coded_cols:
    df[col] = (
        pd.to_numeric(df[col], errors='coerce')
          .astype('Int64')   # preserves NaN
          .astype(str)
    )


# ============================================
# 1. GEOGRAPHIC DATA (Choropleth)
# ============================================
print("\n[1/5] Exporting geographic data...")

state_counts = df['demo_state'].value_counts().to_dict()

# Sequential alphabetical codes (1-53) to state abbreviation
code_to_abbrev = {
    '1': 'AL', '2': 'AK', '3': 'AZ', '4': 'AR', '5': 'CA',
    '6': 'CO', '7': 'CT', '8': 'DE', '9': 'DC', '10': 'FL',
    '11': 'GA', '12': 'HI', '13': 'ID', '14': 'IL', '15': 'IN',
    '16': 'IA', '17': 'KS', '18': 'KY', '19': 'LA', '20': 'ME',
    '21': 'MD', '22': 'MA', '23': 'MI', '24': 'MN', '25': 'MS',
    '26': 'MO', '27': 'MT', '28': 'NE', '29': 'NV', '30': 'NH',
    '31': 'NJ', '32': 'NM', '33': 'NY', '34': 'NC', '35': 'ND',
    '36': 'OH', '37': 'OK', '38': 'OR', '39': 'PA', '40': 'PR',
    '41': 'RI', '42': 'SC', '43': 'SD', '44': 'TN', '45': 'TX',
    '46': 'UT', '47': 'VT', '48': 'VA', '49': 'WA', '50': 'WV',
    '51': 'WI', '52': 'WY', '53': 'INTL'
}

# Sequential alphabetical codes to state name
code_to_name = {
    '1': 'Alabama', '2': 'Alaska', '3': 'Arizona', '4': 'Arkansas', '5': 'California',
    '6': 'Colorado', '7': 'Connecticut', '8': 'Delaware', '9': 'District of Columbia', '10': 'Florida',
    '11': 'Georgia', '12': 'Hawaii', '13': 'Idaho', '14': 'Illinois', '15': 'Indiana',
    '16': 'Iowa', '17': 'Kansas', '18': 'Kentucky', '19': 'Louisiana', '20': 'Maine',
    '21': 'Maryland', '22': 'Massachusetts', '23': 'Michigan', '24': 'Minnesota', '25': 'Mississippi',
    '26': 'Missouri', '27': 'Montana', '28': 'Nebraska', '29': 'Nevada', '30': 'New Hampshire',
    '31': 'New Jersey', '32': 'New Mexico', '33': 'New York', '34': 'North Carolina', '35': 'North Dakota',
    '36': 'Ohio', '37': 'Oklahoma', '38': 'Oregon', '39': 'Pennsylvania', '40': 'Puerto Rico',
    '41': 'Rhode Island', '42': 'South Carolina', '43': 'South Dakota', '44': 'Tennessee', '45': 'Texas',
    '46': 'Utah', '47': 'Vermont', '48': 'Virginia', '49': 'Washington', '50': 'West Virginia',
    '51': 'Wisconsin', '52': 'Wyoming', '53': 'International'
}

geo_data = {
    'states': [],
    'counts': [],
    'state_names': []
}

for code, count in state_counts.items():
    code_str = str(code).strip()
    if code_str in code_to_abbrev:
        geo_data['states'].append(code_to_abbrev[code_str])
        geo_data['counts'].append(int(count))
        geo_data['state_names'].append(code_to_name.get(code_str, code_str))

geo_data['total'] = int(df['demo_state'].notna().sum())

with open('viz_data/geographic.json', 'w') as f:
    json.dump(geo_data, f, indent=2)
print(f"  ✓ {len(geo_data['states'])} states exported")

# ============================================
# 2. DEMOGRAPHICS DATA
# ============================================
print("\n[2/5] Exporting demographics data...")

demographics = {}

# Age distribution
df['demo_yrs'] = pd.to_numeric(df['demo_yrs'], errors='coerce')
demographics['age'] = {
    'values': df['demo_yrs'].dropna().tolist(),
    'mean': round(df['demo_yrs'].mean(), 1),
    'median': round(df['demo_yrs'].median(), 1),
    'min': int(df['demo_yrs'].min()),
    'max': int(df['demo_yrs'].max()),
    'n': int(df['demo_yrs'].notna().sum())
}

# Gender (demo_sab)
gender_map = {'1': 'Male', '2': 'Female', '3': 'Other', '4': 'Prefer not to say'}
gender_counts = df['demo_sab'].astype(str).map(gender_map).value_counts().to_dict()
demographics['gender'] = {
    'labels': list(gender_counts.keys()),
    'values': [int(v) for v in gender_counts.values()],
    'n': int(sum(gender_counts.values()))
}

# Race (demo_race)
race_map = {
    '1': 'American Indian/Alaska Native',
    '2': 'Asian',
    '3': 'Native Hawaiian/Pacific Islander',
    '4': 'Black/African American',
    '5': 'White',
    '6': 'Two or more/Other',
    '7': 'Prefer not to respond'
}
race_counts = df['demo_race'].astype(str).map(race_map).value_counts().to_dict()
# Remove any NaN entries
race_counts = {k: v for k, v in race_counts.items() if pd.notna(k) and k != 'nan'}
demographics['race'] = {
    'labels': list(race_counts.keys()),
    'values': [int(v) for v in race_counts.values()],
    'n': int(sum(race_counts.values()))
}

# Education (ses_edu)
edu_map = {
    '1': 'Less than HS',
    '2': 'High School',
    '3': 'Trade/Cert',
    '4': 'GED',
    '5': 'Some College',
    '6': 'Bachelor\'s',
    '7': 'Postgraduate'
}
edu_order = ['Less than HS', 'High School', 'GED', 'Trade/Cert', 'Some College', 'Bachelor\'s', 'Postgraduate']
edu_counts = df['ses_edu'].astype(str).map(edu_map).value_counts().to_dict()
edu_counts = {k: v for k, v in edu_counts.items() if pd.notna(k) and k != 'nan'}
# Sort by order
demographics['education'] = {
    'labels': [e for e in edu_order if e in edu_counts],
    'values': [int(edu_counts[e]) for e in edu_order if e in edu_counts],
    'n': int(sum(edu_counts.values()))
}

# Household Income (ses_thi)
income_map = {
    '1': '$0-25K',
    '2': '$26-50K',
    '3': '$51-75K',
    '4': '$76-100K',
    '5': '$101-150K',
    '6': '$151-200K',
    '7': '>$200K'
}
income_order = ['$0-25K', '$26-50K', '$51-75K', '$76-100K', '$101-150K', '$151-200K', '>$200K']

thi_counts = df['ses_thi'].astype(str).map(income_map).value_counts().to_dict()
thi_counts = {k: v for k, v in thi_counts.items() if pd.notna(k) and k != 'nan'}
demographics['household_income'] = {
    'labels': [i for i in income_order if i in thi_counts],
    'values': [int(thi_counts[i]) for i in income_order if i in thi_counts],
    'n': int(sum(thi_counts.values()))
}

# Personal Income (ses_tpi)
tpi_counts = df['ses_tpi'].astype(str).map(income_map).value_counts().to_dict()
tpi_counts = {k: v for k, v in tpi_counts.items() if pd.notna(k) and k != 'nan'}
demographics['personal_income'] = {
    'labels': [i for i in income_order if i in tpi_counts],
    'values': [int(tpi_counts[i]) for i in income_order if i in tpi_counts],
    'n': int(sum(tpi_counts.values()))
}

with open('viz_data/demographics.json', 'w') as f:
    json.dump(demographics, f, indent=2)
print(f"  ✓ Demographics exported (age, gender, race, education, income)")

# ============================================
# 3. PROBLEM GAMBLING BY STATE (Top 5 rates)
# ============================================
print("\n[3/5] Exporting problem gambling by state...")

# Calculate problem gambling rate per state (using FIPS codes)
state_gambling = df.groupby('demo_state').agg({
    'prob_gam': lambda x: (x.str.lower() == 'yes').sum(),  # Count of problem gamblers
    'ResponseId': 'count'  # Total responses
}).rename(columns={'prob_gam': 'problem_count', 'ResponseId': 'total'})

# Filter to only valid FIPS codes
valid_fips = set(code_to_name.keys())
state_gambling = state_gambling[state_gambling.index.astype(str).isin(valid_fips)]

state_gambling['rate'] = (state_gambling['problem_count'] / state_gambling['total'] * 100).round(2)
state_gambling = state_gambling[state_gambling['total'] >= 20]  # Minimum sample size
state_gambling = state_gambling.sort_values('rate', ascending=False)

top_states = state_gambling.head(10)  # Get top 10 for flexibility

# Convert FIPS to state names for display
prob_gambling_data = {
    'states': [code_to_name.get(str(fips).strip(), str(fips)) for fips in top_states.index.tolist()],
    'fips_codes': [str(fips) for fips in top_states.index.tolist()],
    'rates': top_states['rate'].tolist(),
    'problem_counts': top_states['problem_count'].astype(int).tolist(),
    'totals': top_states['total'].astype(int).tolist()
}

# Also calculate overall rate
total_problem = (df['prob_gam'].str.lower() == 'yes').sum()
total_responses = df['prob_gam'].notna().sum()
prob_gambling_data['overall_rate'] = round(total_problem / total_responses * 100, 2)
prob_gambling_data['overall_problem_count'] = int(total_problem)
prob_gambling_data['overall_total'] = int(total_responses)

with open('viz_data/problem_gambling_states.json', 'w') as f:
    json.dump(prob_gambling_data, f, indent=2)
print(f"  ✓ Top {len(top_states)} states by problem gambling rate exported")

# ============================================
# 4. ONLINE VS CASINO GAMBLING
# ============================================
print("\n[4/5] Exporting online vs casino gambling data...")

# Convert to numeric
df['mandf_onlineg'] = pd.to_numeric(df['mandf_onlineg'], errors='coerce')
df['mandf_casinog'] = pd.to_numeric(df['mandf_casinog'], errors='coerce')

gambling_comparison = {}

# Overall distributions
gambling_comparison['online'] = {
    'values': df['mandf_onlineg'].dropna().tolist(),
    'mean': round(df['mandf_onlineg'].mean(), 2),
    'median': round(df['mandf_onlineg'].median(), 2),
    'n': int(df['mandf_onlineg'].notna().sum())
}

gambling_comparison['casino'] = {
    'values': df['mandf_casinog'].dropna().tolist(),
    'mean': round(df['mandf_casinog'].mean(), 2),
    'median': round(df['mandf_casinog'].median(), 2),
    'n': int(df['mandf_casinog'].notna().sum())
}

# State-level comparison (difference between online and casino)
state_gambling_type = df.groupby('demo_state').agg({
    'mandf_onlineg': 'mean',
    'mandf_casinog': 'mean',
    'ResponseId': 'count'
}).rename(columns={'ResponseId': 'n'})

state_gambling_type = state_gambling_type[state_gambling_type['n'] >= 20]  # Min sample
state_gambling_type['difference'] = state_gambling_type['mandf_onlineg'] - state_gambling_type['mandf_casinog']
state_gambling_type = state_gambling_type.sort_values('difference', ascending=False)

# Top states preferring online (convert FIPS to names)
# Top states preferring online - only include states with meaningful online activity
online_active = state_gambling_type[state_gambling_type['mandf_onlineg'] >= 0.5]
top_online = online_active.sort_values('difference', ascending=False).head(5)
gambling_comparison['top_online_states'] = {
    'states': [code_to_name.get(str(fips).strip(), str(fips)) for fips in top_online.index.tolist()],
    'online_means': top_online['mandf_onlineg'].round(2).tolist(),
    'casino_means': top_online['mandf_casinog'].round(2).tolist(),
    'differences': top_online['difference'].round(2).tolist(),
    'n': top_online['n'].astype(int).tolist()
}

# Top states preferring casino (convert FIPS to names)
# Top states preferring casino - only include states with meaningful casino activity
casino_active = state_gambling_type[state_gambling_type['mandf_casinog'] >= 0.5]
top_casino = casino_active.sort_values('difference', ascending=True).head(5)
gambling_comparison['top_casino_states'] = {
    'states': [code_to_name.get(str(fips).strip(), str(fips)) for fips in top_casino.index.tolist()],
    'online_means': top_casino['mandf_onlineg'].round(2).tolist(),
    'casino_means': top_casino['mandf_casinog'].round(2).tolist(),
    'differences': top_casino['difference'].round(2).tolist(),
    'n': top_casino['n'].astype(int).tolist()
}

with open('viz_data/gambling_comparison.json', 'w') as f:
    json.dump(gambling_comparison, f, indent=2)
print(f"  ✓ Online vs casino gambling data exported")

# ============================================
# 5. AGE VS GAMBLING FREQUENCY (Scatter)
# ============================================
print("\n[5/5] Exporting age vs gambling frequency data...")

# Calculate average gambling frequency (online + casino) / 2
df['avg_gambling_freq'] = (df['mandf_onlineg'] + df['mandf_casinog']) / 2

# Create scatter data - filter for valid values
scatter_df = df[['demo_yrs', 'avg_gambling_freq', 'prob_gam']].dropna()

# Separate by problem gambling status for coloring
non_problem = scatter_df[scatter_df['prob_gam'].str.lower() != 'yes']
problem = scatter_df[scatter_df['prob_gam'].str.lower() == 'yes']

age_gambling_data = {
    'non_problem': {
        'age': non_problem['demo_yrs'].tolist(),
        'gambling_freq': non_problem['avg_gambling_freq'].tolist(),
        'n': len(non_problem)
    },
    'problem': {
        'age': problem['demo_yrs'].tolist(),
        'gambling_freq': problem['avg_gambling_freq'].tolist(),
        'n': len(problem)
    },
    'overall': {
        'age_mean': round(scatter_df['demo_yrs'].mean(), 1),
        'gambling_mean': round(scatter_df['avg_gambling_freq'].mean(), 2),
        'correlation': round(scatter_df['demo_yrs'].corr(scatter_df['avg_gambling_freq']), 3),
        'n': len(scatter_df)
    }
}

with open('viz_data/age_gambling_scatter.json', 'w') as f:
    json.dump(age_gambling_data, f, indent=2)
print(f"  ✓ Age vs gambling frequency data exported (n={len(scatter_df):,})")

# ============================================
# SUMMARY
# ============================================
print("\n" + "="*50)
print("✅ ALL DATA EXPORTED SUCCESSFULLY!")
print("="*50)
print("\nFiles created in 'viz_data/' folder:")
print("  • geographic.json")
print("  • demographics.json")
print("  • problem_gambling_states.json")
print("  • gambling_comparison.json")
print("  • age_gambling_scatter.json")
print("\nCopy the 'viz_data' folder to your website directory")
print("and open visualizations.html to see your dashboard!")

