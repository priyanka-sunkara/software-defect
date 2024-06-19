import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the dataset
data = pd.read_csv('C:\\Users\\Priyanka\\OneDrive\\Desktop\\cm1.csv')
df = pd.DataFrame(data)

# Define features and labels
X = df[['loc', 'v(g)', 'ev(g)', 'iv(g)', 'n', 'v', 'l', 'd', 'i', 'e', 'b', 't', 'lOCode', 'lOComment', 'lOBlank', 'locCodeAndComment', 'uniq_Op', 'uniq_Opnd', 'total_Op', 'total_Opnd', 'branchCount']]
y = df['defects']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Feature-dependent Naive Bayes approach
class FeatureDependentNaiveBayes:
    def __init__(self):
        self.class_probs = {}
        self.feature_probs = {}

    def fit(self, X, y):
        n_samples, n_features = X.shape
        self.classes = np.unique(y)

        for cls in self.classes:
            X_c = X[y == cls]
            self.class_probs[cls] = len(X_c) / n_samples
            self.feature_probs[cls] = {
                'mean': X_c.mean(axis=0),
                'var': X_c.var(axis=0)
            }

    def _calculate_likelihood(self, mean, var, x):
        eps = 1e-6  # to prevent division by zero
        coeff = 1.0 / np.sqrt(2.0 * np.pi * var + eps)
        exponent = np.exp(-((x - mean) ** 2) / (2 * var + eps))
        return coeff * exponent

    def _calculate_posterior(self, x):
        posteriors = []

        for cls in self.classes:
            prior = np.log(self.class_probs[cls])
            class_conditional = np.sum(
                np.log(self._calculate_likelihood(self.feature_probs[cls]['mean'], self.feature_probs[cls]['var'], x))
            )
            posterior = prior + class_conditional
            posteriors.append(posterior)

        return self.classes[np.argmax(posteriors)]

    def predict(self, X):
        y_pred = [self._calculate_posterior(x) for x in X]
        return np.array(y_pred)

# Initialize and train the model
fdnb = FeatureDependentNaiveBayes()
fdnb.fit(X_train.values, y_train.values)

# Make predictions
predictions = fdnb.predict(X_test.values)

# Evaluate the classifier
accuracy = accuracy_score(y_test, predictions)
print(f"Accuracy: {accuracy}")

# Visualize the results
plt.scatter(range(len(y_test)), y_test, label='Actual', color='blue', marker='x')
plt.scatter(range(len(predictions)), predictions, label='Predicted', color='red', marker='o')
plt.legend()
plt.xlabel('Sample Index')
plt.ylabel('Defective')
plt.title('Actual vs. Predicted Defective Labels')
plt.show()

