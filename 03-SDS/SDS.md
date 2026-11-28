<img width="812" height="1600" alt="SDS" src="https://github.com/user-attachments/assets/c9e7b4d1-977e-429c-a077-bd8e92f4dd04" />
**Architecture:**
The system architecture goes with inputting the age_group, gender, duration and symptoms(symptom 1 and symptom 2), upon entering them, the system will tell whether the patient is in High/Medium/Low priority. The final decision lies by doctor as if they accepts the decision the answer then log into the model helping it in human reviewed retraining.

**Model:**
Tree classifier is used in it as dataset is small limited to 200 entries and tree is explainable and fits within the requirements of the system well.

**Logs:**
Every suggestion will go to doctor for their approval, once it is approved/reject it will go to the system's record where it will be used for training the model.

