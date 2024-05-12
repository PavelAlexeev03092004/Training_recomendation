X_test = [[2, 1, 3, 2, 2, 50, 5, 4, 1, 27, 2]]
from joblib import load
ridge_model = load('ridge_model.joblib')
predictions = ridge_model.predict(X_test)
print (predictions)