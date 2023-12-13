import requests
import json
import mysql.connector as connector

url = "https://qbmbuvbhbxbjmjo.form.io/prueba/submission"

response = requests.request("GET", url)

data = json.loads(response.text)
#Ordenamos el Json para que sea legible
dataj = json.dumps(data,indent=4)

print(dataj)

# for elemento in data: 
#     try:
#         connection = connector.connect(host='localhost',
#                                         database='formio',
#                                         user='root',
#                                         password='')
        
#         mySql_insert_query = f"""INSERT INTO data (name,age,apellido) VALUES ('{elemento['data']['nombre']}',{elemento['data']['edad']}) """

#         cursor = connection.cursor()
#         cursor.execute(mySql_insert_query)
#         connection.commit()
#         print(cursor.rowcount, "Record inserted successfully into Laptop table")
#         cursor.close()

#     except connector.Error as error:
#         print("Failed to insert record into Laptop table {}".format(error))

#     finally:
#         if connection.is_connected():
#             connection.close()
#             print("MySQL connection is closed")
    
