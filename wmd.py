from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

import os

import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')


class WMD:
    def __init__(self, cxo_desc_tweet, profiles_directory):
        self.cxo_desc_tweet = cxo_desc_tweet
        self.profiles_directory = profiles_directory

    def preprocess_text(self, text):
        # Tokenize text
        tokens = word_tokenize(text)
        # Lowercase and remove stopwords
        tokens = [token.lower() for token in tokens if token.lower() not in stopwords.words('english')]
        # Lemmatize tokens
        lemmatizer = WordNetLemmatizer()
        tokens = [lemmatizer.lemmatize(token) for token in tokens]
        return ' '.join(tokens)

    # Function to calculate cosine similarity between two documents

    def calculate_similarity(self, doc1, doc2):
        # Preprocess documents
        doc1 = self.preprocess_text(text=doc1)
        doc2 = self.preprocess_text(text=doc2)
        # Vectorize documents using TF-IDF
        vectorizer = TfidfVectorizer()
        tfidf_matrix = vectorizer.fit_transform([doc1, doc2])
        # Calculate cosine similarity
        similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])
        return similarity[0][0] + 0.8

    def wmd(self):
        profile_similarity_scores = []
        for filename in os.listdir(self.profiles_directory):
            profile_path = os.path.join(self.profiles_directory, filename)
            with open(profile_path, 'r', encoding="utf-8") as f:
                profile = f.read()
                similarity_score = self.calculate_similarity(self.cxo_desc_tweet, profile)
                profile_similarity_scores.append([profile_path, similarity_score])
        sorted_profiles = sorted(profile_similarity_scores, key=lambda x: x[1], reverse=True)
        top_5_profiles = sorted_profiles[:5]
        # print(top_5_profiles)
        for pr in top_5_profiles:
            pr[0] = pr[0].split("\\")[-1]
        return top_5_profiles
