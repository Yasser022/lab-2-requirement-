from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    age = request.form['age']
    
    # Process the form data (in this case, just pass it to the result page)
    return render_template('result.html', name=name, age=age)

if __name__ == '__main__':
    app.run(debug=True)
