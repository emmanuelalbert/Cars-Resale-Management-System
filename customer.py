from flask import *
from database import *

customer=Blueprint('customer',__name__)
from flask import request, render_template, flash

@customer.route("/customerhome", methods=['GET', 'POST'])
def customerhome():
    data = {}

    # Fetch Brand and Category Data
    q = "SELECT * FROM brand"
    data['brand'] = select(q)

    q = "SELECT * FROM category"
    data['cat'] = select(q)

    # Base Query
    base_query = "SELECT * FROM vehicle INNER JOIN category USING(category_id) INNER JOIN brand USING(brand_id) WHERE vehicle.status='available'"

    # Fetch Form Data
    brand = request.form.get('brand')
    min_price = request.form.get('min_price')
    max_price = request.form.get('max_price')
    cat = request.form.get('cat')

    filter_conditions = []

    # Filter by Brand
    if brand:
        filter_conditions.append(f"brand_id = '{brand}'")

    # Filter by Category
    if cat:
        filter_conditions.append(f"category_id = '{cat}'")

    # Final Query Building
    if filter_conditions:
        final_query = base_query + " AND " + " AND ".join(filter_conditions)
    else:
        final_query = base_query

    # Execute Query
    data['result'] = select(final_query)
    print("Executed Query:", final_query)

    # Check if results are empty
    data['no_results'] = len(data['result']) == 0

    if 'search' in request.form:
        flash("Search performed successfully!")

    return render_template('indx.html', data=data)

@customer.route("/customerviewitems",methods=['get','post'])
def customerviewitems():
    data={}
    q="select * from vehicle inner join category using(category_id) inner join brand using(search vehicle) where vehicle.status='available'"
    data['res1']=select(q)
    
    if 'searchbtn' in request.form:
        sch="%"+request.form['search']+"%"
        
        q="select * from vehicle inner join category using(category_id) inner join brand using(brand_id) where vehicle.status='available' and vehicle_name='%s' or category_name='%s' or brand_name='%s'"%(sch,sch,sch)
        data['res']=select(q)
        
    return render_template('customer_view_products.html',data=data)

@customer.route('/singleview',methods=['get','post'])
def singleview():
    data={}
    id=request.args['id']
    q="select * from vehicle where vehicle_id='%s'"%(id)
    print(q)
    data['res']=select(q)
    product_id=data['res'][0]['vehicle_id']
    
    q="select * from booking where booked_status='pending' and vehicle_id='%s' and customer_id='%s'"%(id,session['cid'])
    print(q)
    data['viewcart']=select(q)
    
    if 'addcart' in request.form:
        proid=request.form['proid']
        price=request.form['price']

        q="select * from booking where customer_id='%s' and booked_status='pending'"%(session['cid'])
        res=select(q)
        if res:
            omid=res[0]['booking_id']
            q="update booking set total_amount=total_amount+'%s' where booking_id='%s'"%(price,omid)
            update(q)
            q="insert into booking values(null,'%s','%s',1,'%s')"%(omid,proid,price)
            odid=insert(q)
           
            flash("product added to cart")
            return redirect(url_for('customer.singleview',id=id))
        else:
            q="insert into booking values(null,'%s','%s','%s',curdate(),'pending')"%(session['cid'],proid,price)
            nomid=insert(q)
            flash("product added to cart")
            return redirect(url_for('customer.singleview',id=id))

    if 'viewcart' in request.form:
        return redirect(url_for('customer.customercart'))

    return render_template('customer_single_product.html',data=data)


from flask import jsonify  # Import jsonify to send JSON response

@customer.route('/customercart', methods=['GET', 'POST'])
def customercart():
    data = {}

    # Fetching bookings
    q = """
        SELECT booking.*, vehicle.vehicle_name, vehicle.vehicle_image, vehicle.vehicle_description, 
               vehicle.price, brand.brand_name, booking.date 
        FROM booking 
        INNER JOIN vehicle USING(vehicle_id) 
        INNER JOIN brand USING(brand_id) 
        WHERE booked_status='pending' AND customer_id='%s'
    """ % (session['cid'])
    res = select(q)

    data['viewcart'] = res
    data['len'] = len(res)
    
    # Count existing bookings
    booking_count = len(res)

    if request.method == 'POST' and 'book_test_drive' in request.form:
        vehicle_id = request.form['proid']
        customer_id = session['cid']

        # Prevent booking more than 3 cars
        if booking_count >= 3:
            flash('You can only book a maximum of 3 test drives at a time.', 'error')
            return redirect(url_for('customer.customercart'))

        # Check if the vehicle is already booked
        q = "SELECT * FROM booking WHERE vehicle_id='%s' AND customer_id='%s' AND booked_status='pending'" % (vehicle_id, customer_id)
        existing_booking = select(q)

        if existing_booking:
            flash('You have already booked this vehicle.', 'error')
            return redirect(url_for('customer.customercart'))

        # Fetch vehicle price
        price_query = "SELECT price FROM vehicle WHERE vehicle_id='%s'" % (vehicle_id)
        vehicle_data = select(price_query)
        vehicle_price = vehicle_data[0]['price'] if vehicle_data else 0

        # Insert new booking
        q = """
            INSERT INTO booking (vehicle_id, customer_id, booked_status, total_amount, date) 
            VALUES ('%s', '%s', 'pending', '%s', NOW())
        """ % (vehicle_id, customer_id, vehicle_price)
        insert(q)

        flash('Test drive booked successfully!', 'success')
        return redirect(url_for('customer.customercart'))  # ✅ Redirect instead of popup

    if 'action' in request.args:
        action = request.args['action']
        id = request.args['id']
    else:
        action = None

    if action == 'remove':
        q = "DELETE FROM booking WHERE booking_id='%s'" % (id)
        delete(q)
        flash('Booking removed successfully.', 'success')
        return redirect(url_for('customer.customercart'))

    return render_template('customer_view_cart.html', data=data)


from flask import request, render_template, flash, redirect, url_for, session
import re

from datetime import datetime

@customer.route('/customerpayment', methods=['GET', 'POST'])
def customerpayment():
    data = {}
    total = request.args.get('total')
    data['total'] = total
    omid = request.args.get('id')
    data['id'] = omid

    # Fetch saved cards
    q = "SELECT * FROM card WHERE customer_id='%s'" % (session['cid'])
    data['card'] = select(q)

    # Pre-fill form with selected card details from URL params
    if 'cardname' in request.args:
        cardname = request.args.get('cardname')
        cardno = request.args.get('cardno')
        data['cardno'] = cardno
        data['cardname'] = cardname

    if 'pay' in request.form:
        cn = request.form['cardname']
        cno = request.form['cardno'].replace(' ', '')  # Remove spaces for validation
        cvv = request.form['cvv']  # CVC
        exp_month = request.form['exp_month']
        exp_year = request.form['exp_year']

        # Validate all expiration inputs
        if not exp_month or not exp_year:
            flash('Please select a valid expiration date.', 'error')
            return render_template('customer_payment.html', data=data)

        # Combine exp date
        exp = f"{exp_month}/{exp_year}"

        # Check if expiration date is in the future
        try:
            exp_date = datetime.strptime(f"01/{exp}", "%d/%m/%Y")
            if exp_date < datetime.now().replace(day=1, hour=0, minute=0, second=0, microsecond=0):
                flash('Card has expired. Please use a valid card.', 'error')
                return render_template('customer_payment.html', data=data)
        except ValueError:
            flash('Invalid expiration date format.', 'error')
            return render_template('customer_payment.html', data=data)

        # Validate card number
        if not re.match(r'^\d{16}$', cno):
            flash('Card number must be exactly 16 digits.', 'error')
            return render_template('customer_payment.html', data=data)

        # Validate cardholder name
        if not re.match(r'^[A-Za-z ]+$', cn):
            flash('Cardholder name must contain only letters and spaces.', 'error')
            return render_template('customer_payment.html', data=data)

        # Validate CVV
        if not re.match(r'^\d{3}$', cvv):
            flash('CVC must be exactly 3 digits.', 'error')
            return render_template('customer_payment.html', data=data)

        # Check if card exists
        q = "SELECT * FROM card WHERE card_no='%s'" % (cno)
        res = select(q)
        if res:
            cid = res[0]['card_id']
            q = "INSERT INTO payment VALUES (NULL, '%s', '%s', '%s', NOW())" % (cid, omid, total)
            insert(q)
            k = "UPDATE booking SET booked_status='paid' WHERE booking_id='%s'" % (omid)
            update(k)
        else:
            # Insert new card and process payment
            l = "INSERT INTO card VALUES (NULL, '%s', '%s', '%s', '%s')" % (session['cid'], cno, cn, exp)
            cid = insert(l)
            q = "INSERT INTO payment VALUES (NULL, '%s', '%s', '%s', NOW())" % (cid, omid, total)
            insert(q)
            k = "UPDATE booking SET booked_status='paid' WHERE booking_id='%s'" % (omid)
            update(k)

        flash("Payment finished...", 'success')
        return render_template('customer_payment_processing.html')

    return render_template('customer_payment.html', data=data)




@customer.route('/viewmyorders',methods=['get','post'])
def viewmyorders():
    data={}
    q="select *from booking inner join vehicle using(vehicle_id) where booked_status='paid' and customer_id='%s' "%(session['cid'])
    res=select(q)
    data['myorders']=res
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='return':
        s="select * from booking inner join vehicle using(vehicle_id) where booking_id='%s'"%(id)
        data['return']=select(s)
    if 'send' in request.form:
        reason=request.form['reason']
        a="insert into return_table values(null,'%s','%s',curdate(),'pending')"%(id,reason)
        insert(a)
        b="update booking set booked_status='cancelled' where booking_id='%s'"%(id)
        update(b)
        return redirect(url_for('customer.view_return_request'))
    return render_template('customer_view_myorders.html',data=data)



@customer.route('/viewinvoice')
def viewinvoice():
    data={}
    omid=request.args['id']
    q="SELECT * FROM payment INNER JOIN order_master USING(order_master_id) INNER JOIN card USING(card_id) INNER JOIN order_details USING(order_master_id) INNER JOIN customer ON(order_master.customer_id=customer.customer_id) WHERE payment.order_master_id='%s' AND order_master.customer_id='%s'"%(omid,session['cid'])
    print(q)
    data['pay']=select(q)
    return render_template("customer_view_invoice.html",data=data)


@customer.route('/user_complaint',methods=['get','post'])
def user_complaint():
    data={}
    if 'submit' in request.form:
        complaints=request.form['complaints']
        a="insert into complaint values(null,'%s','%s','pending',curdate())"%(session['cid'],complaints)
        insert(a)
        flash("complaint send successfully")
        return redirect(url_for('customer.user_complaint'))
    s="select * from complaint where customer_id='%s'"%(session['cid'])
    data['value']=select(s)
    return render_template('customer_send_complaints.html',data=data)

@customer.route('/view_return_request',methods=['get','post'])
def view_return_request():
    data={}
    s="select *,return_table.status as rstatus,return_table.date as rdate from return_table inner join booking using(booking_id) inner join vehicle using(vehicle_id) where customer_id='%s'"%(session['cid'])
    data['value']=select(s)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='return':
        a="select * from refund where return_id='%s'"%(id)
        data['refund']=select(a)
    return render_template('customer_return_request.html',data=data)