# Cinematch

Cinematch is a movie recommendation system that helps users find similar movies based on their preferences. By leveraging data from TMDB, Cinematch provides personalized movie recommendations using cosine similarity on movie tags.

## Live Demo

You can access the live demo of Cinematch [here](http://your-demo-url.com).

## Features

- Fetches data for 10,000 movies from the TMDB API
- Creates tags for each movie based on description, genres, actors, and more
- Converts tags into vectors using sklearn
- Computes cosine similarity to find the top 12 most similar movies for each movie
- Stores data of the top 12 most similar movies in a pickle file
- User-friendly frontend created with Streamlit
- Allows users to select any movie from the dataset and get recommendations for similar movies

## Project Structure

- `Data/`: Contains the CSV file with the extracted movie data.
- `Notebooks/`: Jupyter notebooks used for data processing and model development.
- `__pycache__/`: Python cache files.
- `app.py`: Streamlit app for the frontend.
- `helper.py`: Helper functions for data processing and recommendation generation.
- `similarity.pkl`: Pickle file containing the similarity data.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/SudarshanPoudel/Movie_recommandation.git
   cd Movie_recommandation
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```


## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
