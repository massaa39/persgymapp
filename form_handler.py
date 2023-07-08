import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/advice', methods=['POST'])
def provide_advice():
    # フォームから入力された情報を取得する
    membership_number = request.form['membership-number']
    name = request.form['name']
    age = request.form['age']
    gender = request.form['gender']
    height = request.form['height']
    weight = request.form['weight']
    medical_history = request.form.getlist('medical-history')  # 持病に関する情報をリスト形式で取得する
    medical_condition = request.form['medical-condition']
    beauty_goals = request.form['beauty-goals']
    training_goals = request.form['training-goals']
    preferred_seniority = request.form['preferred-seniority']
    communication_method = request.form['communication-method']
    phone_number = request.form['phone-number']
    email = request.form['email']
    emergency_contact = request.form['emergency-contact']
    how_did_you_hear = request.form['how-did-youhear']

    # CSV ファイルにお客様情報を保存する
    with open('customer_data.csv', mode='a', newline='', encoding='utf-8') as f:
        fieldnames = ['membership_number', 'name', 'age', 'gender', 'height', 'weight', 'medical_history', 'medical_condition', 'beauty_goals', 'training_goals', 'preferred_seniority', 'communication_method', 'phone_number', 'email', 'emergency_contact', 'how_did_you_hear']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        writer.writerow({'membership_number': membership_number, 'name': name, 'age': age, 'gender': gender, 'height': height, 'weight': weight, 'medical_history': medical_history, 'medical_condition': medical_condition, 'beauty_goals': beauty_goals, 'training_goals': training_goals, 'preferred_seniority': preferred_seniority, 'communication_method': communication_method, 'phone_number': phone_number, 'email': email, 'emergency_contact': emergency_contact, 'how_did_you_hear': how_did_you_hear})
    
    # 持病に関するアドバイスを取得する
    advice = "運動前に必ず医師に相談し、適切な運動方法を選択してください。"
    condition_advice = {'高血圧': '有酸素運動と筋力トレーニングの両方が重要です。等張性運動を中心に取り入れ、過度な負荷を避けながら運動しましょう。また、心拍数を抑えた運動を行うことで、血圧を下げる効果が期待できます。',
    '糖尿病': '運動前にブドウ糖を摂取し、血糖値が安定してから、低～中負荷の有酸素運動と筋力トレーニングを行いましょう。運動後も、ブドウ糖を摂取して血糖値を正常範囲に戻してください。',
    "関節リウマチ": "関節に負担をかけない等尺性運動や等張性運動が適切です。筋力トレーニングによって筋肉を強化し、関節への負担を軽減できます。ただし、痛みがある場合は無理をしないように注意しましょう。",
    "人工関節または大腿骨の骨切り術後": "股関節の内転や内旋方向への動きは避け、軽い有酸素運動や筋力トレーニングが適切ですが、運動前に必ず医師と相談してください。",
    "腱板縫合手術歴がある": "肩関節外転90度以下の運動は避け、軽い有酸素運動や筋力トレーニングを中心に行いましょう。運動前に医師と相談して、適切な運動方法を選択してください。",
    "企図振戦": "筋力トレーニングが有効ですが、適切な負荷やトレーニング方法を医師と相談して決めてください。",
    "腰痛持ちの方": "軽い有酸素運動やストレッチから始め、負荷を徐々に増やしていくことが重要です。背骨筋力トレーニングによって腰周りの筋肉を強化し、腰痛の予防に役立ちます。運動中に腰に痛みが生じた場合は、すぐに運動を中止し、医師に相談してください。運動前にも医師の指導を仰ぎ、適切な運動方法を選択してください。",
    "関節リウマチ":"関節に負担をかけない等尺性運動や等張性運動が適切です。筋力トレーニングによって筋肉を強化し、関節への負担を軽減できます。ただし、痛みがある場合は無理をしないように注意しましょう。",
    "人工関節または大腿骨の骨切り術後":"股関節の内転や内旋方向への動きは避け、軽い有酸素運動や筋力トレーニングが適切ですが、運動前に必ず医師と相談してください。",
    "腱板縫合手術歴がある":"肩関節外転90度以下の運動は避け、軽い有酸素運動や筋力トレーニングを中心に行いましょう。運動前に医師と相談して、適切な運動方法を選択してください。",
    "企図振戦":"筋力トレーニングが有効ですが、適切な負荷やトレーニング方法を医師と相談して決めてください。",
    "慢性呼吸不全":"運動前にSpO2を測定し、低い場合は軽度に運動するようにしましょう。"} 

    for condition, advice_text in condition_advice.items():
        if condition in medical_history:
            advice += advice_text

    if medical_condition in condition_advice:
        advice += condition_advice[medical_condition]

    # 結果を HTML テンプレートに渡す
    return render_template('advice.html', name=name, advice=advice)

if __name__ == "__main__":
    app.run(debug=True)