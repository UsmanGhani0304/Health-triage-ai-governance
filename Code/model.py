import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('/sythetic_dataset.csv')  #for colabs use this, if you're using it on local machine use "../dataset/sythetic_dataset.csv"

X = df.drop('urgency_label', axis=1)
y = df['urgency_label']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

preprocessor = ColumnTransformer(
    transformers=[('cat', OneHotEncoder(handle_unknown='ignore'), ['age_group', 'gender', 'symptom_1', 'symptom_2', 'fever_yes_no', 'chest_pain_yes_no'])],
    remainder='passthrough')

model = Pipeline(steps=[('preprocess', preprocessor),
                        ('classifier', DecisionTreeClassifier(random_state=42))])

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))

test_data = pd.DataFrame([
    ['Adult', 'Male', 'chest_pain', 'none', 1, 'no', 'yes'],
    ['Child', 'Female', 'fever', 'cough', 2, 'yes', 'no'],
    ['Elderly', 'Female', 'back_pain', 'fever', 5, 'yes', 'no'],
    ['Infant', 'Female', 'fever', 'none', 1, 'yes', 'no'],
    ['Adult', 'Male', 'broken_arm', 'unconscious', 1, 'no', 'no']
], columns=['age_group', 'gender', 'symptom_1', 'symptom_2', 'duration', 'fever_yes_no', 'chest_pain_yes_no'])

print("Test Predictions:", model.predict(test_data))
