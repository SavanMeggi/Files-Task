# import the library
# Give an alias
import pandas as pd

# Read the csv file
data_file = pd.read_csv('al_results_2020 (1).csv')
# The columns Zscore, gender, and syllabus removed
data_file = data_file.drop(columns=['Zscore', 'gender', 'syllabus'])

# saving a modified file .csv
#data_file.to_csv('modified.csv')

# using conditions to find rows with absent values for student with  '|' as a or statement
#student_with_one_or_absents = data_file.loc[ (data_file['sub1_r'] == 'Absent') | (data_file['sub2_r'] == 'Absent') | (data_file['sub3_r'] == 'Absent') | (data_file['cgt_r'] == 'Absent')]
# saving all the absent data in a file
#student_with_one_or_absents.to_csv('absents.csv')

#


# using conditions to find rows with no absent values for student with  '&' as a and statement
data_file = data_file.loc[ (data_file['sub1_r'] != 'Absent') & (data_file['sub2_r'] != 'Absent') & (data_file['sub3_r'] != 'Absent') & (data_file['cgt_r'] != 'Absent') & (data_file['birth_day'] != 'Invalid error') & (data_file['birth_year'] != 'Invalid error') & (data_file['island_rank'] != '-') & (data_file['district_rank'] != '-')]
# saving a modified file .csv
#data_file.to_csv('modified.csv')

months_dict = {'January': '01', 'February': '02', 'March': '03', 'April': '04', 'May': '05', 'June': '06',
               'July': '07', 'August': '08', 'September': '09', 'October': '10', 'November': '11', 'December': '12'}

data_file['birth_month'] = data_file['birth_month'].apply(lambda key: months_dict[key])

#  concatenate birth_day, birth_month and birth_day to form new birthdate column
data_file['birth_date'] = data_file['birth_day'].astype(str) + '-' + data_file['birth_month'] + '-' + data_file[
    'birth_year'].astype(str)

data_file['birth_date'] = pd.to_datetime(data_file['birth_date'], format='%d-%m-%Y', errors='course')

data_file = data_file.drop(columns=['birth_day', 'birth_month', 'birth_year'])
# data_file.to_csv('modified.csv')
