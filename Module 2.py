Module 2 : Data Transformation & Database Integration

import module1 as t1

##Task 1: Categorise the Smoke Values : The categorize_smokers(x) function takes an input x, which represents the number of cigarettes smoked per day for an individual. It then categorizes individuals into different groups based on their smoking habits:
# Function to categorize individuals based on the number of cigarettes smoked per day
def categorize_smokers(x):
    #If x is 0, categorize the person as 'Non-Smokers'.
    if x == 0:
        return 'Non-Smokers'
    # If x is less than or equal to 2, categorize the person as 'Light Smokers'.
    elif x <= 2:
        return 'Light Smokers'
    # If x is greater than 2 and less than or equal to 10, categorize the person as 'Mediocre Smokers'.
    elif x >2 and x <= 10:
        return 'Mediocre Smokers'
    # If x is greater than 10, categorize the person as 'Heavy Smokers'.
    elif x > 10:
        return 'Heavy Smokers' 
    else:
        return 'Invalid Input'
        
##Task 2: Check the values : The check_alcohol_value() function is designed to analyze a dataset containing information about smoking habits, and it returns the count of each unique value present in the 'Alcohol' column. 
# Function to process the smoking data and add a new 'Smoking_Category' column
def smokes():
    # do not edit the predefined function name
    data = t1.rename_column()

    # Applying the 'categorize_smokers' function to each value in the 'Smokes' column
    # and storing the result in a new column 'Smoking_Category'
    data['Smoking_Category'] = data['Smokes'].apply(categorize_smokers)
    return data

    # Returning the modified dataset with the new 'Smoking_Category' column
    return data


def check_alcohol_value():
    # do not edit the predefined function name
    data = smokes()


    # Count the occurrences of each unique value in the 'Alcohol' column
    Alcohol_counts = data['Alcohol'].value_counts()

    # Return the counts of each unique smoking habit value
    return Alcohol_counts

##Task 3: Categories the Alcohol Values : In the categorize_alcohol(x) function, individuals are categorized into different groups based on their alcohol consumption:
# Function to categorize individuals based on the number of alcohol drinks consumed per day
def categorize_alcohol(x):

    # If x is 0, categorize the person as 'Non-Drinkers'.
    if x == 0:
        return 'Non-Drinkers'
    # If x is less than or equal to 2, categorize the person as 'Light Drinkers'.
    elif x <= 2:
        return 'Light Drinkers'
    # If x is greater than 2 and less than or equal to 10, categorize the person as 'Mediocre Drinkers'.
    elif x >2 and x <= 10:
        return 'Mediocre Drinkers'
    # If x is greater than 10, categorize the person as 'Heavy Drinkers'.
    elif x > 10:
        return 'Heavy Drinkers' 
    else:
        return 'Invalid Input'
    pass



# Function to process the alcohol data and add a new 'Alcohol_Category' column
def alkhol():
    # Assuming the 'smokes()' function retrieves the dataset with the 'Smokes' column and the 'Alcohol' column
    data = smokes()

    # Applying the 'categorize_alcohol' function to each value in the 'Alcohol' column
    # and storing the result in a new column 'Alcohol_Category'
    data['Alcohol_Category'] = data['Alcohol'].apply(categorize_alcohol)

    # Returning the modified dataset with the new 'Alcohol_Category' column
    return data

##Task 4: Exporting the Cleaned Dataset : The function export_the_dataset() exports the cleaned DataFrame to a new CSV file named 'lung_cancer.csv'. It uses the pandas library to write the data to the CSV file.

 # The DataFrame obtained from the previous task is used as input and return the cleaned dataframe 'df'.


def export_the_dataset():
    # do not edit the predefined function name
    df = alkhol()
    # write your code to export the cleaned dataset and set the index=false and return the same as 'df'
    df.to_csv(r"lung_cancer.csv", index=False)
    return df

##Task 5: Generate tables using clened dataset

Download the cleaned dataset by clicking on the 'lung_cancer.csv' from File explorer

Utilize the MySQL database and import the cleaned dataset and create the table name 'lung_cancer' that should contains the below columns.

Name
Surname
Age
Smokes
AreaQ
Alcohol
Result
Smoking_Category
Alcohol_Category
To begin with SQL Queries, we need to ensure that the cleaned datasets, "lung_cancer.csv" is uploaded to a MySQL database 

