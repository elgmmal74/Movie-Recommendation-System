# 🎬 Movie Recommendation System - Content-Based  

## 📌 Project Description  
This **Movie Recommendation System** is based on **content-based filtering**, where movies are recommended based on their descriptions. The system analyzes the textual content of movies to find similarities and suggest relevant recommendations to users.  

## 🚀 Technologies Used  
- **Flask** - Web framework for building the application.  
- **Pandas** - For data manipulation and analysis.  
- **Scikit-learn** - Used for **TF-IDF Vectorization** and similarity computation.  
- **Joblib** - For saving and loading the trained model efficiently.  

## 🎯 How It Works  
1. **TF-IDF Vectorizer** extracts text features from movie descriptions.  
2. **Sigmoid Kernel** is used to compute similarity between movies.  
3. When a user enters a movie name, the system finds and suggests the most similar movies.
