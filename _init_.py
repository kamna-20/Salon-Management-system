{% extends "base.html" %}
{% block content %}
<div class="booking-page">
<div class="booking-box">

<h1 class="text-center mb-2">Book Your Appointment</h1>
<p class="text-center text-muted mb-4"> Glow & Grace Salon</p>

{% if message %}
<p class=" alert alert-success">{{ message }}></p>
{% endif %}

<form method="POST">

    <label>Customer Name</label><br>
    <input type="text" name="customer_name" class="form-control" required><br><br>



    <label> Customer Gender</label><br>
    <select name="customer_gender"
            id="customer_gender"
            class="form-control" required>
            <option value="" disabled selected>Select Gender</option>
            <option value="Male"> Male</option>
            <option value="Female">Female</option>
        </select>
        <br><br>

    <label>Service</label><br>
    <select name="service_name" class="form-control" required>
        <option value="" disabled selected> Select Services</option>
        {% for service in services %}
        <option value="{{ service.service_name }}">
            {{ service.service_name }}
        </option>
        {% endfor %}
    </select><br><br>

    <label>Staff</label><br>
    <select name="staff_name"  class="form-control" required>
         <option value="" disabled selected> Select Staff</option>
        {% for staff in staffs %}
        <option value="{{ staff.name }}">
            {{ staff.name }} - {{ staff.specialization }}
        </option>
        {% endfor %}
    </select><br><br>

    <label>Appointment Date</label><br>
    <input type="date" name="appointment_date" class="form-control" min="{{ today }}" required><br><br>

    <label>Appointment Time</label><br>
    <input type="time" name="appointment_time" class="form-control" required><br><br>

    <button type="submit" class="btn btn-primary btn-lg w-100 mt-3"> Book Appointment</button>

</form>

<br>

<a href="/" class=" btn btn-outline dark btn-lg w-100 mt-3"> Back to Home </a>
</div>
</div>




{% endblock %}





.booking-page{
    min-height:100vh;
    width:100%;
    background:linear-gradient(rgba(0,0,0,.5),rgba(0,0,0,.5)),
    url("https://images.unsplash.com/photo-1560066984-138dadb4c035?auto=format&fit=crop&w=1600&q=80");
    justify-content: center;
    background-position:center;
    align-items: flex-start;
    display:flex;
    box-sizing: border-box;
    background-attachment: fixed;
    padding:  45px 20px;

}

html,body{
    margin: 0;
    padding: 0%;
    width: 100%;
    overflow-x: hidden;
}


.booking-box{
    max-width:850px;
    width:100%;
    background:rgba(219, 212, 212, 0.9);
    padding: 10px 45px 45px;
    border-radius:0;
    box-shadow:0 10px 30px rgba(0,0,0,0.3);
    box-sizing: border-box;
    border: none;
}

.booking-box h1{
    text-align:center;
    color:#a55f76;
    font-size:48px;
    font-weight:bold;
    margin-bottom:10px;
    font-family: cursive;
    text-decoration: underline;
    text-decoration-color:#a55f76 ;
    text-decoration-thickness: 3px;
}

.booking-box p{
    text-align:center;
    color:grey;
    margin-bottom:35px;
    font-family: Georgia, 'Times New Roman', Times, serif;
    font-style: italic;
    font-weight: bold;
    font-size: 25px;
}

.booking-box label{
    font-size:15px;
    font-weight:700;
    margin-top: 20px;
    color:#444;
    margin-bottom:8px;
    display:block;
}

.booking-box .form-control{

    padding: 0 12px;
    border-radius:12px;
    border: none;
    border-bottom: 2px solid #cfbec3;
    margin-bottom:10px;
    box-shadow: none;
    color:#444;
    box-sizing: border-box;
    font-size:16px;
    transition: all .3s ease;
    height: 54px;
    width:100%;
    background: rgba(173, 170, 170, 0.95);
}

.booking-box .form-control:focus{
    border-color:#d63384;
    box-shadow:0 0 10px rgba(214,51,132,.3);
    outline:none;
    background-color: rgb(172, 172, 170);
    font-family: Arial, Helvetica, sans-serif;
    font-size: large;
}
.booking-box select.form-control{
    cursor:pointer;
}
.booking-box .alert{
    border-radius: 8px;
    margin-bottom: 20px;
}

 .booking-box .btn-primary{
    background:linear-gradient(135deg,#c9a1af,#c98b9f);
    color:white;
    box-shadow: 0 8px 20px rgba(165,95,118,0.25);
    border:none;
    border-radius:30px;
    font-size:18px;
    font-weight:bold;
    width:230px;
    height:52px;
    margin:35px auto 0;
    transition:.3s;
    display: block;
}

.btn-primary:hover{
    transform:translateY(-3px);
    box-shadow:0 10px 20px rgba(214,51,132,.4);
    background: #c2185b;
}

.btn-outline-dark{
    border-radius:12px;
    font-size:18px;
    font-weight:bold;
    transition:.3s;
    width: 100%;

}

.btn-outline-dark:hover{
    background:#653e3e;
    color:rgb(144, 139, 139);
}


.alert-success{
    border-radius:12px;
    text-align:center;
    font-weight:bold;
}
@media (max-width:768px)  {
    .booking-page{
        padding:25px 15px 40px;
    }
    .booking-box{
        padding:10px 20px 35px;
    }
    .booking-box h1{
        font-size: 36px;
    }
    .booking-box p.text-muted{
        font-size: 21px;
    }
    .booking-box .btn-primary{
        width:100%;
    }
}


