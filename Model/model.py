import numpy as np
import pandas as pd
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline
import joblib  # for saving the model

# Load the data
data = pd.read_csv('E:\Qafza\Spam\Model\DataSet\spam.csv')
# Create a new column to indicate if the email is spam or not
data['Spam'] = data['Category'].apply(lambda x: 1 if x == 'spam' else 0)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(data.Message, data.Spam, test_size=0.25, random_state=42)

# Create a model using a Pipeline
clf = Pipeline([
    ('vectorizer', CountVectorizer()),  # Convert text to matrix form
    ('nb', MultinomialNB())  # Naive Bayes model
])

# Train the model
clf.fit(X_train, y_train)

# Save the model
joblib.dump(clf,'spam_classifier.joblib')