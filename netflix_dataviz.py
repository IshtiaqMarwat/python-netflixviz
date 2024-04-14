#!/usr/bin/env python
# coding: utf-8

# # Netflix Data Analysis and Visualization

# This repository contains Python code for analyzing and visualizing Netflix data using the pandas, matplotlib, seaborn, and plotly libraries. The code performs data inspection, handles missing values, and creates visualizations to gain insights into various aspects of the Netflix dataset.
# 
# Details:
# Data Inspection:
# 
# Loads the Netflix dataset from a CSV file.
# Displays the first and last 5 rows of the dataset.
# Provides information about the shape and columns of the dataset.
# Shows descriptive statistics of numerical columns.
# Counts null values in different columns.
# Displays the impact of null values on the dataset.
# Lists top directors, movie vs TV show count, ratings, top countries, release years, and top genres.
# Handling Missing Values:
# 
# Drops rows with missing values in the "rating", "duration", and "date_added" columns.
# Replaces missing values in the "country", "cast", and "director" columns with appropriate values.
# Visualization:
# 
# Displays the top 10 actors based on the number of titles they appear in.
# Plots the distribution of movie durations and TV show seasons.
# Visualizes the monthly additions of content over the years using a heatmap.

# In[ ]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import re
import plotly.express as px
import plotly.graph_objs as go
import plotly.figure_factory as ff

warnings.filterwarnings('ignore')
plt.style.use('seaborn-darkgrid')

# Load Netflix data
df = pd.read_csv(r"path\to\netflix_titles.csv")

# Inspecting Data
print("First 5 rows of data:")
print(df.head())

print("\nLast 5 rows of data:")
print(df.tail())

print("\nShape of data:")
print(df.shape)

print("\nColumns in the data:")
print(df.columns)

print("\nInformation about the data:")
print(df.info())

print("\nDescriptive statistics of numerical data:")
print(df.describe())

print("\nCount of null values in different columns:")
print(df.isnull().sum().sort_values(ascending=False))

print("\nImpact of null values on the column/data (%):")
print(round(df.isnull().sum() / df.shape[0] * 100, 2).sort_values(ascending=False))

print("\nTop 10 directors by count:")
print(df["director"].value_counts().head(10))

print("\nCount of movies vs TV shows:")
print(df["type"].value_counts())

print("\nCount of ratings:")
print(df["rating"].value_counts())

print("\nTop 10 countries by count:")
print(df["country"].value_counts().head(10))

print("\nTop 15 release years by count:")
print(df["release_year"].value_counts().head(15))

print("\nTop 15 genres by count:")
print(df["listed_in"].value_counts().head(15))

# Handling Missing Values
print("\nHandling Missing Values:")
print("Before handling missing values:")
print(round(df.isnull().sum() / df.shape[0] * 100, 2).sort_values(ascending=False))

df.dropna(subset=["rating", "duration"], axis=0, inplace=True)
df.dropna(subset=["date_added"], axis=0, inplace=True)

df["country"].replace(np.NaN, "Unknown", inplace=True)
df["cast"].replace(np.NaN, "No Cast", inplace=True)
df["director"].replace(np.NaN, "No Director", inplace=True)

print("After handling missing values:")
print(round(df.isnull().sum() / df.shape[0] * 100, 2).sort_values(ascending=False))

# Visualization
print("\nVisualization:")
print("Top 10 actor movies based on the number of titles:")
cast_shows = df[df["cast"] != "No Cast"].set_index("title")["cast"].str.split(', ', expand=True).stack().reset_index(level=1, drop=True)
plt.figure(figsize=(13, 7))
sns.countplot(y=cast_shows, order=cast_shows.value_counts().index[:10], palette='pastel')
plt.show()

print("\nDistribution of movie durations:")
plt.figure(figsize=(10, 6))
sns.histplot(df.loc[df["type"] == "Movie", "duration"], bins=30, kde=True, color='skyblue')
plt.title("Distribution of Movie Durations")
plt.xlabel("Duration (Minutes)")
plt.ylabel("Frequency")
plt.show()

print("\nDistribution of TV show durations:")
plt.figure(figsize=(10, 6))
sns.histplot(df.loc[df["type"] == "TV Show", "duration"], bins=15, kde=True, color='salmon')
plt.title("Distribution of TV Show Durations")
plt.xlabel("Seasons")
plt.ylabel("Frequency")
plt.show()

# Monthly additions of content over the years
netflix_date = df[["date_added"]].dropna()
netflix_date["year"] = netflix_date["date_added"].apply(lambda x: x.split(', ')[-1])
netflix_date["month"] = netflix_date["date_added"].apply(lambda x: x.lstrip().split(' ')[0])

month_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
new_df = netflix_date.groupby('year')['month'].value_counts().unstack().fillna(0)[month_order]

plt.figure(figsize=(10, 7), dpi=200)
heatmap = plt.pcolor(new_df, cmap="Greens", edgecolors="white", linewidths=2)
plt.xticks(np.arange(0.5, len(new_df.columns), 1), new_df.columns, rotation=45)
plt.yticks(np.arange(0.5, len(new_df.index), 1), new_df.index)
plt.colorbar(heatmap)
plt.title("Monthly Additions of Content Over the Years")
plt.xlabel("Month")
plt.ylabel("Year")
plt.show()

