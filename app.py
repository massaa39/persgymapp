"""
A web application for generating advice based on user input.
"""

import csv
from flask import Flask, render_template, request, redirect, url_for
from advice_generator import create_advice

app = Flask(__name__)

def save_to_csv(data):
    """
    Saves data to a CSV file.
    """
    with open("members.csv", "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(data.values())

@app.route("/")
def index():
    """
    Renders the index page.
    """
    return render_template("index.html")

@app.route("/sinform")
def sinform():
    """
    Renders the form page.
    """
    return render_template("sinform.html")

@app.route("/submit-form", methods=["POST"])
def submit_form():
    """
    Handles form submission.
    """
    form_data = {
        "membership_number": request.form.get("membership_number"),
        "name": request.form.get("name"),
        "age": request.form.get("age"),
        "gender": request.form.get("gender"),
        "height": request.form.get("height"),
        "weight": request.form.get("weight"),
        "medical_conditions": request.form.getlist("medical_conditions[]"),
        "other_condition": request.form.get("other_condition"),
        "beauty_goals": request.form.get("beauty_goals"),
        "training_goals": request.form.get("training_goals"),
        "preferred_seniority": request.form.get("preferred_seniority"),
        "communication_method": request.form.get("communication_method"),
        "phone_number": request.form.get("phone_number"),
        "email": request.form.get("email"),
        "emergency_contact": request.form.get("emergency_contact"),
        "how_did_you_hear": request.form.get("how_did_you_hear"),
        "medical_history": request.form.get("medical_history")
    }

    save_to_csv(form_data)

    advice = create_advice(form_data["age"], form_data["beauty_goals"], form_data["preferred_seniority"], form_data["medical_history"], form_data["training_goals"], form_data["medical_conditions"])
    advice = advice.replace(" ", "%20")
    return redirect(url_for("show_advice", name=form_data["name"], advice=advice))

@app.route("/show_advice/<name>/<advice>")
def show_advice(name, advice):
    """
    Displays generated advice.
    """
    advice = advice.replace("%20", " ")
    return render_template("advice.html", name=name, advice=advice)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")