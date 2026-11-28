Educational/Portfolio: Synthetic data only, Not for clinical use.
Problem Statement:
A nurse at a clinic daily faces issue, regarding patient's priority(on which patient to be given priority), some have severe symptoms but don't get prioritized due to lack of patient's symptoms reading. Create an AI who can read the patient's symptoms and suggest the AI  based patient's priority(High/Medium/Low). AI is just there for suggesstions after patient's symptoms are entered with giving a brief description as to why he prioritized that patient. The main authority lies on doctors and nurse as to which patient is given priority with the decision, then each descision is stored inside the system for it's future training.

What will system do?
System will take input, i.e., Symptom 1, Symptom 2......Symptom n.
System will check the combination of symptoms or single symtom and then based on it, it will rank them high, medium or low.
The system will not diagnose patient neither will it treat or suggest medicines. It will not take patient's name as input and won't use patient's real data but will use synthetic data

Then the doctor will check it and then convey to nurse whether that patient should be called first or not and nurse will follow.

Note: Every decision passed via doctor will go ahead for model's training.
Golden Rule: The AI will only suggest, every decision will go through human(doctor)
