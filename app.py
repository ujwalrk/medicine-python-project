from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder="templates")
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:5ubhanuRapp1d!@localhost/medicine_stores'
db = SQLAlchemy(app)

class customers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(255))
    mobile_no = db.Column(db.String(20))
    age = db.Column(db.Integer)
    address = db.Column(db.String(255))
    prescription = db.Column(db.Text)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        full_name = request.form["full_name"]
        mobile_no = request.form["mobile_no"]
        age = request.form["age"]
        address = request.form["address"]
        prescription = request.form["prescription"]

        new_customers = customers(full_name=full_name, mobile_no=mobile_no, age=age, address=address, prescription=prescription)

        try:
            db.session.add(new_customers)
            db.session.commit()
            return render_template('success.html')
        except Exception as e:
            db.session.rollback()
            return f"An error occurred: {str(e)}"

    return render_template('index.html')

if __name__ == "__main__":
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
