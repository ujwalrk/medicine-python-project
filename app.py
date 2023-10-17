from flask import Flask, render_template, request
from flask_mysqldb import MySQL
app = Flask(__name__, template_folder="templates")

app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = "Assassincreed4$"
app.config['MYSQL_DB'] = "medicine_stores"

mysql = MySQL(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        full_name = request.form["full_name"]
        mobile_no = request.form["mobile_no"]
        age = request.form["age"]
        address = request.form["address"]
        prescription = request.form["prescription"]
		
        cur = mysql.connection.cursor()

        cur.execute( "INSERT INTO customers (full_name,mobile_no, age, address, prescription) VALUES(%s, %s, %s, %s, %s)",(full_name,mobile_no, age, address, prescription))
        mysql.connection.commit()
        cur.close()
        return render_template('success.html')
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)