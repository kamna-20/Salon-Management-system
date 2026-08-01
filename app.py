from flask import Flask, render_template, request, redirect, url_for, session
from models import db, User, Customer, Service, Staff, Appointment,Payment

from dotenv import load_dotenv 
import os
load_dotenv()

app = Flask(__name__)
app.secret_key = "salon123"



app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

app.config['SECRET_KEY'] 
os.getenv('SECRET_KEY')

db.init_app(app)

with app.app_context():
    db.create_all()

# @app.route("/routes")
# def home():
#     return  render_template("index.html")

# @app.route("/")
# def routes():
#     return  redirect(url_for('login'))
@app.route("/")
def home():
    return  render_template("index.html")

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
            session["logged_in"]=True
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
            service_name=request.form["service"],
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



from datetime import datetime, date

@app.route("/appointment", methods=["GET", "POST"])
def appointment():

    staffs = Staff.query.all()
    services = Service.query.all()

    if request.method == "POST":

        customer_name = request.form["customer_name"]
        service_name = request.form["service_name"]
        staff_name = request.form["staff_name"]
        appointment_date = request.form["appointment_date"]
        appointment_time = request.form["appointment_time"]

        # Check past date
        selected_date = datetime.strptime(
            appointment_date, "%Y-%m-%d"
        ).date()

        if selected_date < date.today():
            return render_template(
                "appointment.html",
                message="Past date is not allowed.",
                staffs=staffs,
                services=services,
                today=date.today()
            )

        # Check if staff is already booked
        existing = Appointment.query.filter_by(
            staff_name=staff_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).first()

        if existing:
            return render_template(
                "appointment.html",
                message="Staff is already booked at this time.",
                staffs=staffs,
                services=services,
                today=date.today()
            )

        appointment = Appointment(
            customer_name=customer_name,
            service_name=service_name,
            staff_name=staff_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        )

        db.session.add(appointment)
        db.session.commit()

        return render_template(
            "appointment.html",
            message="Appointment Booked Successfully.",
            staffs=staffs,
            services=services,
            today=date.today()
        )

    return render_template(
        "appointment.html",
        staffs=staffs,
        services=services,
        today=date.today()
    )
        


@app.route("/dashboard")
def dashboard():
  if"logged_in"not in session:
      return redirect(url_for("login"))
  
  total_customers = Customer.query.count()
  total_services = Service.query.count()
  total_appointments = Appointment.query.count()

  return render_template( "dashboard.html",
        total_customers = total_customers,
         total_services=total_services,
         total_appointments=total_appointments
     )



@app.route('/payment', methods=['GET','POST'])
def payment():

    services = Service.query.all()

    if request.method == "POST":

        customer_name = request.form.get("customer_name")
        service_id = request.form.get("service_id")
        payment_method = request.form.get("payment_method")

        selected_service = Service.query.get(service_id)

        new_payment = Payment(
            customer_name=customer_name,
            service=selected_service.service_name,
            amount=selected_service.price,
            payment_method=payment_method
        )

        db.session.add(new_payment)
        db.session.commit()

        return redirect('/payment')

    return render_template("payment.html", services=services)




from datetime import datetime, date

@app.route("/book_appointment", methods=["GET", "POST"])
def book_appointment():

    staffs = Staff.query.all()
    services = Service.query.all()

    if request.method == "POST":

        customer_name = request.form["customer_name"]
        service_name = request.form["service_name"]
        staff_name = request.form["staff_name"]
        appointment_date = request.form["appointment_date"]
        appointment_time = request.form["appointment_time"]

        # Past date check
        selected_date = datetime.strptime(
            appointment_date, "%Y-%m-%d"
        ).date()

        if selected_date < date.today():
            return render_template(
                "book_appointment.html",
                message="Past date is not allowed.",
                staffs=staffs,
                services=services,
                today=date.today()
            )

        # Staff already booked check
        existing = Appointment.query.filter_by(
            staff_name=staff_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        ).first()

        if existing:
            return render_template(
                "book_appointment.html",
                message="Staff is already booked at this time.",
                staffs=staffs,
                services=services,
                today=date.today()
            )

        appointment = Appointment(
            customer_name=customer_name,
            service_name=service_name,
            staff_name=staff_name,
            appointment_date=appointment_date,
            appointment_time=appointment_time
        )

        db.session.add(appointment)
        db.session.commit()

        return render_template(
            "book_appointment.html",
            message="Appointment Booked Successfully.",
            staffs=staffs,
            services=services,
            today=date.today()
        )

    return render_template(
        "book_appointment.html",
        staffs=staffs,
        services=services,
        today=date.today()
    )

if __name__ == "__main__":
    app.run(debug=True)