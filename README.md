# Book Recommendation System

## Overview
This project implements a book recommendation system using two approaches:
1. **Popularity- Based Recommender System**: Recommends books based on their popularity and average rating.
2. **Collaborative Filtering- Based Recommender System**: Recommends books based on user similarity and book similarity.

The project uses Python for data processing and recommendation algorithms, and Flask for creating a web interface to interact with the recommendation system.

## Requirements
To run this project, ensure you have the following Python libraries installed:

```
pip install numpy pandas scikit- learn flask pickle- mixin
```
## Dataset

The project uses the following CSV files:

- books.csv: Contains book information, including ISBN, Book- Title, Book- Author, and Image- URL- M.
- users.csv: Contains user information.
- ratings.csv: Contains ratings given by users to books, including User- ID, ISBN, and Book- Rating.

## Data Preprocessing

1.	Loading Data: Read the datasets using pandas and inspect them.
2.	Checking Data Quality:
- Check for missing values and duplicates in each dataset.

## Recommendation Systems

### Popularity- Based Recommender System

1.	Merge Datasets: Merge ratings and books datasets on the ISBN column.
2.	Calculate Popularity Metrics:
- Compute the number of ratings for each book.
- Compute the average rating for each book.
3.	Filter and Sort:
- Filter books with a minimum number of ratings.
- Sort by average rating to get the top books.
4.	Save Data: Save the results into a pickle file popular.pkl.

### Collaborative Filtering- Based Recommender System

1.	Filter Users and Books:
- Identify users who have rated more than 200 books.
- Identify books with more than 50 ratings.
2.	Create User- Book Rating Matrix:
- Create a pivot table with books as rows and users as columns.
3.	Calculate Similarity Scores:
- Use cosine similarity to compute similarity scores between books.
4.	Recommendation Function:
- Define a function to recommend books similar to a given book.
5.	Save Data:
- Save the pivot table, book data, and similarity scores into pickle files: pt.pkl, books.pkl, and similarity_scores.pkl.

## Web Application

The Flask application provides a web interface for interacting with the recommendation system.

1.	Endpoints:
- /: Displays popular books.
- /recommend: Displays the recommendation input form.
- /recommend_books: Processes user input and displays recommended books.
2.	Templates:
- index.html: Shows a list of popular books with their details.
- recommend.html: Allows users to input a book name and view recommendations.

## How to Run

1.	Ensure all required packages are installed.
2.	Run the Flask application:

```
python app.py
```
Access the application:
- Open your web browser and go to http://127.0.0.1:5000/ to view the popular books.
- Navigate to /recommend to input a book name and get recommendations.

## Results

- Popularity- Based Recommendations: Provides the top 50 books based on average rating and number of ratings.
- Collaborative Filtering Recommendations: Provides books similar to a user- provided book based on collaborative filtering.


# Movie Recommendation System

## Overview
This project implements a movie recommendation system using content- based filtering. The system recommends movies based on their similarities in genres, keywords, cast, and crew.

## Dataset
The project uses the following CSV files:
-  `tmdb_5000_movies.csv`: Contains movie information such as `id`, `title`, `overview`, `genres`, `keywords`, `cast`, and `crew`.
-  `tmdb_5000_credits.csv`: Contains movie credits information such as `title`, `cast`, and `crew`.

## Requirements
To run this project, ensure you have the following Python libraries installed:

```
pip install numpy pandas scikit- learn nltk
```

## Data Preprocessing

1.	Load Data: Read the datasets using pandas.
2.	Merge Datasets: Merge tmdb_5000_movies and tmdb_5000_credits on the title column.
3.	Drop Unwanted Columns: Retain only the necessary columns: id, title, overview, genres, keywords, cast, and crew.
4.	Handle Missing Values: Drop rows with missing values and duplicates.
5.	Process Text Data:
- Genres: Convert genre objects into a list of genre names.
- Keywords: Convert keyword objects into a list of keyword names.
- Cast: Extract the top 3 actors from the cast.
- Crew: Extract the director from the crew.
- Overview: Split the overview into individual words.
6.	Combine Data: Create a tags column by combining overview, crew, cast, and genres.

## Feature Extraction

1.	Text Preprocessing:
- Convert all text to lowercase.
- Use CountVectorizer to convert text data into numerical features.
2.	Stemming: Apply stemming to reduce words to their root forms.

## Recommendation System

1.	Calculate Similarities:
- Compute cosine similarity between movies based on their tags.
2.	Recommendation Function:
- Define a function recommending that takes a movie title as input and returns the top 5 similar movies based on cosine similarity.

## Serialization

1.	Save Data:
- Save the processed movie data and similarity matrix using pickle for later use.

## How to Run

1.	Ensure all required packages are installed.
2.	Execute the code:
- Run the script to preprocess data, compute similarities, and make recommendations.
3.	Check Recommendations:
- Use the recommending function to get movie recommendations. Example:

```
recommending("Spider- Man 3")
```

```
#Recommend movies similar to "Spider- Man 3
recommending("Spider- Man 3")

# Recommend movies similar to "The Dark Knight Rises"
recommending("The Dark Knight Rises")
```
