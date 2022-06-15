# import pickle
#
# model = pickle.load(open('model.pkl', 'rb'))
# print(float(model.predict([[1000	,0,	0.3048,	71.3,	0.00266337]])))

p = {
    "data": {
        "Frequency": 9,
        "Angle of Attack": 8,
        "Chord Length": 10,
        "Velocity": 1,
        "Suction Side": 7
    }
}
# s = p.
# s.mapping
# print(list(p['data'].values()))

# import pickle
#
# model = pickle.load(open('model.pkl', 'rb'))
# pickle.dump(model, open('test.pkl', 'wb'))
# pickle.dump(model, open('model.pkl', 'wb'))
#
# model = pickle.load(open('scaler.pkl', 'rb'))
# pickle.dump(model, open('scaler.pkl', 'wb'))