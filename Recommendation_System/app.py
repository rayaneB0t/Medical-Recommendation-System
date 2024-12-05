from flask import Flask, render_template, request
import numpy as np

app = Flask(__name__)

# Example symptoms and diseases mapping (simplified)
symptoms_dict = {'itching': 0, 'skin_rash': 1, 'nodal_skin_eruptions': 2}
diseases_list = {0: 'Fungal infection', 1: 'Allergy', 2: 'GERD'}

# Dummy function to predict disease based on symptoms
def given_predicted_value(patient_symptoms):
    input_vector = np.zeros(len(symptoms_dict))
    for item in patient_symptoms:
        if item in symptoms_dict:
            input_vector[symptoms_dict[item]] = 1
    predicted_disease = diseases_list.get(np.argmax(input_vector), 'Unknown')
    return predicted_disease

@app.route("/", methods=["GET", "POST"])
def home():
    predicted_disease = None
    if request.method == "POST":
        symptoms = request.form["symptoms"]
        user_symptoms = [s.strip() for s in symptoms.split(',')]
        predicted_disease = given_predicted_value(user_symptoms)
    return render_template("index.html", predicted_disease=predicted_disease)

if __name__ == "__main__":
    app.run(debug=True)
