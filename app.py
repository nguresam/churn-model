from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load the churn model
model = joblib.load('CRAG CHURN MODEL')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Retrieve user input from the form
        p1 = int(request.form['p1'])
        p2 = int(request.form['p2'])
        p3 = int(request.form['p3'])
        p4 = float(request.form['p4'])
        p5 = int(request.form['p5'])
        p6 = int(request.form['p6'])
        p7 = int(request.form['p7'])
        p8 = float(request.form['p8'])
        p9 = int(request.form['p9'])
        if p9 == 1:
            Geography_Germany = 1
            Geography_Spain = 0
            Geography_France = 0
        elif p9 == 2:
            Geography_Germany = 0
            Geography_Spain = 1
            Geography_France = 0
        elif p9 == 3:
            Geography_Germany = 0
            Geography_Spain = 0
            Geography_France = 1
        p10 = int(request.form['p10'])

        result = model.predict([[p1, p2, p3, p4, p5, p6, p7, p8, Geography_Germany, Geography_Spain, p10]])

        if result == 0:
            prediction = "No Exit"
        else:
            prediction = "Exit"

        return render_template('index.html', prediction=prediction)
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)




