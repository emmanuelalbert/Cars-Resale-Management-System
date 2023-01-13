from flask import *
from database import *

customer=Blueprint('customer',__name__)

@customer.route('/customerhome')
def customerhome():

    return render_template('customer_home.html')


@customer.route("/customerviewitems",methods=['get','post'])
def customerviewitems():
    data={}
    q="select * from purchase_master pm,purchase_details pd,product p where pm.pmaster_id=pd.pmaster_id and pd.product_id=p.product_id"
    data['res']=select(q)
    return render_template('customer_view_products.html',data=data)

@customer.route('/singleview',methods=['get','post'])
def singleview():
    data={}
    pdid=request.args['pdid']
    q="select * from purchase_details pd,product p,subcategory sc,category c where pd.product_id=p.product_id and p.subcat_id=sc.subcat_id and sc.cat_id=c.cat_id and pd.pdetails_id='%s'"%(pdid)
    print(q)
    data['res']=select(q)
    product_id=data['res'][0]['product_id']

    q="select * from order_master om,order_details od,product p where om.order_master_id=od.order_master_id and od.product_id=p.product_id and od.product_id=(select product_id from purchase_details where pdetails_id='%s')"%(pdid)
    print(q)
    data['viewcart']=select(q)
    
    if 'addcart' in request.form:
        proid=request.form['proid']
        price=request.form['price']

        q="select * from order_master where customer_id='%s' and ostatus='pending'"%(session['cid'])
        res=select(q)
        if res:
            omid=res[0]['order_master_id']
            q="update order_master set total_amount=total_amount+'%s' where order_master_id='%s'"%(price,omid)
            update(q)
            q="insert into order_details values(null,'%s','%s',1,'%s')"%(omid,proid,price)
            odid=insert(q)
            q="insert into purchased values(null,'%s','%s',1)"%(pdid,odid)
            insert(q)
            flash("product added to cart")
            return redirect(url_for('customer.singleview',pdid=pdid))
        else:
            q="insert into order_master values(null,'%s','%s',curdate(),'pending')"%(session['cid'],price)
            nomid=insert(q)
            q="insert into order_details values(null,'%s','%s',1,'%s')"%(nomid,proid,price)
            odid1=insert(q)
            q="insert into purchased values(null,'%s','%s',1)"%(pdid,odid1)
            insert(q)
            flash("product added to cart")
            return redirect(url_for('customer.singleview',pdid=pdid))

    if 'viewcart' in request.form:
        return redirect(url_for('customer.customercart'))

    return render_template('customer_single_product.html',data=data)


@customer.route('/customercart',methods=['get','post'])
def customercart():
    data={}
    q="select *,od.quantity as qty,pd.quantity as puqty from order_master om,order_details od,product p,purchased pur,purchase_details pd where om.order_master_id=od.order_master_id and od.product_id=p.product_id and pur.order_details_id=od.order_details_id and pur.pdetails_id=pd.pdetails_id "
    data['viewcart']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']

    else:
        action=None
    
    if action=='plus':

        q="select * from order_details where order_details_id='%s'"%(id)
        res=select(q)
        omid=res[0]['order_master_id']
        qty=res[0]['quantity']
        price=res[0]['total_price']
        unitp=int(price)/int(qty)
        q="update order_master set total_amount=total_amount+'%s' where order_master_id='%s'"%(unitp,omid)
        update(q)
        q="update order_details set total_price=total_price+'%s',quantity=quantity+1 where order_details_id='%s'"%(unitp,id)
        update(q)
        q="update purchased set qty_purchased=qty_purchased+1 where order_details_id='%s'"%(id)
        update(q)
        return redirect(url_for('customer.customercart'))

    if action=='minus':

        q="select * from order_details where order_details_id='%s'"%(id)
        res=select(q)
        omid=res[0]['order_master_id']
        qty=res[0]['quantity']
        price=res[0]['total_price']
        unitp=int(price)/int(qty)
        q="update order_master set total_amount=total_amount-'%s' where order_master_id='%s'"%(unitp,omid)
        update(q)
        q="update order_details set total_price=total_price-'%s',quantity=quantity-1 where order_details_id='%s'"%(unitp,id)
        update(q)
        q="update purchased set qty_purchased=qty_purchased-1 where order_details_id='%s'"%(id)
        update(q)
        return redirect(url_for('customer.customercart'))


    if action=='remove':

        q="select * from order_details where order_details_id='%s'"%(id)
        res=select(q)
        omid=res[0]['order_master_id']
        qty=res[0]['quantity']
        price=res[0]['total_price']
        data['total']=price
        # unitp=int(price)/int(qty)
        q="update order_master set total_amount=total_amount-'%s' where order_master_id='%s'"%(price,omid)
        update(q)
        q="delete from order_details where order_details_id='%s'"%(id)
        delete(q)
        q="delete from purchased where order_details_id='%s'"%(id)
        delete(q)
        return redirect(url_for('customer.customercart'))
    return render_template('customer_view_cart.html',data=data)


@customer.route('/customerpayment',methods=['get','post'])
def customerpayment():
    data={}
    total=request.args['total']
    data['total']=total
  
    omid=request.args['id']
    data['id']=omid
    q="select * from card where customer_id='%s'"%(session['cid'])
    data['card']=select(q)

    if 'cardname' in request.args:
        cardname=request.args['cardname']
        cardno=request.args['cardno']
        data['cardno']=cardno
        data['cardname']=cardname
       

    if 'pay' in request.form:
        cn=request.form['cardname']
        cno=request.form['cardno']
        exp=request.form['exp']

        q="insert into card values(null,'%s','%s','%s','%s')"%(session['cid'],cno,cn,exp)
        cid=insert(q)
        q="insert into payment values(null,'%s','%s','%s',now())"%(cid,omid,total)
        insert(q)
        q="update order_details set ostatus='paid' where order_master_id='%s'"%(id)
        update(q)
        q="SELECT * FROM `order_master` om,`order_details` od,`purchased` p,`purchase_details` pd WHERE om.order_master_id=od.order_master_id AND od.order_details_id=p.order_details_id AND p.pdetails_id=pd.pdetails_id AND om.order_master_id='%s'"%(omid)
        res=select(q)
        print(res)
        for i in res:
            pur_det=i['pdetails_id']
            qty_pur=i['qty_purchased']
            q="update purchase_details set quantity=quantity-'%s' where pdetails_id='%s'"%(qty_pur,pur_det)
            print(q)
            update(q)
        flash("payment finished...")
        return redirect(url_for('customer.customerhome'))

    return render_template('customer_payment.html',data=data)