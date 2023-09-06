from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    if request.method == 'POST':
        if 'number1' in request.form and 'number2' in request.form:
            number1 = float(request.form['number1'])
            number2 = float(request.form['number2'])
            result = number1 + number2

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
