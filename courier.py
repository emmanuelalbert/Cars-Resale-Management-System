from flask import *
from database import *

courier=Blueprint('courier',__name__)

@courier.rout('/courierhome')
def courierhome():

    return render_template('courier_home.html')


@courier.route("/courierviewallreq")
def courierviewallreq():
    data={}
    q="SELECT * FROM `ordermaster`, `orderdetails`, `customer`, `product` WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `ordermaster`.`customer_id`=`customer`.`customer_id` AND `orderdetails`.`product_id`=`product`.`product_id` and ostatus='paid'"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']
    else:
        action=None

    if action == "accept":
        q="insert into delivery values(null, '%s','%s',curdate(),'Accepted by Courier')"%(omid,session['cor_id'])
        insert(q)
        q="update ordermaster set ostatus='Accepted by Courier' where ordermaster_id='%s'"%(omid)
        update(q)
        flash("Couier Accepted")
        # sweetAlert("Hello")
        return redirect(url_for("courier.courierhome"))
    return render_template("courierviewallreq.html",data=data)


@courier.route("/courierviewmyreq")
def courierviewmyreq():
    data={}
    q="SELECT * FROM `ordermaster`, `orderdetails`, `customer`, `product`, delivery WHERE `ordermaster`.`ordermaster_id`=`orderdetails`.`ordermaster_id` AND `ordermaster`.`customer_id`=`customer`.`customer_id` AND `orderdetails`.`product_id`=`product`.`product_id` and `ordermaster`.`ordermaster_id`=delivery.ordermaster_id and courier_id='%s' "%(session['cor_id'])

    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']
        did=request.args['did']
    else:
        action=None

    if action == "accept":
        q="update delivery set status='Delivery Completed' where delivery_id='%s' "%(did)
        insert(q)
        q="update ordermaster set order_status='Delivery Completed' where ordermaster_id='%s'"%(omid)
        update(q)
        flash("Delivered Successfully")
        return redirect(url_for("courier.courierhome"))
    return render_template("courierviewmyreq.html",data=data)


