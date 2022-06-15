from flask import Flask, jsonify, request, Response, render_template
from flask_cors import CORS, cross_origin
from model import ModelOperations
import numpy as np
import pickle

app = Flask(__name__)


@app.route("/", methods=['POST', 'GET'])
@cross_origin()
def index():
    return render_template('index.html')


@app.route("/predict", methods=['POST', 'GET'])
@cross_origin()
def predict():
    # data = request.json['data']

    # Returns a generator object
    data = request.form.values()

    # Accessing the values in the generator
    data = [i for i in data]

    # print(data)

    user_input = data

    m_oper = ModelOperations(user_input)

    m_oper.Standardize()

    m_oper.Load_model()

    prediction = m_oper.Predict()

    m_oper.BulkPredict()

    m_oper.savePrediction()

    r2, adj_r2 = m_oper.getAccurcay()

    # print(prediction, np.round(r2*100,2), np.round(adj_r2*100, 2))

    # return jsonify(prediction)
    return render_template('result.html', prediction=prediction, r2=np.round(r2*100,2), adj_r2=np.round(adj_r2*100, 2))


@app.route("/report", methods=['POST', 'GET'])
@cross_origin()
def report():
    return render_template('report.html')


@app.route('/bulk', methods=['POST', 'GET'])
@cross_origin()
def bulk():
    return render_template('Prediction.html')


if(__name__ == '__main__'):
    app.run(debug=True)