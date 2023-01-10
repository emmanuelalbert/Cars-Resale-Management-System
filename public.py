from flask import *
from database import *

public=Blueprint('public',__name__)

@public.route('/',methods=['get','post'])
def home():
   
    return render_template('index.html')



@public.route('/login',methods=['post','get'])
def login():

    if 'login' in request.form:
        email=request.form['uname']
        pasw =request.form['passw']

        q="select * from login where username='%s' and password='%s'"%(email,pasw)
        print(q)
        res=select(q)
        
        if res:
            session['email']=res[0]["username"]
            utype=res[0]["type"]
            if utype == "admin":
                q="select * from login where type='admin' and status='active'"
                adminact=select(q)
                if adminact:
                    flash("Login Succeessfully")
                    return redirect(url_for("admin.adhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            elif utype == "staff":
                q="select * from login where type='staff' and status='active'"
                staffact=select(q)
                if staffact:
                    q="select * from staff where username='%s'"%(session['email'])
                    session['sid']=select(q)[0]['staff_id']
                    flash("Login Succeessfully")
                    return redirect(url_for("staff.staffhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            elif utype == "customer":
                q="select * from login where type='customer' and status='active'"
                customeract=select(q)
                if customeract:
                    q="select * from customer where username='%s'"%(session['email'])
                    session['cid']=select(q)[0]['customer_id']
                    flash("Login Succeessfully")
                    return redirect(url_for("customer.customerhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            elif utype == "courier":
                q="select * from login where type='courier' and status='active'"
                courieract=select(q)
                if courieract:
                    q="select * from courier where username='%s'"%(session['email'])
                    session['cor_id']=select(q)[0]['courier_id']
                    flash("Login Succeessfully")
                    return redirect(url_for("courier.courierhome"))
                else:
                    flash("This Account is not Active")
                    return redirect(url_for("public.login")) 
            else:
                flash("failed try again")
                return redirect(url_for("public.login"))
        else:
            flash("invalid Email or Password!")
            return redirect(url_for("public.login"))

    return render_template("login.html")


@public.route('/userreg',methods=['get','post'])
def userreg():
    data={}
    if 'submit' in request.form:
        email=request.form['email']
        password=request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        house=request.form['house']
        street=request.form['street']
        city=request.form['city']
        # district=request.form['district']
        state=request.form['state']
        pin=request.form['pin']
        phone=request.form['phone']
        gender=request.form['gender']
        dob=request.form['dob']
        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values ('%s','%s','customer','active')"%(email,password)
            insert(q)
            q="insert into customer values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','inactive')"%(email,fname,lname,house,street,city,state,pin,phone,email,gender,dob)
            insert(q)
            return redirect(url_for("public.login"))
    return render_template('customer_register.html',data=data)