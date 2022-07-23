# import the library
# Give an alias
import pandas as pd

# Read the csv file
data_file = pd.read_csv('al_results_2020 (1).csv')
# The columns Zscore, gender, and syllabus removed
data_file = data_file.drop(columns=['Zscore', 'gender', 'syllabus'])

# saving a modified file .csv
data_file.to_csv('modified.csv')