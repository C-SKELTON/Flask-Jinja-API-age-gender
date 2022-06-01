from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/guess/<name>')
def guess(name):
    age_end_point = f'https://api.agify.io?name={name}'
    age_response = requests.get(age_end_point)
    data = age_response.json()
    age = data['age']

    gender_end_point = f'https://api.genderize.io?name={name}'
    gender_response = requests.get(gender_end_point)
    data_ = gender_response.json()
    gender = data_['gender']

    return render_template("guess.html", name_ = name, age_ = age, gender_ = gender)


if __name__ == '__main__':
    app.run(debug=True)