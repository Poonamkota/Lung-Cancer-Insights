Module 3 SQL Queries

Write an SQL query to solve the given problem statement.
Task 1: How many values are there in the given dataset

SELECT COUNT(*) AS TotalValues FROM `lung_cancer`

Output: TotalValues 59

Task 2: Select the average age of individuals in the given dataset

SELECT AVG(age) AS AverageAge FROM `lung_cancer`

Output: AverageAge  42.6271

Task 3: Select the total count of 'Non-Smokers' in the given dataset
SELECT COUNT(*) AS TotalNonSmokers
FROM lung_cancer
WHERE Smoking_Category IN ('Non-Smokers');

Output: TotalNonSmokers 3

Task 4: Select the 'Name', 'Age', and 'Alcohol Category' columns for 'Mediocare Drinkers'
SELECT `Name`, `Age`,`Alcohol_Category` FROM `lung_cancer` WHERE `Alcohol_Category` = 'Mediocre Drinkers' order by `Age`

Output: 

Name	Age   	Alcohol_Category	
Yul	18	Mediocre Drinkers	
Gwyneth 	21	Mediocre Drinkers	
Lee 	21	Mediocre Drinkers	
Maggie 	26	Mediocre Drinkers	
John	27	Mediocre Drinkers	
Jane	28	Mediocre Drinkers	
Halle 	31	Mediocre Drinkers	
Anna	34	Mediocre Drinkers	
John	35	Mediocre Drinkers	
Faye 	37	Mediocre Drinkers	
Gene 	40	Mediocre Drinkers	
Katharine 	42	Mediocre Drinkers	
Gregory 	43	Mediocre Drinkers	
Barbra 	44	Mediocre Drinkers	
Jack 	47	Mediocre Drinkers	
Diane 	50	Mediocre Drinkers	
Ray	52	Mediocre Drinkers	
Charlize 	53	Mediocre Drinkers	
John 	55	Mediocre Drinkers	
Jane 	55	Mediocre Drinkers	
Jack 	56	Mediocre Drinkers	
Henry 	59	Mediocre Drinkers	
Peter 	62	Mediocre Drinkers	
Robert 	62	Mediocre Drinkers	
Maggie 	62	Mediocre Drinkers	



Task 5: Select the 'Name' and 'Age' of the oldest individual in the given dataset.
SELECT `Name`, `Age`
FROM `lung_cancer`
ORDER BY `Age` DESC Limit 1;
	
Output: 
Name   Rex
Age     77	

Task 6: Select the 'Name' and 'Surname' of individuals whose names start with 'A'.
SELECT `Name`,`Surname`
FROM `lung_cancer`
WHERE `Name` LIKE 'A%'
ORDER BY `Name` ASC;

Output: 

Name   	Surname	
Alec 	Guinness	
Alex	Telles	
Anna	Magnani	


Task 7: Select the 'Name', 'Age', and 'Alcohol' columns for individuals who are both 'Heavy Smokers' and 'Mediocare Drinkers'
SELECT `Name`, `Age`,`Alcohol` 
FROM `lung_cancer` 
WHERE `Smoking_Category` = 'Heavy Smokers' and `Alcohol_Category` = 'Mediocre Drinkers' 
order by `Age`

Output:

Name	Age   	Alcohol	
Lee 	21	3	
Gwyneth 	21	3	
Maggie 	26	8	
John	27	5	
Jane	28	8	
Halle 	31	4	
Anna	34	8	
Gene 	40	7	
Katharine 	42	5	
Gregory 	43	8	
Barbra 	44	6	
Jack 	47	8	
Diane 	50	4	
Ray	52	5	
Charlize 	53	3	
John 	55	4	
Jane 	55	3	
Jack 	56	3	
Henry 	59	4	
Robert 	62	5	
Peter 	62	4	
Katharine 	62	6	
Sissy 	63	5	
Sally 	69	4	
Charlton 	75	5	


Task 8: Find out the percentage of lung cancer for individuals whose age is greater than 18.
SELECT Result, COUNT(*) AS Count, 100.0 * (COUNT(*) / ( SELECT COUNT(*) AS total_count FROM lung_cancer WHERE Age > 18 )) AS Percentage FROM lung_cancer WHERE Age > 18 GROUP BY Result

Output: 

Result	Count	Percentage	
1	28	48.27586	
0	30	51.72414	


Task 9: Select the names and ages of individuals whose names contain the word "John".
SELECT `Name`,`Age`
FROM `lung_cancer`
WHERE `Name` LIKE '%John%';

Output:

Name	Age	
John	35	
John	27	
John 	55	


Task 10: Find the count of people who have lung cancer with different 'Smoking Category'.
SELECT `Smoking_Category`, COUNT(*) AS `Count` FROM `lung_cancer` WHERE `Result` = 1 GROUP BY `Smoking_Category`

Output:

Smoking_Category	Count	
Mediocre Smokers	5	
Heavy Smokers	23	


Task 11: Find the count of people who have lung cancer with different 'Alcohol Category'.
SELECT `Alcohol_Category`, COUNT(*) AS `Count` FROM `lung_cancer` WHERE `Result` = 1 GROUP BY `Alcohol_Category`

Output:

Mediocre Drinkers	28	

