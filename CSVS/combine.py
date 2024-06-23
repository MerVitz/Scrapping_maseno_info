# -*- coding: utf-8 -*-
import pandas as pd

msu_all_programs = pd.read_csv('C:/Users/user/Desktop/Scrapping_maseno_info/CSVS/msu_all_programs.csv')
msu_info = pd.read_csv('C:/Users/user/Desktop/Scrapping_maseno_info/CSVS/msu_info.csv')

print("msu_all_programs columns:", msu_all_programs.columns)
print("msu_info columns:", msu_info.columns)

# Reshape msu_all_programs to a long format
program_types = ['Doctorate', 'Masters', 'Bachelors', 'Diploma', 'Certificate']
long_format_programs = pd.melt(msu_all_programs, var_name='Category', value_name='Program Name', value_vars=program_types)

# Remove rows with empty program names
long_format_programs = long_format_programs.dropna().reset_index(drop=True)

# Add missing columns to match msu_info structure
long_format_programs['Detail'] = long_format_programs['Category']
long_format_programs['Category'] = 'Program Information'
long_format_programs['Additional Info'] = long_format_programs['Program Name']

# Select relevant columns
long_format_programs = long_format_programs[['Category', 'Detail', 'Additional Info']]

# Combine the two dataframes
combined_data = pd.concat([long_format_programs, msu_info], ignore_index=True)

# Save the combined dataframe to a new CSV file
combined_data.to_csv('C:/Users/user/Desktop/Scrapping_maseno_info/CSVS/msu_combined.csv', index=False)

print("Data has been combined and saved to msu_combined.csv")
