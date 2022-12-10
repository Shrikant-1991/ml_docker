from flask import Flask, render_template, request
import numpy as np
import pickle

model = pickle.load(open('iris_model.pkl', 'rb'))

#this was first chage in the master branch
app = Flask(__name__)


@app.route('/')
def man():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def home():
    sepal_length = eval(request.form['sepal_length'])
    sepal_width = eval(request.form['sepal_width'])
    petal_length = eval(request.form['petal_length'])
    petal_width = eval(request.form['petal_width'])
    
    array =np.array([[sepal_length,sepal_width,petal_length,petal_width]]).reshape(1,-1)

    pred = model.predict(array)
    return render_template('after.html', data=pred)


if __name__ == "__main__":
    app.run(host='0.0.0.0',debug=False)   

# @app.route('/predict1')
# def predict1():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     c = int(request.args.get('c'))
#     d = int(request.args.get('d'))

#     arr = np.array([[a, b, c, d]])
#     pred = model.predict(arr)
#     return render_template('after.html', data=pred)
