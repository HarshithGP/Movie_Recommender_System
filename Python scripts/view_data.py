#Displays the first 100 rows of the movie ratings csv file as a html page

import pandas as pd
import webbrowser
import os

# Read the dataset into a data table using Pandas
ratings_data_table = pd.read_csv("Movie_Lens/ratings.csv")

# Create a web page view of the data for easy viewing
html = ratings_data_table[0:100].to_html()

# Save the html to a temporary file
with open("data.html", "w", encoding="utf8") as f:
    f.write(html)

# Open the web page in our web browser
full_filename = os.path.abspath("data.html")
webbrowser.open("file://{}".format(full_filename))

# Read the dataset into a data table using Pandas
movie_data_table = pd.read_csv("Movie_Lens/movies.csv", index_col="movieId")

# Create a web page view of the data for easy viewing
html = movie_data_table.to_html()

# Save the html to a temporary file
with open("movie_list.html", "w", encoding="utf8" ) as f:
    f.write(html)

# Open the web page in our web browser
full_filename = os.path.abspath("movie_list.html")
webbrowser.open("file://{}".format(full_filename))