## Lung Cancer Insight: A Comprehensive Study using SQL
In this project, analyze the Lung Cancer Data Set and visualize smoking's impact on health, correlating it with lung cancer. Discover smoking's role in lung cancer across age groups and identify the most affected age-group.Lung Cancer Insights: Module 1 Data Cleaning & Preprocessing


## Project Description: Project Description
This project aims to comprehensively analyze the Lung Cancer Data Set, highlighting the significant impact of smoking on health, leading to lung cancer. By examining data trends, we'll uncover how smoking relates to lung cancer across different age groups and pinpoint the age group with the highest smoking rates. Through visualization, we'll illuminate the connections between smoking behaviors and their health outcomes, providing insights into the varying effects on different age groups.

import pandas as pd
import warnings
warnings.filterwarnings('ignore')

##Task 1: Load the Data : Read the patients data using 'lung_cancer_examples.csv' through pandas library and return the dataset for the further analysis.

def read_csv():
    # Method to read the CSV file "lung_cancer_examples.csv" using pandas.
    df = pd.read_csv("lung_cancer_examples.csv")
    return df

##Task 2: Find The duplicate values. We need to check for duplicate values in a dataset 'lung_cancer_examples'. Finally, the counts of duplicated values are returned as a integer. This information can be useful in identifying duplicate data and deciding on appropriate strategies to deal with them, such as imputation or deletion.

def check_duplicates():
    df = read_csv()
    # Method to check for duplicate rows in the DataFrame.
    # Returns: The number of duplicated rows found in the DataFrame.
    count_dup = df.duplicated().sum()
    return count_dup

##Task 3: Find the nUll Values : The function check_null_values() , calculates the sum of null (missing) values for each column in the DataFrame. It then returns a Series containing the count of null values for each column in the DataFrame. This provides insights into the presence and extent of missing data in the dataset after duplicates have been dropped.


def check_null_values():
    df = read_csv()
    # Method to check for null (missing) values in the DataFrame.
    # Returns: A pandas Series indicating the count of null values for each column in the DataFrame.
    check_null = df.isna().sum()
    return check_null

##Task 4: Renaming the columns
def rename_column():
    # do not edit the predefined function name
    df = read_csv()
    # Rename columns 'Alkhol' to 'Alcohol'.
    df.rename(columns = {'Alkhol':'Alcohol'}, inplace = True)
    return df

##Task 5: Check the values: The check_smoke_value() function is designed to analyze a dataset containing information about smoking habits, and it returns the count of each unique value present in the 'Smokes' column. 

def check_smoke_value():
    # do not edit the predefined function name
    data = rename_column()

    # Count the occurrences of each unique value in the 'Smokes' column
    smokes_counts = data['Smokes'].value_counts()

    # Return the counts of each unique smoking habit value
    return smokes_counts

