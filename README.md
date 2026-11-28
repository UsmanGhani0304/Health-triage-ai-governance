# Health Triage AI - Governance Project

This project suggests urgency Low / Medium / High from patient symptoms.
Final decision is always with the doctor.

This is an educational project. Not for clinical use. Synthetic data only. No real patient data.

## How It Works
Input -> Classifier -> Human Review -> Log

1. Input: age_group, gender, symptom_1, symptom_2, duration, fever_yes_no, chest_pain_yes_no
2. Classifier: Decision Tree Classifier suggests Low / Medium / High
3. Human Review: Every suggestion goes to doctor for approval
4. Log: Input, system suggestion, doctor final decision, and time are logged

Diagram is in 03-SDS/architecture.png

## Why Decision Tree and Not LLM?
Dataset is 200 rows, small tabular data. I needed a model I can explain.
LLM cannot explain why it said High. Decision Tree can.

## Results
Accuracy: 97.5% on synthetic data. 39 out of 40 test cases correct.
High Recall: 1.00, no High case missed.
Tested in Google Colab.

## Project Structure
01-BRD - Business problem
02-SRS - Requirements
03-SDS - Architecture and design
04-Model-Card - Model details
05-Risk-Assessment - Risks
06-Evaluation - Results
code/model.py - Model code
dataset/synthetic_dataset.csv - 200 rows synthetic dataset

## How To Run
1. Open Google Colab
2. Upload dataset/synthetic_dataset.csv
3. Open code/model.py and run it
4. Check accuracy and test predictions

## Governance
No diagnosis, no treatment, no prescription.
Every High case needs human review.
Only human-reviewed decisions are used for retraining.
