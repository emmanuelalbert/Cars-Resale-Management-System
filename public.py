from flask import *
from database import *

public = Blueprint('public', __name__)

@public.route('/', methods=['get', 'post'])
def home():
    return render_template('index.html')

@public.route('/login', methods=['post', 'get'])
def login():
    if 'login' in request.form:
        email = request.form['uname']
        pasw = request.form['passw']

        q = "SELECT * FROM login WHERE username='%s' AND password='%s'" % (email, pasw)
        print(q)
        res = select(q)
        
        if res:
            session['email'] = res[0]["username"]
            utype = res[0]["type"]
            if utype == "admin":
                q = "SELECT * FROM login WHERE type='admin' AND status='active'"
                adminact = select(q)
                if adminact:
                    flash("Login Successfully")
                    return redirect(url_for("admin.adhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            elif utype == "staff":
                q = "SELECT * FROM login WHERE username='%s' AND status='active'" % (session['email'])
                staffact = select(q)
                if staffact:
                    q = "SELECT * FROM staff WHERE username='%s'" % (session['email'])
                    session['sid'] = select(q)[0]['staff_id']
                    flash("Login Successfully")
                    return redirect(url_for("staff.shome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            elif utype == "customer":
                q = "SELECT * FROM login WHERE username='%s' AND status='active'" % (session['email'])
                customeract = select(q)
                if customeract:
                    q = "SELECT * FROM customer WHERE username='%s'" % (session['email'])
                    session['cid'] = select(q)[0]['customer_id']
                    flash("Login Successfully")
                    return redirect(url_for("customer.customerhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            elif utype == "courier":
                q = "SELECT * FROM login WHERE username='%s' AND status='active'" % (session['email'])
                courieract = select(q)
                if courieract:
                    q = "SELECT * FROM courier WHERE username='%s'" % (session['email'])
                    session['cor_id'] = select(q)[0]['courier_id']
                    flash("Login Successfully")
                    return redirect(url_for("courier.courierhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            else:
                flash("Failed try again")
                return redirect(url_for("public.login"))
        else:
            flash("Invalid Email or Password!")
            return redirect(url_for("public.login"))

    return render_template("login.html")

@public.route('/userreg', methods=['GET', 'POST'])
def userreg():
    data = {}
    if 'submit' in request.form:
        # Capture form data
        email = request.form.get('email')  # Using .get() ensures we don't get a KeyError
        password = request.form.get('password')
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        house = request.form.get('hname')
        street = request.form.get('street')
        city = request.form.get('city')
        state = request.form.get('state')
        pin = request.form.get('pin')
        phone = request.form.get('phone')
        gender = request.form.get('gender')
        dob = request.form.get('dob')

        # Check if email is provided
        if not email:
            flash("Email is required!", "error")
            return render_template('customer_register.html', data=data)

        # Check if username already exists
        q = "SELECT * FROM login WHERE username='%s'" % (email)
        res = select(q)
        if res:
            flash("Username Already Exists!", "error")
        else:
            # Insert into login table with email
            q = "INSERT INTO login (username, password, type, status) VALUES ('%s', '%s', 'customer', 'active')" % (email, password)
            insert(q)

            # Insert into customer table
            s = """INSERT INTO customer 
                    (username, customer_fname, customer_lname, customer_house_name, customer_street, 
                    customer_city, customer_state, customer_pincode, customer_phone, customer_gender, 
                    customer_dob, customer_status) 
                    VALUES 
                    ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', 'active')""" % (
                email, fname, lname, house or "NULL", street or "NULL", city or "NULL", state or "NULL",
                pin, phone or "NULL", gender or "NULL", dob or "NULL"
            )
            insert(s)

            return redirect(url_for("public.login"))
    
    return render_template('customer_register.html', data=data)


@public.route('/reset_password', methods=['GET', 'POST'])
def reset_password():
    if 'reset' in request.form:
        uname = request.form['uname']
        new_passw = request.form['new_passw']
        confirm_passw = request.form['confirm_passw']

        # Check if username exists
        q = "SELECT * FROM login WHERE username='%s'" % (uname)
        user = select(q)

        if user:
            if new_passw == confirm_passw:
                # Update password
                q = "UPDATE login SET password='%s' WHERE username='%s'" % (new_passw, uname)
                update(q)  # Assuming 'update' is a function in database.py for UPDATE queries
                flash("Password reset successfully. Please log in.", "success")
                return redirect(url_for('public.login'))
            else:
                flash("Passwords do not match", "error")
                return render_template('reset_password.html')
        else:
            flash("Username not found", "error")
            return render_template('reset_password.html')
    
    return render_template('reset_password.html')
