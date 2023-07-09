import pandas as pd
import pickle
import time
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.svm import SVC
from sklearn.tree import DecisionTreeClassifier

# Load data
data = pd.read_csv('../Data Collection/TrainingData.csv')

# Preprocess data
data.dropna(inplace=True)
#data['is_maintenance'] = data['Maintenance'].notnull().astype(int)
X = data[['RPM', 'Speed', 'Throttle Position', 'Coolant Temperature', 'Engine Load', 'Run Time']]
y = data['Output']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

start= time.time()
print("Start Time- in secs" ,(start))
# Train a KNN classifier
clf = KNeighborsClassifier(n_neighbors=5)
clf.fit(X_train, y_train)

# Make predictions on the test data and calculate accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
# Save the trained model to a pickle file
with open('./Models/KNNmodel.pkl', 'wb') as f:
    pickle.dump(clf, f)
stop= time.time()
print("Stop Time- in secs" ,(stop))
print("Elapse Time- in secs" ,(stop-start))

start= time.time()
print("Start Time- in secs" ,(start))
# Train a logistic regression classifier
clf = LogisticRegression(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test data and calculate accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
# Save the trained model to a pickle file
with open('./Models/LRmodel.pkl', 'wb') as f:
    pickle.dump(clf, f)
stop= time.time()
print("Stop Time- in secs" ,(stop))
print("Elapse Time- in secs" ,(stop-start))

start= time.time()
print("Start Time- in secs" ,(start))
# Train a decision tree classifier
clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test data and calculate accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
# Save the trained model to a pickle file
with open('./Models/DTmodel.pkl', 'wb') as f:
    pickle.dump(clf, f)
stop= time.time()
print("Stop Time- in secs" ,(stop))
print("Elapse Time- in secs" ,(stop-start))

start= time.time()
print("Start Time- in secs" ,(start))
# Train model
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Evaluate model
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
confusion_mat = confusion_matrix(y_test, y_pred)

print('Accuracy:', accuracy)
#print(X_test)
print('Confusion matrix:\n', confusion_mat)
# Save the trained model to a pickle file
with open('./Models/RFmodel.pkl', 'wb') as f:
    pickle.dump(clf, f)
stop= time.time()
print("Stop Time- in secs" ,(stop))
print("Elapse Time- in secs" ,(stop-start))

start= time.time()
print("Start Time- in secs" ,(start))
# Train a SVM classifier
clf = SVC(kernel='linear', C=1, random_state=42)
clf.fit(X_train, y_train)

# Make predictions on the test data and calculate accuracy
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)
# Save the trained model to a pickle file
with open('./Models/SVMmodel.pkl', 'wb') as f:
    pickle.dump(clf, f)
stop= time.time()
print("Stop Time- in secs" ,(stop))
print("Elapse Time- in secs" ,(stop-start))