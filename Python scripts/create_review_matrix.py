import pandas as pd
import numpy as np
import os
import webbrowser

# Read the dataset into a data table using Pandas
ratings_data_table = pd.read_csv("Movie_Lens/ratings.csv")
del ratings_data_table['timestamp']

# Convert the running list of user ratings into a matrix using the 'pivot table' function
ratings_df = pd.pivot_table(ratings_data_table, index='userId', columns='movieId', aggfunc=np.max)

# Create a web page view of the data for easy viewing
html = ratings_df.to_html(na_rep="")

# Save the html to a temporary file
with open("html/review_matrix.html", "w") as f:
    f.write(html)

# Open the web page in our web browser
full_filename = os.path.abspath("review_matrix.html")
webbrowser.open("file://{}".format(full_filename))

# Create a csv file for review_matrix
ratings_df.to_csv("review_matrix.csv",na_rep="")
