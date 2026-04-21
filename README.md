 Fake Job Detection System
1. Overview
Machine Learning-based web application designed to classify job advertisements as Real or Fake using Natural Language Processing (NLP).

2. Technical Implementation Steps
   
- Data Preprocessing & Cleaning
Tokenization: Breaking down job descriptions into individual words.

Stop-word Removal: Eliminating non-informative words (e.g., "is", "the", "at") to focus on key professional terminology.

Text Normalization: Converting text to lowercase and removing special characters/punctuation.

- Feature Extraction (Vectorization)
Implemented TF-IDF (Term Frequency-Inverse Document Frequency) to transform unstructured text data into numerical feature vectors.

This ensures that rare, highly descriptive words (which often indicate scams) carry more weight in the classification process.

- Model Training
Algorithm: Random Forest Classifier.

3. Project Structure
app.py: Web interface and logic.

final_rf_model.pkl: Trained ML model.

final_vectorizer.pkl: Text vectorizer.

requirements.txt: Necessary libraries.





