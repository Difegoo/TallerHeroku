from flask import Flask, render_template, request, redirect, url_for
import mysql.connector
import numpy as np
from werkzeug.utils import redirect

mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "datosin"
)
myCursor = mydb.cursor() #Se almacena en mycursor

app = Flask(__name__)

@app.route("/") #decorador
def inicio():

    return render_template('registroweb.html')

@app.route("/indato", methods=["POST", "GET"]) #decorador
def indato():

    if request.method == "POST":
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        telefono = request.form['telefono']
        query = f"INSERT INTO users (nombre, edad, apellido, telefono) VALUES('{nombre}','{edad}','{apellido}','{telefono}')"
        myCursor.execute(query)
        mydb.commit()#Confirma los cambios
        #return "EL USUARIO HA SIDO REGISTRADO CORRECTAMENTE"
        return redirect(url_for('inicio'))

    else: 
        return "bad request"

@app.route("/tabla") #decorador
def leerdato2():
    query = "SELECT * FROM users"
    myCursor.execute(query) #Ejecutamos el query
    result = myCursor.fetchall() #Devuelve un arreglo de tuplas (Cada fila de la base de datos)
    return render_template("tablas.html", people = result)

if __name__ == "__main__":
    app.run()