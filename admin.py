from flask import *
from database import *
import uuid

admin=Blueprint('admin',__name__)

@admin.route('/adhome')
def adhome():

    from datetime import date
    today=date.today()
    print(today)
    
    # q="select * from product product"
    # res=select(q)
    # if res:
    #     for i in res:
    #         product_id=i['product_id']
            
    #         q1="select * from product where product_id='%s' and exp_date='%s'"%(product_id,today)
    #         res1=select(q1)
    #         if res1:
    #             q="update product set status='Expired' where product_id='%s'"%(product_id)
    #             update(q)
    #             flash("Some of the Product Is Expired... please take nessory action")
    #         else:
    #             a=2
    #     else:
            # c=2
    
    
    return render_template('admin_home.html')



@admin.route('/adminmanagestaff', methods=['GET', 'POST'])
def adminmanagestaff():
    data = {}

    # Insert new staff
    if 'submit' in request.form:
        email = request.form['email']
        password = request.form['password']
        fname = request.form['fname']
        lname = request.form['lname']
        house = request.form['house']
        street = request.form['street']
        city = request.form['city']
        district = request.form['district']
        pin = request.form['pin']
        phone = request.form['phone']
        gender = request.form['gender']
        dob = request.form['dob']

        # Check if email already exists
        q = "SELECT * FROM login WHERE username='%s'" % (email)
        res = select(q)

        if res:
            flash("Username Already Exists!")
        else:
            q1 = "INSERT INTO login (username, password, type, status) VALUES ('%s', '%s', 'staff', 'active')" % (email, password)
            insert(q1)

            q2 = """
                INSERT INTO staff (
                    username, staff_fname, staff_lname, staff_house_name, staff_street,
                    staff_city, staff_dist, staff_pincode, staff_phone, staff_email,
                    staff_gender, staff_dob, staff_status
                ) VALUES (
                    '%s', '%s', '%s', '%s', '%s',
                    '%s', '%s', '%s', '%s', '%s',
                    '%s', '%s', 'inactive'
                )
            """ % (
                email, fname, lname, house, street,
                city, district, pin, phone, email,
                gender, dob
            )

            try:
                insert(q2)
                flash("Staff added successfully!")
                return redirect(url_for("admin.adminmanagestaff"))
            except Exception as e:
                print("Insert Error:", e)
                flash("Error while adding staff!")

    # Show all staff
    q = "SELECT * FROM staff"
    data['res'] = select(q)

    # Handle actions
    action = request.args.get('action')
    uname = request.args.get('uname')
    stid = request.args.get('stid')

    if action == "active":
        update("UPDATE login SET status='active' WHERE username='%s'" % uname)
        update("UPDATE staff SET staff_status='active' WHERE staff_id='%s'" % stid)
        return redirect(url_for("admin.adminmanagestaff"))

    if action == "inactive":
        update("UPDATE login SET status='inactive' WHERE username='%s'" % uname)
        update("UPDATE staff SET staff_status='inactive' WHERE staff_id='%s'" % stid)
        return redirect(url_for("admin.adminmanagestaff"))

    if action == "update":
        q = "SELECT * FROM staff WHERE staff_id='%s'" % stid
        data['up'] = select(q)

    # Update staff info
    if 'update' in request.form:
        fname = request.form['fname']
        lname = request.form['lname']
        house = request.form['house']
        street = request.form['street']
        city = request.form['city']
        district = request.form['district']
        pin = request.form['pin']
        phone = request.form['phone']
        gender = request.form['gender']
        dob = request.form['dob']

        q = """
            UPDATE staff SET
                staff_fname='%s',
                staff_lname='%s',
                staff_house_name='%s',
                staff_street='%s',
                staff_city='%s',
                staff_dist='%s',
                staff_pincode='%s',
                staff_phone='%s',
                staff_gender='%s',
                staff_dob='%s'
            WHERE staff_id='%s'
        """ % (
            fname, lname, house, street, city,
            district, pin, phone, gender, dob, stid
        )

        update(q)
        flash("Staff details updated!")
        return redirect(url_for("admin.adminmanagestaff"))

    return render_template('admin_manage_staff.html', data=data)



@admin.route('/adminmanagevendor',methods=['get','post'])
def adminmanagevendor():
    data={}
    if 'submit' in request.form:
       
        email=request.form['email']
        name=request.form['vname']
       
     
        street=request.form['street']
        city=request.form['city']
       
  
        pin=request.form['pin']
        phone=request.form['phone']

        q="select * from vendor where v_email='%s'"%(email)
        res=select(q)
        if res:
            flash("Alredy Exists......")
        else:
            q="insert into vendor values (null,'0','%s','%s','%s','%s','%s','%s','active')"%(name,email,street,city,pin,phone)
            insert(q)
            return redirect(url_for("admin.adminmanagevendor"))
    data={}
    q="select *,vendor.status as status from vendor "
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        vid=request.args['vid']
   
      
    else:
        action=None

    if action == "active":
      
        q="update vendor set status='active' where vendor_id='%s' "%(vid)
        update(q)
       
        return redirect(url_for("admin.adminmanagevendor"))
    if action == "inactive":
       
        q="update vendor set status='inactive' where vendor_id='%s' "%(vid)
        update(q)
       
        return redirect(url_for("admin.adminmanagevendor"))

    if action == "update":
        q="select * from vendor where vendor_id='%s'"%(vid)
        val=select(q)
        data['vendor']=val

        if 'update' in request.form:
           
            email=request.form['email']
            name=request.form['vname']
        
        
            street=request.form['street']
            city=request.form['city']
        
    
            pin=request.form['pin']
            phone=request.form['phone']

            q="update vendor set v_name='%s', v_street='%s', v_city='%s', v_pincode='%s', v_phone='%s',v_email='%s' where vendor_id='%s' "%(name,street,city,pin,phone,email,vid)
            update(q)
            return redirect(url_for("admin.adminmanagevendor"))
    return render_template('admin_manage_vendor.html',data=data) 



@admin.route('/adminmanagecourier',methods=['get','post'])
def adminmanagecourier():
    data={}
    if 'submit' in request.form:
       
        # email=request.form['email']
        name=request.form['cname']
       
     
        street=request.form['street']
        city=request.form['city']
       
  
        pin=request.form['pin']
        phone=request.form['phone']
    
        uname=request.form['uname']
        passw=request.form['password']

        state=request.form['state']

        q="select * from login where username='%s'"%(uname)
        res=select(q)
        if res:
            flash("username already exists")
        else:

            q="insert into login values('%s','%s','courier','inactive')"%(uname,passw)
            insert(q)

            q="insert into courier values (null,'0','%s','%s','%s','%s','%s','%s','%s','inactive')"%(uname,name,street,city,state,pin,phone)
            insert(q)
        return redirect(url_for("admin.adminmanagecourier"))
    data={}
    q="select * from courier"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        vid=request.args['vid']
   
      
    else:
        action=None

    if action == "active":
      
        q="update courier set status='active' where courier_id='%s' "%(vid)
        update(q)
        q="update login set status='active' where username=(select username from courier where courier_id='%s')"%(vid)
        update(q)
        return redirect(url_for("admin.adminmanagecourier"))
    if action == "inactive":
       
        q="update courier set status='inactive' where courier_id='%s' "%(vid)
        update(q)
        q="update login set status='inactive' where username=(select username from courier where courier_id='%s')"%(vid)
        update(q)
        return redirect(url_for("admin.adminmanagecourier"))

    if action == "update":
        q="select * from courier where courier_id='%s'"%(vid)
        val=select(q)
        data['cour']=val

        if 'update' in request.form:
           
            # email=request.form['email']
            name=request.form['cname']
        
        
            street=request.form['street']
            city=request.form['city']
        
    
            pin=request.form['pin']
            phone=request.form['phone']
        
          
            state=request.form['state']

            q="update courier set cour_name='%s', cour_street='%s', cour_city='%s', cour_pincode='%s', cour_phone='%s',cour_state='%s' where courier_id='%s' "%(name,street,city,pin,phone,state,vid)
            update(q)
            return redirect(url_for("admin.adminmanagecourier"))
    return render_template('admin_manage_courier.html',data=data) 



@admin.route('/adminmanagecaterogy',methods=['get','post'])
def adminmanagecaterogy():
    data={}
    if 'submit' in request.form:
        name=request.form['name']
        desc=request.form['desc']
        
        q="select * from category where category_name='%s'"%(name)
        res=select(q)
        if res:
            flash("already exists......")
        else:
    
            q="insert into category values (null,'%s','%s')"%(name,desc)
            insert(q)
            return redirect(url_for("admin.adminmanagecaterogy"))

    data={}
    q="select * from category"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        cat_id=request.args['cat_id']

      
    else:
        action=None

    # if action == "active":
    #     q="update category set status='active' where category_id='%s' "%(cat_id)
    #     update(q) 
    #     return redirect(url_for("admin.adminmanagecaterogy"))
    # if action == "inactive":
    #     q="update category set status='inactive' where category_id='%s' "%(cat_id)
    #     update(q)
    #     return redirect(url_for("admin.adminmanagecaterogy"))

    if action == "update":
        q="select * from category where category_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

    if 'update' in request.form:
        name=request.form['name']
        desc=request.form['desc']

        q="update category set category_name='%s', category_description='%s' where category_id='%s' "%(name,desc,cat_id)
        update(q)
        return redirect(url_for("admin.adminmanagecaterogy"))
    if action=='delete':
        a="delete from category where category_id='%s'"%(cat_id)
        delete(a)
        return redirect(url_for("admin.adminmanagecaterogy"))
    return render_template('admin_manage_category.html',data=data) 



@admin.route('/adminmanagesubcategory',methods=['get','post'])
def adminmanagesubcategory():
    data={}

    q="select * from category  "
    data['cat']=select(q)
    if 'submit' in request.form:
        catid=request.form['catid']
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into subcategory values (null,'%s','%s','%s')"%(catid,name,desc)
        insert(q)
        return redirect(url_for("admin.adminmanagesubcategory"))


    q="select * from subcategory inner join category using (category_id)"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        subid=request.args['subid']

      
    else:
        action=None

    # if action == "active":
    #     q="update subcategory set status='active' where subcategory_id='%s' "%(subid)
    #     update(q) 
    #     return redirect(url_for("admin.adminmanagesubcategory"))
    # if action == "inactive":
    #     q="update subcategory set status='inactive' where subcategory_id='%s' "%(subid)
    #     update(q)
    #     return redirect(url_for("admin.adminmanagesubcategory"))

    if action == "update":
        q="select * from subcategory inner join category using(category_id) where subcat_id='%s'"%(subid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update subcategory set subcat_name='%s', subcat_desc='%s' where subcat_id='%s' "%(name,desc,subid)
            update(q)
            return redirect(url_for("admin.adminmanagesubcategory"))
    return render_template('admin_manage_subcategory.html',data=data) 



@admin.route('/adminmanageitems', methods=['GET', 'POST'])
def adminmanageitems():
    data = {}

    # Fetch categories and brands for dropdowns
    data['sub'] = select("SELECT * FROM category")
    data['brand'] = select("SELECT * FROM brand")

    # Check if there's any action from query string
    action = request.args.get('action')
    pid = request.args.get('pid')

    # Handle Delete
    if action == 'delete' and pid:
        delete("DELETE FROM vehicle WHERE vehicle_id='%s'" % pid)
        return redirect(url_for("admin.adminmanageitems"))

    # Handle Status Update
    if action == "available" and pid:
        update("UPDATE vehicle SET status='available' WHERE vehicle_id='%s'" % pid)
        return redirect(url_for("admin.adminmanageitems"))

    if action == "inactive" and pid:
        update("UPDATE vehicle SET status='sold' WHERE vehicle_id='%s'" % pid)
        return redirect(url_for("admin.adminmanageitems"))

    # Handle Pre-Filling for Update
    if action == "update" and pid:
        q = """SELECT * FROM vehicle 
               INNER JOIN category USING(category_id) 
               INNER JOIN brand USING(brand_id) 
               WHERE vehicle_id='%s'""" % pid
        data['up'] = select(q)

    # Handle New Submission
    if 'submit' in request.form:
        bid = request.form['bid']
        subid = request.form['subid']
        manufacture_year = request.form['manufacture_year']
        odo_reading = request.form['odo_reading']
        color = request.form['color']
        price = request.form['price']
        image = request.files['vehicle_img']
        name = request.form['name']
        desc = request.form['desc']
        features = request.form['features']
        status = request.form['status']

        path = "static/uploads/" + str(uuid.uuid4()) + image.filename
        image.save(path)

        # Check for duplicates
        res = select("SELECT * FROM vehicle WHERE vehicle_name='%s'" % name)
        if res:
            flash("Vehicle Already Added....")
        else:
            q = """INSERT INTO vehicle 
                   (brand_id, category_id, manufacture_year, odo_reading, color, price, vehicle_image, 
                   vehicle_name, vehicle_description, features, status) 
                   VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')""" % (
                        bid, subid, manufacture_year, odo_reading, color, price, path, name, desc, features, status)
            insert(q)
            return redirect(url_for("admin.adminmanageitems"))

    # Handle Update Form Submission
    if 'update' in request.form:
        bid = request.form['bid']
        subid = request.form['subid']
        name = request.form['name']
        desc = request.form['desc']
        price = request.form['price']
        features = request.form['features']
        color = request.form['color']
        odo_reading = request.form['odo_reading']
        manufacture_year = request.form['manufacture_year']
        status = request.form['status']

        image = request.files['vehicle_img']
        if image and image.filename != "":
            path = "static/uploads/" + str(uuid.uuid4()) + image.filename
            image.save(path)
            q = """UPDATE vehicle SET brand_id='%s', category_id='%s', vehicle_name='%s', 
                   vehicle_description='%s', price='%s', features='%s', vehicle_image='%s', 
                   manufacture_year='%s', odo_reading='%s', color='%s', status='%s'
                   WHERE vehicle_id='%s'""" % (
                    bid, subid, name, desc, price, features, path,
                    manufacture_year, odo_reading, color, status, pid)
        else:
            q = """UPDATE vehicle SET brand_id='%s', category_id='%s', vehicle_name='%s', 
                   vehicle_description='%s', price='%s', features='%s',
                   manufacture_year='%s', odo_reading='%s', color='%s', status='%s'
                   WHERE vehicle_id='%s'""" % (
                    bid, subid, name, desc, price, features,
                    manufacture_year, odo_reading, color, status, pid)
        update(q)
        return redirect(url_for("admin.adminmanageitems"))

    # Finally, fetch the vehicle list to display
    data['value'] = select("SELECT * FROM vehicle")

    return render_template('admin_manage_item.html', data=data)


@admin.route('/adminmanagepurchase',methods=['get','post'])
def adminmanagepurchase():
    data={}
    q="select * from vendor where status='active'"
    data['ven']=select(q)
    q="select * from product where status='active'"
    data['pro']=select(q)
    if 'submit' in request.form:
        ven=request.form['vid']
        proid=request.form['pro']
        cprice=request.form['cprice']
        qty=request.form['qty']
        total=request.form['total']
        q="select * from product where product_id='%s'"%(proid)
        res=select(q)
        proper=res[0]['profit_per']
        sellp=int(proper)*int(cprice)/100
        selling=int(cprice)+sellp
        q="select * from purchase_master where pstatus='pending' and vendor_id='%s'"%(ven)
        res=select(q)
        if res:
            pmmid=res[0]['pmaster_id']
            q="select * from purchase_details where pmaster_id='%s' and  product_id='%s' and cost_price='%s'"%(pmmid,proid,cprice)
            resq=select(q)
            if resq:
                q="update purchase_master set total_amount=total_amount+'%s' where pmaster_id='%s'"%(total,pmmid)
                insert(q)
                q="update purchase_details set quantity=quantity+'%s' where product_id='%s' and pmaster_id='%s'"%(qty,proid,pmmid)
                update(q)
            else:
                q="update purchase_master set total_amount=total_amount+'%s' where pmaster_id='%s'"%(total,pmmid)
                insert(q)
                q="insert into purchase_details values(null,'%s','%s','%s','%s','%s','available')"%(pmmid,proid,cprice,selling,qty)
                insert(q)
        else:
            q="insert into purchase_master values(null,'%s',0,'pending','%s',now())"%(ven,total)
            id=insert(q)
            q="insert into purchase_details values(null,'%s','%s','%s','%s','%s','available')"%(id,proid,cprice,selling,qty)
            insert(q)
            flash('Product Added to Purchase List...')
            return redirect(url_for('admin.adminmanagepurchase'))
    
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id and pstatus='pending'"
    res=select(q)
    data['res']=select(q)

    if 'btn' in request.form:
        
        
        q="select * from purchase_master inner join purchase_details using(pmaster_id) where pstatus='pending'"
        res=select(q)
        if res:
            for i in res:
                proid=i['product_id']
                sellpingprice=i['selling_price']
                quantity=i['quantity']
                pdetailsid=i['pdetails_id']
                
                q="select * from product where product_id='%s' and stock='0'"%(proid)
                res1=select(q)
                if res1:
                    q="update product set stock='%s',price='%s' where  product_id='%s'"%(quantity,sellpingprice,proid)
                    update(q)
                    q="update purchase_details set st_status='stock added' where pdetails_id='%s'"%(pdetailsid)
                    update(q)
                    q="update purchase_master set pstatus='paid' where pstatus='pending'"
                    update(q)
                    # flash('Purchase Completed...')
                else:
                    q="update purchase_master set pstatus='paid' where pstatus='pending'"
                    update(q)
                flash('Purchase Completed...')
                    
        
        
        
        
        return redirect(url_for('admin.adminmanagepurchase'))
    return render_template('admin_manage_purchase.html',data=data)


@admin.route('/adminviewpur')
def adminviewpur():
    data={}
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id "
    res=select(q)
    data['res']=select(q)
    return render_template('admin_view_purchasedlist.html',data=data)



@admin.route('/adminvieworders')
def adminvieworders():
    data={}
    q="select * from `booking` inner join `customer` using(`customer_id`) inner join `vehicle` using(`vehicle_id`)"
    res=select(q)
    data['res']=select(q)
    return render_template('admin_view_booking.html',data=data)

@admin.route('/adminviewdetails')
def adminviewdetails():
    data={}
    omid=request.args['omid']
    q="select * from `booking` inner join `customer` using(`customer_id`) inner join `vehicle` using(`vehicle_id`) where booking_id='%s'"%(omid)
    res=select(q)
    data['res']=select(q)
    return render_template('admin_view_details.html',data=data)


@admin.route('/adminviewpayment')
def adminviewpayment():
    data={}
    omid=request.args['omid']
    q="SELECT * FROM `payment` INNER JOIN `card` USING(`card_id`) WHERE `booking_id`='%s'"%(omid)
    data['pay']=select(q)
    return render_template('admin_view_payments.html',data=data)



@admin.route("/adminviewcomplaints",methods=['get','post'])
def adminviewcomplaints():

    
    data={}
    q="select * from customer inner join complaint using (customer_id)"
    data['res']=select(q)

    if 'action' in request.args:
        action=request.args['action']
        cid=request.args['cid']
    else:
        action=None

    if action == "reply":
        data['replysec']=True

        if 'submit' in request.form:
            reply=request.form['reply']

            q="update complaint set reply='%s' where complaint_id='%s'"%(reply,cid)
            update(q)
            return redirect(url_for("admin.adminviewcomplaints"))
    return render_template("admin_view_complaints.html",data=data)



@admin.route('/adminviewsales',methods=['get','post'])
def adminviewsales():
    data={}
    q="SELECT * FROM order_master om,order_details od,product p,`customer` u WHERE om.order_master_id=od.order_master_id AND od.product_id=p.product_id AND om.customer_id=u.customer_id  group by om.order_master_id"
    res=select(q)
    data['res']=select(q)
    
    if 'dsch' in request.form:
        dsearch=request.form['dsearch']
        
        q="SELECT * FROM order_master om,order_details od,product p,`customer` u WHERE om.order_master_id=od.order_master_id AND od.product_id=p.product_id AND om.customer_id=u.customer_id and date='%s'  group by om.order_master_id "%(dsearch)
        res=select(q)
        data['res']=select(q)
        
    if 'nsch' in request.form:
        search="%"+request.form['search']+"%"
        q="SELECT * FROM order_master om,order_details od,product p,`customer` u WHERE om.order_master_id=od.order_master_id AND od.product_id=p.product_id AND om.customer_id=u.customer_id and c_fname like '%s'  group by om.order_master_id "%(search)
        res=select(q)
        data['res']=select(q)
    return render_template('admin_view_sales.html',data=data)



@admin.route('/viewcustomer',methods=['get','post'])
def viewcustomer():
    data={}
    q="select * from customer "
    data['viewcus']=select(q)
    
    
    if 'action' in request.args:
        action=request.args['action']
        uname=request.args['uname']
        cid=request.args['cid']
      
    else:
        action=None
    
    
    if action == "active":
        q="update login set status='active' where username='%s' "%(uname)
        update(q)
        q="update customer set c_status='active' where customer_id='%s' "%(cid)
        update(q)
        return redirect(url_for("admin.viewcustomer"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update customer set c_status='inactive' where customer_id='%s' "%(cid)
        update(q)
        return redirect(url_for("admin.viewcustomer"))
    
    if 'sc' in request.form:
        search="%"+request.form['search']+"%"
        q="select * from customer where c_fname like '%s'"%(search)
        data['viewcus']=select(q)
    return render_template('admin_view_customer.html',data=data)




@admin.route('/adminassignorder',methods=['get','post'])
def adminassignorder():
    data={}
    id=request.args['omid']
    data['omid']=id
    q="select * from courier"
    data['res']=select(q)
    
    if 'cid' in request.args:
        cid=request.args['cid']
        id=request.args['omid']
        
        q="select * from delivery where order_master_id='%s'"%(id)
        res=select(q)
        
        if res:
            flash("order already assigned........")
        else:
            q="insert into delivery values(null,'%s','%s',curdate(),'assigned')"%(id,cid)
            insert(q)
            q="update order_master set ostatus='assigned' where order_master_id='%s'"%(id)
            update(q)
            flash("Order Assigned Successfully....")
            return redirect(url_for('admin.adminvieworders'))
    
    return render_template ('admin_assign_orders.html',data=data)
    
    
    
@admin.route('/managebrand',methods=['get','post'])
def managebrand():
    data={}
    s="select * from brand"
    data['value']=select(s)
    if 'brand' in request.form:
        bname=request.form['bname']
        bdescription=request.form['bdescription']
        a="insert into brand values(null,'%s','%s','Active')"%(bname,bdescription)
        insert(a)
        return redirect(url_for('admin.managebrand'))
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        b="delete from brand where brand_id='%s'"%(id)
        delete(b)
        return redirect(url_for('admin.managebrand'))
    if action=='update':
        b="select * from brand where brand_id='%s'"%(id)
        data['up']=select(b)
        
    if 'update' in request.form:
        bname=request.form['bname']
        bdescription=request.form['bdescription']
        b="update brand set brand_name='%s',brand_description='%s' where brand_id='%s'"%(bname,bdescription,id)
        update(b)
        return redirect(url_for('admin.managebrand'))
    return render_template('admin_manage_brand.html',data=data)


@admin.route('/admin_return_request', methods=['GET', 'POST'])
def admin_return_request():
    data = {}
    s = "SELECT *, `return_table`.`status` AS rstatus FROM return_table INNER JOIN booking USING(booking_id) INNER JOIN customer USING(customer_id) INNER JOIN vehicle USING(vehicle_id) WHERE booked_status='cancelled'"
    data['value'] = select(s)
    
    if 'action' in request.args:
        action = request.args['action']
        id = request.args.get('id')
        amount = request.args.get('amount')
    else:
        action = None
    
    if action == 'return' and id:
        # Update return status to 'returned'
        a = "UPDATE return_table SET status='returned' WHERE return_id='%s'" % (id)
        update(a)
        flash('Return request approved successfully.', 'success')
        return redirect(url_for('admin.admin_return_request'))
    
    if action == 'payment' and id and amount:
        # Insert into refund table and update status to 'refund'
        b = "INSERT INTO refund (return_id, amount, date) VALUES ('%s', '%s', CURDATE())" % (id, amount)
        insert(b)
        a = "UPDATE return_table SET status='refund' WHERE return_id='%s'" % (id)
        update(a)
        flash('Refund processed successfully.', 'success')
        return redirect(url_for('admin.admin_return_request'))
    
    if action == 'cancel' and id:
        # Check if status is 'pending' before cancelling
        check_status = "SELECT status FROM return_table WHERE return_id='%s'" % (id)
        result = select(check_status)
        if result and result[0]['status'] == 'pending':
            a = "UPDATE return_table SET status='return cancelled' WHERE return_id='%s'" % (id)
            update(a)
            flash('Return request cancelled successfully.', 'success')
        else:
            flash('Cannot cancel: Return request is not pending.', 'error')
        return redirect(url_for('admin.admin_return_request'))
    
    return render_template('admin_return_request.html', data=data)

@admin.route('/adminviewreport', methods=['GET', 'POST'])
def adminviewreport():
    data = {}

    if request.method == 'POST' and 'dsch' in request.form:
        fdate = request.form.get('fdate', '').strip()
        todate = request.form.get('todate', '').strip()

        if fdate and todate:
            q = f"""
                SELECT b.*, v.vehicle_name, v.vehicle_description, v.vehicle_image, v.price,
                       c.customer_fname, c.customer_lname
                FROM booking b
                JOIN vehicle v ON b.vehicle_id = v.vehicle_id
                JOIN customer c ON b.customer_id = c.customer_id
                WHERE DATE(b.date) BETWEEN '{fdate}' AND '{todate}'
            """
            flash('Booking Report Filtered Successfully', 'success')
        else:
            q = """
                SELECT b.*, v.vehicle_name, v.vehicle_description, v.vehicle_image, v.price,
                       c.customer_fname, c.customer_lname
                FROM booking b
                JOIN vehicle v ON b.vehicle_id = v.vehicle_id
                JOIN customer c ON b.customer_id = c.customer_id
            """
            flash('Showing all booking records', 'info')
    else:
        q = """
            SELECT b.*, v.vehicle_name, v.vehicle_description, v.vehicle_image, v.price,
                   c.customer_fname, c.customer_lname
            FROM booking b
            JOIN vehicle v ON b.vehicle_id = v.vehicle_id
            JOIN customer c ON b.customer_id = c.customer_id
        """

    data['res'] = select(q)
    return render_template('admin_view_report.html', data=data)


