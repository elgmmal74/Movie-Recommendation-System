from flask import Flask, render_template, request
import joblib

# Load the models and data
sig = joblib.load('models/sig_matrix.pkl')
tfv = joblib.load('models/tfv_vectorizer.pkl')
indices = joblib.load('models/indices.pkl')
movies_cleaned = joblib.load('models/movies_cleaned.pkl')

# Recommendation function
def give_recommendations(title, sig=sig):
    try:
        # Get the index corresponding to the movie title
        idx = indices[title]

        # Get the pairwise similarity scores
        sig_scores = list(enumerate(sig[idx]))

        # Sort the movies based on similarity scores
        sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

        # Get the scores of the 10 most similar movies (excluding the movie itself)
        sig_scores = sig_scores[1:11]

        # Get the movie indices
        movie_indices = [i[0] for i in sig_scores]

        # Return the top 10 most similar movies
        return movies_cleaned['original_title'].iloc[movie_indices].tolist()  # Convert to list
    except KeyError:
        # Handle the case where the movie title is not found
        return ["Movie not found. Please try another title."]

# Create Flask app
app = Flask(__name__)

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = []
    if request.method == 'POST':
        movie_title = request.form['movie_title']
        recommendations = give_recommendations(movie_title)
    return render_template('index.html', recommendations=recommendations)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)