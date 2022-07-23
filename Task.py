# import the library
# Give an alias
import pandas as pd

# Read the csv file
data_file = pd.read_csv('al_results_2020 (1).csv')
# The columns Zscore, gender, and syllabus removed
data_file = data_file.drop(columns=['Zscore', 'gender', 'syllabus'])

# saving a modified file .csv
data_file.to_csv('modified.csv')

# using conditions to find rows with absent values for student with  '|' as a or statement
student_with_one_or_absents = data_file.loc[ (data_file['sub1_r'] == 'Absent') | (data_file['sub2_r'] == 'Absent') | (data_file['sub3_r'] == 'Absent') | (data_file['cgt_r'] == 'Absent')]
# saving all the absent data in a file
student_with_one_or_absents.to_csv('absents.csv')

# using conditions to find rows with no absent values for student with  '&' as a and statement
data_file = data_file.loc[ (data_file['sub1_r'] != 'Absent') & (data_file['sub2_r'] != 'Absent') & (data_file['sub3_r'] != 'Absent') & (data_file['cgt_r'] != 'Absent')]
# saving a modified file .csv
data_file.to_csv('modified.csv')