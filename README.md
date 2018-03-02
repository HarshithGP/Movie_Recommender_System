# Movie_Recommender_System
A movie recommendation system that uses collaborative filtering techniques to recommend a new movie by predicting the user's rating for that movie.

Developed a Movie Recommender System built from a model trained using collaborative filtering techniques.
- The ratings provided by existing users for various movies is extracted from the Movie Lens data set and stored as a sparse Ratings Matrix.
- This sparse Ratings matrix is factorized using the low rank matrix factorization algorithm to generate the attribute vectors for all users and movies in the data set. 
• The algorithm works by assigning random values to the user and movie attribute vectors and iteratively tweaks these values so as to minimize the cost associated with the difference between the known values of the Movie Ratings matrix and the current matrix.
• The final Ratings Matrix of predicted user ratings for all movies by each user is obtained by multiplying the final latent attribute vectors for users and movies that minimizes the cost function.
• New users are recommended movies filtered according to the highest average ratings provided by all existing users in the data set.
• Trained the model using the Movie Lens data set of Imdb movie reviews and achieved a root mean square error of less than 5% on the testing set.
