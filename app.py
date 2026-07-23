from flask import Flask, render_template, request, redirect, url_for
from models import db, User, Customer, Service, Staff, Appointment

app = Flask(__name__)



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.secret_key = "secret123"

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/routes")
def home():
    return  render_template("index.html")

@app.route("/")
def routes():
    return  redirect(url_for('login'))

@app.route("/register",
methods=["GET", "POST"])
def register():

    if request.method == "POST":

        name = request.form["name"]
        email = request.form["email"]
        password = request.form["password"]

        user = User(
            name=name,
            email=email,
            password=password
        )

        db.session.add(user)
        db.session.commit()

        return redirect(url_for("login"))
    return render_template("register.html")



@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = User.query.filter_by(
            email=email,
            password=password
        ).first()

        if user:
            return redirect(url_for("dashboard"))
        else:
            return "Invalid Email or Password"
    return render_template("login.html")

@app.route("/customer", methods=["GET", "POST"])
def customer():

    if request.method == "POST":

        customer = Customer(
            name=request.form["name"],
            phone=request.form["phone"],
            gender=request.form["gender"],
            address=request.form["address"]
        )

        db.session.add(customer)
        db.session.commit()

        return redirect(url_for("customer"))

    return render_template("customer.html")


@app.route("/service", methods=["GET", "POST"])
def service():

    if request.method == "POST":

        service = Service(
            service_name=request.form["service_name"],
            price=request.form["price"],
            duration=request.form["duration"]
        )

        db.session.add(service)
        db.session.commit()


    return render_template("service.html")



@app.route("/staff", methods=["GET", "POST"])
def staff():

      if request.method == "POST":

        staff = Staff(
            name=request.form["name"],
            phone=request.form["phone"],
            specialization=request.form["specialization"],
            available=request.form["available"]
        )

        db.session.add(staff)
        db.session.commit()

        return  redirect(url_for("staff"))
      return render_template("staff.html")


@app.route("/appointment", methods=["GET", "POST"])
def appointment():

    if request.method == "POST":

        staff_name = request.form["staff_name"]
        date = request.form["appointment_date"]
        time = request.form["appointment_time"]

        # # Check staff already booked or not
        # existing = Appointment.query.filter_by(
        #     staff_name=staff_name,
        #     appointment_date=date,
        #     appointment_time=time
        # ).first()

        # if existing:
        #     return "Staff is already booked at this time"

        appointment = Appointment(
            customer_name=request.form["customer_name"],
            service_name=request.form["service_name"],
            staff_name= staff_name,
            appointment_date=date,
            appointment_time=time
         )

        db.session.add(appointment)
        db.session.commit()

        return "Appointment Booked Successfully"
    return render_template("appointment.html")



@app.route("/dashboard")
def dashboard():
 customers = Customer.query.count()
 services = Service.query.count()
 appointments = Appointment.query.count()

 return render_template( "dashboard.html",
         customers=customers,
         services=services,
         appointments=appointments
     )


if __name__ == "__main__":
    app.run(debug=True)