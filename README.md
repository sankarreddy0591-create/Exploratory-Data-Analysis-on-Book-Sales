# 📚 Exploratory-Data-Analysis-on-Book-Sales
EDA


## 📚 Exploratory Data Analysis (EDA) on Book Sales

## 📌 Project Overview

This project focuses on **Exploratory Data Analysis (EDA) of Book Sales Data** using Python. The objective is to understand book publishing trends, genres, author ratings, book popularity, sales performance, and publisher revenue.

The project uses data analysis and visualization techniques to identify patterns, explore relationships between variables, and generate meaningful insights from the dataset.

## 🎯 Project Objectives

- 📖 Analyze book publishing years and publishing trends.
- 📊 Explore the distribution of books across different genres.
- ⭐ Analyze average book ratings and ratings counts.
- ✍️ Identify authors based on average ratings and gross sales.
- 💰 Examine the relationship between sale price and units sold.
- 🌍 Analyze book language distribution.
- 🏢 Evaluate publisher revenue.
- 🧹 Identify missing values, duplicate records, and data quality issues.
- 📈 Visualize sales trends over the years.

## 📂 Dataset Information

**Dataset Name:** `Books_Data_Clean.csv`

**Dataset Type:** Structured CSV data

The dataset contains information related to books, authors, ratings, publishing years, genres, languages, prices, sales, and publisher revenue.

### Important Dataset Columns

| Column | Description |
|---|---|
| `Book Name` | Name of the book |
| `Author` | Name of the author |
| `Publishing Year` | Year the book was published |
| `genre` | Book genre or category |
| `Book_average_rating` | Average rating of the book |
| `Book_ratings_count` | Number of book ratings |
| `Author_Rating` | Author rating category |
| `sale price` | Selling price of the book |
| `units sold` | Number of units sold |
| `gross sales` | Gross sales associated with the book |
| `publisher revenue` | Revenue attributed to the publisher |
| `Publisher ` | Publisher name |
| `language_code` | Language code of the book |

*Note: The exact column names follow the supplied dataset. The complete list can be checked in the dataset.*

## 🛠️ Technologies Used

- 🐍 **Python** — Main programming language
- 🐼 **Pandas** — Data manipulation and analysis
- 🔢 **NumPy** — Numerical operations
- 📊 **Matplotlib** — Data visualization
- 🎨 **Seaborn** — Statistical visualization
- 💻 **Jupyter Notebook / VS Code** — Development environment

## 🔄 Project Workflow
```
    Import Libraries 
        ↓
    Load Dataset 
        ↓
    Inspect Data  
        ↓
    Clean Data 
        ↓
    Analyze Data  
        ↓
    Visualize Results 
        ↓
    Summarize Insights.
```

### 1. Import Required Libraries
Imported NumPy, Pandas, Matplotlib, and Seaborn for data processing, statistical analysis, and visualization.

### 2. Load the Dataset
Loaded the `Books_Data_Clean.csv` dataset into a Pandas DataFrame.

### 3. Understand the Dataset
- Displayed the first and last five records.
- Checked the dataset structure and column data types.
- Examined descriptive statistics.
- Reviewed the dataset columns.

### 4. Data Cleaning
- Filtered records to retain publishing years greater than 1900.
- Checked missing values in each column.
- Removed records with missing book names.
- Checked duplicate records.
- Examined the number of unique values in each column.

### 5. Exploratory Data Analysis
Performed numerical and categorical analysis to understand book characteristics, author performance, ratings, and sales patterns.

### 6. Data Visualization
Created charts to identify distributions, comparisons, and relationships among important variables.

### 7. Generate Insights
Examined the results to understand publishing trends, genre distributions, book ratings, sales performance, and publisher revenue.

## 📊 Data Visualization

The project includes the following visualizations:

| Visualization | Purpose |
|---|---|
| Publishing Year Histogram | Understand the distribution of publishing years |
| Genre Bar Chart | Compare the number of books across genres |
| Genre Rating Box Plot | Compare book rating distributions by genre |
| Sale Price vs Units Sold Scatter Plot | Explore the relationship between selling price and units sold |
| Language Distribution Pie Chart | Examine the distribution of book languages |
| Average Rating vs Ratings Count Scatter Plot | Explore the relationship between ratings and rating counts |
| Top 20 Authors by Gross Sales | Compare authors based on total gross sales |
| Units Sold by Author Rating Box Plot | Compare sales distributions across author rating categories |
| Yearly Units Sold Line Chart | Examine changes in total units sold over time |

## 🔍 Key Analysis Areas

### 📚 Publishing Trends
Examined book publishing years to understand the distribution of publication records.

### 🎭 Genre Analysis
Compared the number of books across genres and explored differences in average book ratings.

### ⭐ Author and Rating Analysis
Calculated average book ratings by author and examined book rating counts across author rating categories.

### 💰 Sales Performance
Analyzed sale prices, units sold, gross sales by author, and yearly sales volume.

### 🌍 Language Analysis
Examined book counts by language code and visualized the language distribution.

### 🏢 Publisher Revenue Analysis
Aggregated publisher revenue to compare the revenue associated with different publishers.

## 📁 Project Structure

```text
EDA Book Sales/
│
├── Data/
│   └── Books_Data_Clean.csv
│
├── Notebooks/
│   └── EDA_Analysis.ipynb
|
├── src/
│   └── eda_analysis.py
│
├── visualization/
│   ├── publishing_year_distribution.png
│   ├── books_by_genre.png
│   ├── ratings_by_genre.png
│   ├── sale_price_vs_units_sold.png
│   ├── language_distribution.png
│   ├── rating_vs_ratings_count.png
│   ├── top_authors_by_sales.png
│   ├── units_sold_by_author_rating.png
│   └── yearly_units_sold.png
│
├── README.md
└── requirements.txt
```

*The visualization and report filenames shown above represent the intended outputs from the organized analysis script.*

## 📦 Installation and Setup

### Step 1: Clone the Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### Step 2: Navigate to the Project Folder

```bash
cd "EDA Book Sales"
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Analysis

```bash
python src/eds_analysis.py
```

**Note:** Ensure that the dataset is available in the `Data` folder and that the path in your Python script matches the actual folder name.

## 📋 Requirements

The `requirements.txt` file should contain:

```text
numpy
pandas
matplotlib
seaborn
```

## 💡 Expected Outcomes

- Better understanding of book sales data and its structure.
- Identification of missing values and duplicate records.
- Understanding of book genre and language distributions.
- Exploration of book ratings and author performance.
- Analysis of sales patterns and publisher revenue.
- Visual representation of important data relationships.
- Improved practical knowledge of Python-based exploratory data analysis.

## 🚀 Future Improvements

- Build an interactive dashboard using Power BI or Streamlit.
- Perform deeper statistical analysis of book sales.
- Investigate factors associated with higher book sales.
- Develop a machine learning model to predict sales, if the dataset supports it.
- Automate the generation of EDA reports.

## 👨‍💻 Skills Demonstrated

Python | Pandas | NumPy | Data Cleaning | Exploratory Data Analysis | Data Visualization | Statistical Analysis | Matplotlib | Seaborn

## 🏁 Conclusion

This project demonstrates an end-to-end exploratory analysis of book sales data using Python. It covers data inspection, data quality checks, statistical summaries, grouping and aggregation, and visualization.

The analysis provides a foundation for understanding publishing patterns, book ratings, author performance, and sales trends, while developing practical skills relevant to entry-level Data Analyst and Data Science roles.

---

