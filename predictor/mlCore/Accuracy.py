from sklearn.metrics import accuracy_score

def get_score(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)   
    print(f"Model Accuracy: {accuracy}")
        