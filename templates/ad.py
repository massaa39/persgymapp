from flask import Flask, render_template, request
from advice_generator import generate_advice

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form.to_dict()
        age = int(request.form['age'])
        beauty_goals = request.form['beauty_goals']
        preferred_seniority = request.form['preferred_seniority']
        medical_history = request.form.get('medical_history', '')
        training_goals = request.form['training_goals']
        medical_conditions = request.form.getlist('medical_conditions[]')

        advice = generate_advice(age, beauty_goals, preferred_seniority, medical_history, training_goals, medical_conditions)

        name = data["name"]

        return render_template('advice.html', name=name, advice=advice)
    else:
        return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)
