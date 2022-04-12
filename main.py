
from flask import Flask, render_template, request, redirect, url_for

def calc_bmi(height, weight):
    weight = weight * 0.45
    height = height * 0.025
    height = height * height
    return round((weight/height), 1)

def calc_category(bmi):
    if bmi < 18.5:
        return "Underweight"  
    elif bmi >= 18.5 and bmi < 25: 
        return "Normal Weight"
    elif bmi >= 25 and bmi < 30: 
        return "Overweight"
    elif bmi >= 30: 
        return "Obese"





app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def home():

    bmi = 0
    category = "none"

    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])


        bmi = calc_bmi(height, weight)


        category = calc_category(bmi)
        
        

    return render_template("index.html", bmi=bmi, category=category)



if __name__ == "__main__":
    app.run()




