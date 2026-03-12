# Gambling Behavior & Mental Health Analysis

A comprehensive data visualization project demonstrating SQL database design, complex queries, and interactive Python visualizations using a single combined dataset of 2,560 survey participants.

## 🎯 Project Overview

This project analyzes gambling behavior and mental health data using SQL and Python. It demonstrates:

- **SQL Database Design**: Creating a SQLite database from a single CSV file
- **Complex SQL Queries**: CASE statements, CTEs, conditional aggregation, GROUP BY with HAVING
- **Data Analysis**: Using Python and Pandas for data processing
- **Interactive Visualizations**: Creating interactive charts with Plotly
- **Web Dashboard**: Presenting findings in a responsive HTML interface

## 📊 Dataset

**File**: `combined-scoring.csv`
- **2,560 participants** across three populations:
  - 855 Adolescent/Young Adult (ad_data)
  - 696 Older Adult (dvs_data)
  - 1,009 General Population (g25_data)
- **104 variables** including:
  - Demographics (age, gender, location)
  - Gambling measures (BBGS, SOGS, GSAS scores)
  - Mental health (depression, mania, anxiety)
  - Behavioral traits (reward sensitivity, impulsivity)
  - Social support measures

## 🏗️ Project Structure

```
gambling-analysis-project/
├── data/
│   ├── combined-scoring.csv
│   └── gambling_research.db (generated)
├── scripts/
│   ├── 01_create_database.py
│   └── 02_analysis.py
├── visualizations/
│   ├── age_distribution.json
│   ├── gambling_prevalence.json
│   ├── mental_health.json
│   ├── geographic.json
│   └── risk_factors.json
├── index.html
└── README.md
```

## 🚀 Getting Started

### Prerequisites

```bash
pip install pandas plotly
```

(SQLite comes built-in with Python)

### Running the Analysis

1. **Create the Database**
   ```bash
   cd scripts
   python 01_create_database.py
   ```
   This loads the CSV into SQLite and creates indexes.

2. **Run Analysis & Generate Visualizations**
   ```bash
   python 02_analysis.py
   ```
   This executes 5 SQL queries and creates interactive visualizations.

3. **View the Dashboard**
   Open `index.html` in your web browser.

## 📈 SQL Analyses

### Analysis 1: Age Distribution
- **Technique**: GROUP BY with CASE statements
- **Purpose**: Compare age ranges across three study populations
- **Result**: Overlapping histogram showing distinct age groups

### Analysis 2: Gambling Prevalence by Demographics
- **Technique**: Conditional aggregation (CASE within SUM)
- **Purpose**: Calculate prevalence rates by age group and gender
- **Result**: Grouped bar chart showing demographic differences

### Analysis 3: Mental Health by Gambling Status
- **Technique**: Common Table Expression (CTE)
- **Purpose**: Compare mental health scores between groups
- **Result**: Multi-panel comparison of depression, mania, and behavioral inhibition

### Analysis 4: Geographic Distribution
- **Technique**: GROUP BY with HAVING for statistical filtering
- **Purpose**: Identify state-level patterns in gambling problems
- **Result**: Horizontal bar chart of top 20 states

### Analysis 5: Risk Factors by Age
- **Technique**: CTE with nested CASE and conditional aggregation
- **Purpose**: Examine reward sensitivity across age groups
- **Result**: Grouped bar chart comparing gamblers vs non-gamblers

## 🔍 Key SQL Techniques Demonstrated

```sql
-- CASE Statements for Categorization
CASE 
    WHEN demo_yrs < 25 THEN '18-24'
    WHEN demo_yrs BETWEEN 25 AND 34 THEN '25-34'
    ELSE '35+'
END as Age_Group

-- Conditional Aggregation
SUM(CASE WHEN prob_gam = 'yes' THEN 1 ELSE 0 END) as Count_With_Issues

-- Common Table Expressions (CTEs)
WITH filtered_data AS (
    SELECT ... FROM table WHERE conditions
)
SELECT ... FROM filtered_data

-- GROUP BY with HAVING
GROUP BY state
HAVING COUNT(*) >= 10

-- Complex Aggregations
ROUND(AVG(CASE WHEN condition THEN column END), 2)
```

## 📊 Visualization Features

All visualizations are interactive with:
- **Zoom & Pan**: Explore data in detail
- **Hover Info**: See exact values on mouseover
- **Responsive Design**: Works on desktop and mobile
- **Export Options**: Download as PNG

## 🌐 Deploying to GitHub Pages

1. **Copy to your repository**:
   ```bash
   cp -r gambling-analysis-project /your/repo/projects/
   ```

2. **Update the GitHub link** in `index.html` (line ~750)

3. **Push to GitHub**:
   ```bash
   git add .
   git commit -m "Add gambling analysis project"
   git push
   ```

4. **Your site will be live at**:
   `https://yourusername.github.io/projects/gambling-analysis-project/`

## 🔗 Tableau Integration

The SQLite database is ready for Tableau Desktop:

1. Open Tableau Desktop
2. Connect → More → SQLite
3. Navigate to `gambling_research.db`
4. Start building dashboards!

## 📝 Project Highlights

**For Your Portfolio:**

"Developed a full-stack data analysis project using SQL and Python to analyze 2,560 survey responses across three populations. Wrote complex SQL queries featuring CTEs, conditional aggregation, and statistical filtering. Created 5 interactive Plotly visualizations and deployed a responsive web dashboard. Demonstrates proficiency in database design, query optimization, and data storytelling."

**Key Skills Demonstrated:**
- SQL query design and optimization
- Python data analysis with Pandas
- Interactive data visualization
- Web development (HTML/CSS/JavaScript)
- Statistical analysis
- Technical documentation

## 🛠️ Technologies

- **Database**: SQLite
- **Data Processing**: Python 3.x, Pandas
- **Visualization**: Plotly
- **Web**: HTML5, CSS3, JavaScript
- **Version Control**: Git-ready

## 📧 Contact

Cooper Sharp  
[Your Email]  
[Your LinkedIn]  
[Your Portfolio Website]

## 📄 License

This project is available for educational and portfolio purposes.

---

**Note**: Data has been de-identified to protect participant privacy.
