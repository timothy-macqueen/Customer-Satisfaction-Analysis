# Customer-Satisfaction-Analysis
An Excel-based customer satisfaction analysis project demonstrating data cleaning, transformation, exploratory analysis, KPI development, PivotTables, interactive dashboards, and business insight generation.

### Project Overview
This project presents an interactive Customer Satisfaction Analysis Dashboard developed in Microsoft Excel. The objective was to clean, transform, analyse, and visualise customer survey data to identify patterns in customer satisfaction, purchasing behaviour, and recommendation rates.
The project demonstrates an end-to-end data analysis workflow, from data preparation and quality validation through to dashboard development and business reporting.

### Objectives
•	Analyse overall customer satisfaction.
•	Measure the proportion of customers who would recommend the business.
•	Analyse revenue across products and departments.
•	Identify differences in customer satisfaction across provinces and age groups.
•	Examine relationships between satisfaction ratings and customer sentiment.
•	Perform data quality checks to identify potential inconsistencies.
•	Present findings through an interactive Excel dashboard.

### Tools & Technologies
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
•	Filters
•	Data cleaning and transformation
•	Data validation and quality checks
•	Dashboard development
•	Data visualisation

### Data Preparation
Data privacy: This project uses entirely synthetic data generated with Python and Faker. It does not contain real customer or personally identifiable information.
Power Query was used to prepare the dataset before analysis. The data-cleaning workflow included transforming and standardising fields, checking data types, preparing analytical fields, and creating additional variables required for reporting.
The cleaned dataset was then used to build PivotTables, PivotCharts, KPI calculations, and the interactive dashboard.

### Project Structure
Download the complete Customer-Satisfaction-Analysis project folder, keeping the dashboard and raw data in the following structure:

Customer-Satisfaction-Analysis/
├── Customer_Satisfaction_Dashboard.xlsx
└── data/
    └── customer_satisfaction_raw.xlsx

### Refreshing the Power Query Workflow

The Excel dashboard uses Power Query to load and transform the raw customer satisfaction data. Follow these steps to configure the workflow on your computer.

**First-time setup**

1. Download or clone the complete Customer-Satisfaction-Analysis repository.
2. Open Customer_Satisfaction_Dashboard.xlsx in desktop Excel.
3. Navigate to Data → Get Data → Launch Power Query Editor.
4. In Power Query Editor, select Home → Manage Parameters.
5. Select pProjectFolder and update its value to the full local path of your downloaded Customer-Satisfaction-Analysis folder. For example: C:\Users\YourName\Documents\Customer-Satisfaction-Analysis. Do not include the data subfolder or the Excel filename in this parameter.
6. Click OK, then return to Excel.
7. Select Data → Refresh All to refresh the queries and update the dashboard.

**Subsequent refreshes**
Once configured, use Data → Refresh All whenever you want to refresh the workflow. If you move the project folder, update pProjectFolder to its new location.

Important: Keep the data subfolder and raw data filename unchanged unless you also update the relevant Power Query source path. The workbook and raw data file must remain accessible on your computer.

### Dashboard
The main dashboard provides a high-level view of customer satisfaction and purchasing performance.
Key Performance Indicators
The dashboard includes four headline KPIs:
•	Total Respondents
•	Average Satisfaction
•	Recommendation Rate
•	Total Revenue

### Dashboard Visualisations
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

### Additional Data Quality Checks
Additional analysis was performed separately from the main dashboard to assess the consistency and reliability of the survey data.
•	Average Satisfaction by Age Group
•	Average Purchase by Gender
•	Monthly Revenue Trend
•	Comment Outcome, Share of all respondents
•	Comment Sentiment by Satisfaction Rating

Interactive slicers allow the analysis to be filtered by:
•	Province
•	Department

**Recommendation Distribution**
This analysis compares the percentage recommendation by customers with number of respondents to identify whether the majority of customers recommended the products and services of the e-commerce store. 

**Comment Outcome, Share of all respondents**
A rating–comment agreement check was used to assess whether customer satisfaction ratings were consistent with the sentiment expressed in customer comments, including those that made "No Comment".
These checks help demonstrate that the analysis considered data quality and validation, rather than focusing solely on visualisation.

**Comment Sentiment by Satisfaction Rating (% of commented responses. 7.6% of respondents left no comment, spread evenly across ratings)**
This analysis compares numerical satisfaction ratings with customer sentiment to identify whether the two measures showed broadly consistent patterns or a mismatch.

#### Data Notes

- Positive comment matches Satisfied / Very Satisfied
- Neutral comment matches Neutral
- Negative comment matches Dissatisfied / Very Dissatisfied
- Anything else is a Mismatch
- Respondents with no comment (637, 7.6%) are marked Not Applicable and excluded

Agreement % = Match ÷ (Match + Mismatch) = 2,927 ÷ 7,710 = **38.0%**

**Chance benchmark**
If comments were assigned to respondents at random, the expected agreement would be:
(65.1% Positive × 40.1% Satisfied/Very Satisfied) + (11.7% Neutral × 19.5% Neutral) + (23.2% Negative × 40.4% Dissatisfied/Very Dissatisfied) ≈ **37.8%**
The percentages are shares of the 7,710 commented respondents. See below:

| Rating group | Calculation | Share |
| --- | --- | --- |
| Satisfied + Very Satisfied | (1,518 + 1,576) ÷ 7,710 = 3,094 ÷ 7,710 | 40.1% |
| Neutral | 1,500 ÷ 7,710 | 19.5% |
| Dissatisfied + Very Dissatisfied | (1,562 + 1,554) ÷ 7,710 = 3,116 ÷ 7,710 | 40.4% |

**Sentiment method**
An initial keyword-based rule misclassified many comments (e.g. "Product was disappointing" and "Delivery delayed" were labelled Neutral). Because the survey uses a small set of repeated phrases, each distinct comment was labelled manually (Positive, Negative or Neutral) in a lookup table (`Sentiment_Map`) and merged into the data in Power Query. New phrases after a refresh must be added to the map, otherwise they return null.

**Limitations**
- Sentiment labels are my own judgement, so borderline phrases (e.g. "Packaging could improve") could be labelled differently.
- Neutral comments count as a Mismatch against Satisfied and Dissatisfied ratings. This is a deliberate, strict rule.
- The comment field appears unrelated to ratings (see findings), so agreement reflects the dataset, not customer behaviour.
- All data is synthetic, so findings illustrate analysis methods rather than real customer behaviour.


## Key Findings
•   Satisfaction and revenue show limited alignment: Only 1 of the top 10 highest-revenue products also ranks in the top 10 for satisfaction. Notably, the Samsung 55-inch      Smart TV and Lenovo ThinkPad Laptop are both top-10 revenue earners despite ranking in the bottom 10 for customer satisfaction — a disconnect worth                         investigating further, as these products carry more commercial risk than their satisfaction scores suggest.
•	The electronics department drove the highest total revenue.
•	Average satisfaction sits at 3 out of 5, with only half of respondents saying they'd recommend the business
•	The Northern Cape recorded the highest average satisfaction of any province
•   The Nikon Mirrorless Camera was the top selling by units; instant noodles the lowest.
•	Written comments and satisfaction ratings showed limited agreement: Only 38.0% of commented responses had sentiment matching the rating (blank comments            excluded). That is almost identical to the 37.8% expected if comments were assigned at random.
•   Sentiment was spread evenly across ratings: Positive comments made up 65.1% of all comments, including 66.0% of Very Dissatisfied and 64.5% of Very Satisfied      respondents. Very Satisfied respondents were slightly more likely to leave a Negative comment (24.6%) than Very Dissatisfied respondents (22.0%).

**Implication** 
Very Dissatisfied customers left comments such as "Excellent product" and "Highly recommend". This suggests the free-text field is not meaningfully linked to ratings in this dataset. This dataset is synthetic (generated with Python). Comments were assigned independently of satisfaction ratings, so agreement is close to what chance would produce. In a real dataset, this result would signal a data quality problem worth investigating. The Rating-Comment Agreement KPI and Comment Sentiment by Satisfaction Rating therefore demonstrate data validation checks rather than customer insights.

These findings demonstrate how raw customer survey data can be transformed into concise, decision-supporting insights.

## Recommendations
•	Investigate products with below-average satisfaction. 
•	Review customer feedback for recurring complaints. 
•	Focus marketing on high-performing products. 
•	Monitor provinces with lower satisfaction to identify service improvements.

#### Project Workflow
The project followed an end-to-end analytical workflow:
Raw Data → Power Query → Cleaned Data → KPI Calculations → PivotTables → PivotCharts → Dashboard → Data Quality Checks → Business Insights

#### Project Files

#### File Descriptions
•	Customer_Satisfaction_Dashboard.xlsx - Complete Excel workbook containing the cleaned data, calculations, PivotTables, charts, dashboard, and data-quality analysis.
•	customer_satisfaction_raw.xlsx -	Excel workbook containing the raw data to be inputted into Power Query.
•	Products.xlsx - Excel workbook which was generated by product_purchase_amount.py. Was included because each time the script is run the purchase amounts are randomized.
•	Data_Cleaning_Power_Query.pdf -	Written report summarising the data cleaning process. 
•	generate_customer_data.py - Python script to produce raw data.
•	product_purchase_amount.py - Python script to generate correct purchase amounts for South Africa in 2026.
•	department.py - Python script to generate the lookup table to do VLOOKUP to showcase the department for each product.
•	screenshots/dashboard.png - Screenshot of the completed interactive dashboard.
•	screenshots/power-query.png - Screenshot demonstrating the Power Query data-preparation process
•	screenshots/extra-analysis – Screenshot demonstrating the additional analysis

#### Skills Demonstrated
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

## Conclusion
This project demonstrates the ability to take a customer survey dataset through a structured data-analysis process and transform it into an interactive reporting solution. The combination of data preparation, analytical calculations, visualisation, and quality checks demonstrates practical Excel-based data analysis and reporting skills. 
