# Customer-Satisfaction-Analysis
An Excel-based customer satisfaction analysis project demonstrating data cleaning, transformation, exploratory analysis, KPI development, PivotTables, interactive dashboards, and business insight generation.

Project Overview:
This project presents an interactive Customer Satisfaction Analysis Dashboard developed in Microsoft Excel. The objective was to clean, transform, analyse, and visualise customer survey data to identify patterns in customer satisfaction, purchasing behaviour, and recommendation rates.
The project demonstrates an end-to-end data analysis workflow, from data preparation and quality validation through to dashboard development and business reporting.

Objectives:
•	Analyse overall customer satisfaction.
•	Measure the proportion of customers who would recommend the business.
•	Analyse revenue across products and departments.
•	Identify differences in customer satisfaction across provinces and age groups.
•	Examine relationships between satisfaction ratings and customer sentiment.
•	Perform data quality checks to identify potential inconsistencies.
•	Present findings through an interactive Excel dashboard.

Tools & Technologies:
•	Microsoft Excel
•	Power Query
•	Python
•	Faker
•	VS Code
•	PivotTables
•	PivotCharts
•	XLOOKUP
•	VLOOKUP
•	Excel formulas
•	Excel functions
•	Data cleaning and transformation
•	Data validation and quality checks
•	Dashboard development
•	Data visualisation

Data Preparation:
Data privacy: This project uses entirely synthetic data generated with Python and Faker. It does not contain real customer or personally identifiable information.
Power Query was used to prepare the dataset before analysis. The data-cleaning workflow included transforming and standardising fields, checking data types, preparing analytical fields, and creating additional variables required for reporting.
The cleaned dataset was then used to build PivotTables, PivotCharts, KPI calculations, and the interactive dashboard.

Power Query Setup
The workbook uses a Power Query parameter called pProjectFolder to locate the raw data file without relying on the author's personal file path.

The project folder should maintain the following structure:

Customer-Satisfaction-Analysis/
├── Customer_Satisfaction_Dashboard.xlsx
└── data/
    └── raw_customer_satisfaction.xlsx
To refresh the Power Query workflow download the complete Customer-Satisfaction-Analysis project folder.
Open Customer_Satisfaction_Dashboard.xlsx.
Go to Data → Get Data → Launch Power Query Editor.
In Power Query, select Home → Manage Parameters.
Select pProjectFolder.
Set the parameter value to the location of the downloaded Customer-Satisfaction-Analysis folder on your computer.
Click OK.
Return to Excel and select Data → Refresh All.

Power Query will automatically locate the raw data using:
pProjectFolder\data\customer_satisfaction_raw.xlsx

Dashboard:
The main dashboard provides a high-level view of customer satisfaction and purchasing performance.
Key Performance Indicators
The dashboard includes four headline KPIs:
•	Total Respondents
•	Average Satisfaction
•	Recommendation Rate
•	Total Revenue

Dashboard Visualisations:
The dashboard includes the following analyses:
1.	Average Satisfaction by Top 10 Products
2.	Average Satisfaction by Bottom 10 Products
3.	Revenue by Top 10 Products
4.	Revenue by Bottom 10 Products
5.	Revenue by Department                                         
6.	Average Satisfaction by Province

Interactive slicers allow the analysis to be filtered by:
•	Province
•	Department

Additional Data Quality Checks:
Additional analysis was performed separately from the main dashboard to assess the consistency and reliability of the survey data.
•	Average Satisfaction by Age Group
•	Average Purchase by Gender
•	Monthly Revenue Trend
•	Recommendation Distribution
This analysis compares the percentage recommendation by customers with number of respondents to identify whether the majority of customers recommended the products and services of the e-commerce store. 

Rating–Comment Agreement:
A rating–comment agreement check was used to assess whether customer satisfaction ratings were consistent with the sentiment expressed in customer comments.
These checks help demonstrate that the analysis considered data quality and validation, rather than focusing solely on visualisation.

Satisfaction × Sentiment:
This analysis compares numerical satisfaction ratings with customer sentiment to identify whether the two measures show broadly consistent patterns.
Interactive slicers allow the analysis to be filtered by:
•	Province
•	Department

Key Findings:
The final findings will be based on the completed dashboard and calculated results.
•	Overall Average Satisfaction: 3 out of 5.
•	Recommendation: 50% of respondents indicated that they would recommend the business.
•	Revenue Performance: The electronics department generated the highest total revenue.
•	Customer Satisfaction: The Northern Cape recorded the highest average satisfaction.
•	Product Performance: The Nikon Mirrorless Camera was the highest selling product and instant noodles were the lowest selling product. 
These findings demonstrate how raw customer survey data can be transformed into concise, decision-supporting insights.

Recommendations:
•	Investigate products with below-average satisfaction. 
•	Review customer feedback for recurring complaints. 
•	Focus marketing on high-performing products. 
•	Monitor provinces with lower satisfaction to identify service improvements.

Project Workflow:
The project followed an end-to-end analytical workflow:
Raw Data → Power Query → Cleaned Data → KPI Calculations → PivotTables → PivotCharts → Dashboard → Data Quality Checks → Business Insights

Project Files

File	Descriptions:
•	Customer_Satisfaction_Dashboard.xlsx - Complete Excel workbook containing the cleaned data, calculations, PivotTables, charts, dashboard, and data-quality analysis.
•	customer_satisfaction_raw.xlsx -	Excel workbook containing the raw data to be inputted into Power Query.
•	Products2.xlsx - Excel workbook which was generated by product_purchase_amount.py. Was included because each time the script is run the purchase amounts are randomized.
•	Data_Cleaning_Power_Query.pdf -	Written report summarising the data cleaning process. 
•	generate_customer_data.py - Python script to produce raw data.
•	product_purchase_amount.py - Python script to generate correct purchase amounts for South Africa in 2026.
•	department.py - Python script to generate the lookup table to do VLOOKUP to showcase the department for each product.
•	screenshots/dashboard.png - Screenshot of the completed interactive dashboard.
•	screenshots/power-query.png -	Screenshot demonstrating the Power Query data-preparation process.

Skills Demonstrated:
This project demonstrates practical experience in:
•	Data cleaning
•	Data transformation
•	Data validation
•	Excel data analysis
•	Power Query
•	XLOOKUP
•	VLOOKUP
•	PivotTables
•	PivotCharts
•	KPI development
•	Dashboard design
•	Data visualisation
•	Data quality assurance
•	Analytical interpretation
•	Business reporting

Conclusion:
This project demonstrates the ability to take a customer survey dataset through a structured data-analysis process and transform it into an interactive reporting solution. The combination of data preparation, analytical calculations, visualisation, and quality checks demonstrates practical Excel-based data analysis and reporting skills. 
