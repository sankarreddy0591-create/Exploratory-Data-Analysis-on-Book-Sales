
# project : EXPLORATORY DATA ANALYSIS - BOOK SALES


# import required libaries

import os
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

# load dataset into a pandas
df=pd.read_csv(r"F:\DS & DA Projects\real-time projects\EDA Book Sales\Data\Books_Data_Clean.csv")
print("========== Dataset Loaded Successful============", df)
print("Dataset Shape:", df.shape)

#  set project path

base_dir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

output_dir=os.path.join(base_dir, "Visualization")
os.makedirs(output_dir, exist_ok=True)
sns.set_theme(style="whitegrid")

# display the first five records in the df
print("========= First Five Records ==========:", df.head())

# display the last five records in the df
print("========= First last Records ==========:", df.tail())

# display the dataset information
print("========= DataSet Information ==========:", df.info())

# display the dataset Statistical summary
print("========= DataSet  Statistical summary ==========:", df.describe().T)

#  display the dataset columns
print("========= DataSet  columns ==========:", df.columns.tolist())

# keep books published after 1900
df=df[df["Publishing Year"]>1900]
print("==========keep books published after 1900========:", df)

# checking missing values
print("========missing values before cleaning========:", df.isna().sum())

# remove records with missing books names
df=df.dropna(subset=['Book Name'])
print("==========missing values after clening========:", df.isna().sum())

# check duplicates records
print("=========duplicate rows==========:",df.duplicated().sum())

# check unique values
print("========Unique values per columns==========:",df.nunique() )

# publishining year distribution

plt.hist(df['Publishing Year'], bins=20)

plt.xlabel("Piblishing Year")
plt.ylabel("Frequency")
plt.title("Distribution of Publishing Year")
plt.show()
plt.close()
print("======Distribution of Publishing Yea========:",plt.hist(df['Publishing Year'], bins=20) )

# analysis book genre
df['genre'].value_counts().plot(kind="bar")
plt.xlabel("Genre")
plt.ylabel("Number of Books")
plt.title("Number of Book In Each Genre")
plt.show()
plt.close()
print("===========Number of Book In Each Genre=========:", plt.plot(df['genre'].value_counts()))

# compare average ratings across genre

plt.figure(figsize=(10,5))
sns.boxplot(
    x="genre",
    y="Book_average_rating",
    data=df
)
plt.xlabel("Genre")
plt.ylabel("Average Book Ratings")
plt.title("Book Ratings Distribution by Genre")
plt.show()
plt.close()
print("========Book Ratings Distribution by Genre=========: ",sns.boxplot(
    x="genre",
    y="Book_average_rating",
    data=df
) )

