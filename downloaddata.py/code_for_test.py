from sklearn.metrics import classification_report, accuracy_score
predictions = model.predict(X_test_vec)
print("Accuracy:", accuracy_score(y_test, predictions))
print(classification_report(y_test, predictions))