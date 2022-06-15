import mysql.connector as connection
import sqlite3
import pickle
import json
import pandas as pd

class MySQL:

    def __init__(self):
        self.conn = None
        self.curr = None
        self.validation_data = None
        self.user_data = None


    def getUserData(self):
        user_data = json.load(open('userdata.json', 'r'))
        self.user_data = list(list(user_data.values())[0].values())

    def initConnection(self):
        self.getUserData()
        self.conn = sqlite3.connect(database=f"{self.user_data[1]}.db")


    def initCursor(self):
        self.curr = self.conn.cursor()


    def createDB(self):
        self.curr.execute(f"create database {self.user_data[1]};")


    def createTable(self):
        # self.curr.execute(f"use {self.user_data[1]};")
        columns = self.user_data[5]
        self.curr.execute(f"create table {self.user_data[4]}({columns[0]} float, {columns[1]} float, {columns[2]} float, "
                          f"{columns[3]} float, {columns[4]} float, {columns[5]} float);")


    def dumpData(self):
        df = pd.read_csv('Validation_Data.csv', index_col=[0])
        for i in range(df.shape[0]):
            data = df.iloc[i]
            self.curr.execute(f"insert into {self.user_data[4]} values({data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]});")

        self.conn.commit()


    def loadData(self):
        # self.curr.execute("use airfoil;")
        self.validation_data = pd.read_sql(f"select * from {self.user_data[4]};", self.conn)
        self.curr.execute(f"drop table {self.user_data[4]};")
        self.conn.close()
        return self.validation_data
        # print(self.validation_data)







# class MySQL:
#
#     def __init__(self):
#         self.conn = None
#         self.curr = None
#         self.validation_data = None
#         self.user_data = None
#
#
#     def getUserData(self):
#         user_data = json.load(open('userdata.json', 'r'))
#         self.user_data = list(list(user_data.values())[0].values())
#
#     def initConnection(self):
#         self.getUserData()
#         self.conn = connection.connect(host=self.user_data[0], user=self.user_data[2], passwd=self.user_data[3], use_pure=True)
#
#
#     def initCursor(self):
#         self.curr = self.conn.cursor(buffered=True)
#
#
#     def createDB(self):
#         self.curr.execute(f"create database {self.user_data[1]};")
#
#
#     def createTable(self):
#         self.curr.execute(f"use {self.user_data[1]};")
#         columns = self.user_data[5]
#         self.curr.execute(f"create table {self.user_data[4]}({columns[0]} float, {columns[1]} float, {columns[2]} float, "
#                           f"{columns[3]} float, {columns[4]} float, {columns[5]} float);")
#
#
#     def dumpData(self):
#         df = pd.read_csv('Validation_Data.csv', index_col=[0])
#         for i in range(df.shape[0]):
#             data = df.iloc[i]
#             self.curr.execute(f"insert into {self.user_data[4]} values({data[0]}, {data[1]}, {data[2]}, {data[3]}, {data[4]}, {data[5]});")
#
#         self.conn.commit()
#
#
#     def loadData(self):
#         # self.curr.execute("use airfoil;")
#         self.validation_data = pd.read_sql(f"select * from {self.user_data[4]};", self.conn)
#         return self.validation_data
#         # print(self.validation_data)


# m = MySQL()
# m.initConnection()
# m.initCursor()
# m.createDB()
# m.createTable()
# m.dumpData()
# m.loadData()

