import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.naive_bayes import GaussianNB  # Assuming Gaussian Naive Bayes for simplicity

# Load the dataset (Allow user to upload their own CSV)
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(cm1.csv)
    st.write(data)  # Display the dataset

    # Define features and labels (You'll need to adjust this based on your dataset)
    X = data[['loc','v(g)','ev(g)','iv(g)','n','v','l','d','i','e','b','t','lOCode','lOComment','lOBlank','locCodeAndComment','uniq_Op','uniq_Opnd','total_Op','total_Opnd','branchCount','defects']]  # Replace with your actual features
    y = data['defects']  # Replace with your actual target column
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Initialize and train the model (Replace with your FeatureDependentNaiveBayes class)
    model = GaussianNB()
    model.fit(X_train, y_train)

    # Predictions (You can create an input form for new data to predict on)
    if st.button('Predict'):
        predictions = model.predict(X_test)
        accuracy = accuracy_score(y_test, predictions)
        st.write(f'Accuracy: {accuracy}')
        st.write(predictions)  # Display the predictions
