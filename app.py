from flask import Flask, render_template, request, redirect
import mysql.connector 

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = "Joãomysql"
app.config["MYSQL_DB"] = "sorteio"




@app.route("/")
def index():
    return render_template("index.html")

@app.route("/contatos.html")
def contatos():
    return render_template("contatos.html")

@app.route("/sobreogame.html")
def sobreogame():
    return render_template("sobreogame.html")

@app.route("/sorteio.html" , methods=["GET","POST"])
def sorteio():
    if request.method == "HOST":
        email = request.form ["email"]
        texto = request.form ["texto"]

        conn = mysql.connection
        cursor = conn.cursor()

        cursor.execute("INSERT INTO sorteio(email, texto) VALUES (%s, %s)",(email, texto))
        conn.commit()
        cursor.close()
    return render_template("sorteio.html")

@app.route("/index.html")
def inicio():
    return render_template("index.html")


app.run(debug=True)
