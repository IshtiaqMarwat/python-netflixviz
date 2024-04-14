# Netflix Data Analysis and Visualization

This repository contains Python code for analyzing and visualizing Netflix data using the pandas, matplotlib, seaborn, and plotly libraries. The code performs data inspection, handles missing values, and creates visualizations to gain insights into various aspects of the Netflix dataset.

Details: Data Inspection:

Loads the Netflix dataset from a CSV file. Displays the first and last 5 rows of the dataset. Provides information about the shape and columns of the dataset. Shows descriptive statistics of numerical columns. Counts null values in different columns. Displays the impact of null values on the dataset. Lists top directors, movie vs TV show count, ratings, top countries, release years, and top genres. Handling Missing Values:

Drops rows with missing values in the "rating", "duration", and "date_added" columns. Replaces missing values in the "country", "cast", and "director" columns with appropriate values. Visualization:

Displays the top 10 actors based on the number of titles they appear in. Plots the distribution of movie durations and TV show seasons. Visualizes the monthly additions of content over the years using a heatmap.
