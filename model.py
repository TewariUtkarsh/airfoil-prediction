import pandas as pd
import numpy as np
import pickle
from sklearn.metrics import r2_score
from DBOperations import MySQL


class ModelOperations:

    def __init__(self, user_input):
        self.data = user_input
        self.model = None
        self.validation_data = None
        self.x_test = None
        self.y_test = None
        self.y_pred = None
        self.prediction = None
        self.r2 = None
        self.adj_r2 = None


    def Standardize(self):
        scaler = pickle.load(open('scaler.pkl', 'rb'))
        self.data = scaler.transform([self.data])


    def Load_model(self):
        self.model = pickle.load(open('model.pkl', 'rb'))


    def Predict(self):
        # print(self.data[0][0])
        self.prediction = self.model.predict(self.data)
        return self.prediction[0]


    def get_r2_score(self):
        self.r2 = r2_score(self.y_test, self.y_pred)


    def get_adj_r2_score(self):
        n = self.x_test.shape[0]
        p = self.x_test.shape[1]

        self.adj_r2 = 1 - ((1-self.r2)*(n-1)/(n-p-1))


    def getAccurcay(self):
        self.get_r2_score()
        self.get_adj_r2_score()
        return self.r2, self.adj_r2


    def BulkPredict(self):
        db = MySQL()
        db.initConnection()
        db.initCursor()
        # db.createDB()
        db.createTable()
        db.dumpData()
        scaler = pickle.load(open('scaler.pkl', 'rb'))

        self.validation_data = db.loadData()
        self.x_test = self.validation_data.drop(axis=1, columns='Scaled_Sound')
        self.y_test = self.validation_data['Scaled_Sound']

        self.x_test = scaler.transform(self.x_test)

        self.y_pred = self.model.predict(self.x_test)
        # print(self.validation_data)

    def savePrediction(self):
        df = pd.DataFrame(self.x_test)
        df['Scaled_Sound'] = self.y_pred
        df.index = [i for i in range(1, 497)]
        df.to_html('Prediction.html')

