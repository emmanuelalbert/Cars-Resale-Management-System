from flask import *
from database import *
import uuid

staff=Blueprint('staff',__name__)

@staff.route('/adhome')
def staffhome():

    return render_template('staff_home.html')



@staff.route('/staffmanagestaff',methods=['get','post'])
def staffmanagestaff():
    data={}
    if 'submit' in request.form:
        email=request.form['email']
        password=request.form['password']
        fname=request.form['fname']
        lname=request.form['lname']
        house=request.form['house']
        street=request.form['street']
        city=request.form['city']
        district=request.form['district']
        # state=request.form['state']
        pin=request.form['pin']
        phone=request.form['phone']
        gender=request.form['gender']
        dob=request.form['dob']

        q="select * from login where username='%s'"%(email)
        res=select(q)
        if res:
            flash("Username Already Exist!")
        else:
            q="insert into login values ('%s','%s','staff','inactive')"%(email,password)
            insert(q)
            q="insert into staff values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','inactive')"%(email,fname,lname,house,street,city,district,pin,phone,email,gender,dob)
            insert(q)
            return redirect(url_for("staff.staffmanagestaff"))

    data={}
    q="select * from staff"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        uname=request.args['uname']
        stid=request.args['stid']
      
    else:
        action=None

    if action == "active":
        q="update login set status='active' where username='%s' "%(uname)
        update(q)
        q="update staff set staff_status='active' where staff_id='%s' "%(stid)
        update(q)
        return redirect(url_for("staff.staffmanagestaff"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update staff set staff_status='inactive' where staff_id='%s' "%(stid)
        update(q)
        return redirect(url_for("staff.staffmanagestaff"))

    if action == "update":
        q="select * from staff where staff_id='%s'"%(stid)
        val=select(q)
        data['staff']=val


        if 'update' in request.form:
            # email=request.form['email']
            # password=request.form['password']
            fname=request.form['fname']
            lname=request.form['lname']
            house=request.form['house']
            street=request.form['street']
            city=request.form['city']
            district=request.form['district']
            # state=request.form['state']
            pin=request.form['pin']
            phone=request.form['phone']
            gender=request.form['gender']
            dob=request.form['dob']

            q="update staff set staff_fname='%s', staff_lname='%s', staff_housename='%s', staff_street='%s', staff_city='%s', staff_dist='%s', staff_pincode='%s', staff_phone='%s', staff_gender='%s', staff_dob='%s' where staff_id='%s' "%(fname,lname,house,street,city,district,pin,phone,gender,dob,stid)
            update(q)
            return redirect(url_for("staff.staffmanagestaff"))
    return render_template('staff_manage_staff.html',data=data) 




@staff.route('/staffmanagevendor',methods=['get','post'])
def staffmanagevendor():
    data={}
    if 'submit' in request.form:
       
        email=request.form['email']
        name=request.form['vname']
       
     
        street=request.form['street']
        city=request.form['city']
       
  
        pin=request.form['pin']
        phone=request.form['phone']
    

       
        q="insert into vendor values (null,'%s','%s','%s','%s','%s','%s','%s','inactive')"%(session['sid'],name,email,street,city,pin,phone)
        insert(q)
        return redirect(url_for("staff.staffmanagevendor"))
    data={}
    q="select * from vendor"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        vid=request.args['vid']
   
      
    else:
        action=None

    if action == "active":
      
        q="update vendor set status='active' where vendor_id='%s' "%(vid)
        update(q)
        return redirect(url_for("staff.staffmanagevendor"))
    if action == "inactive":
       
        q="update vendor set status='inactive' where vendor_id='%s' "%(vid)
        update(q)
        return redirect(url_for("staff.staffmanagevendor"))

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
            return redirect(url_for("staff.staffmanagevendor"))
    return render_template('staff_manage_vendor.html',data=data) 



@staff.route('/staffmanagecourier',methods=['get','post'])
def staffmanagecourier():
    data={}
    if 'submit' in request.form:
       
        email=request.form['email']
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

            q="insert into courier values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','inactive')"%(session['sid'],uname,name,email,street,city,state,pin,phone)
            insert(q)
        return redirect(url_for("staff.staffmanagecourier"))
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
        return redirect(url_for("staff.staffmanagecourier"))
    if action == "inactive":
       
        q="update courier set status='inactive' where courier_id='%s' "%(vid)
        update(q)
        return redirect(url_for("staff.staffmanagecourier"))

    if action == "update":
        q="select * from courier where courier_id='%s'"%(vid)
        val=select(q)
        data['cour']=val

        if 'update' in request.form:
           
            email=request.form['email']
            name=request.form['cname']
        
        
            street=request.form['street']
            city=request.form['city']
        
    
            pin=request.form['pin']
            phone=request.form['phone']
        
          
            state=request.form['state']

            q="update courier set cour_name='%s', cour_street='%s', cour_city='%s', cour_pincode='%s', cour_phone='%s',cour_email='%s',cour_state='%s' where courier_id='%s' "%(name,street,city,pin,phone,email,state,vid)
            update(q)
            return redirect(url_for("staff.staffmanagecourier"))
    return render_template('staff_manage_courier.html',data=data) 



@staff.route('/staffmanagecaterogy',methods=['get','post'])
def staffmanagecaterogy():
    data={}
    if 'submit' in request.form:
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into category values (null,'%s','%s')"%(name,desc)
        insert(q)
        return redirect(url_for("staff.staffmanagecaterogy"))

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
    #     return redirect(url_for("staff.staffmanagecaterogy"))
    # if action == "inactive":
    #     q="update category set status='inactive' where category_id='%s' "%(cat_id)
    #     update(q)
    #     return redirect(url_for("staff.staffmanagecaterogy"))

    if action == "update":
        q="select * from category where cat_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update category set cat_name='%s', cat_desc='%s' where cat_id='%s' "%(name,desc,cat_id)
            update(q)
            return redirect(url_for("staff.staffmanagecaterogy"))
    return render_template('staff_manage_category.html',data=data) 



@staff.route('/staffmanagesubcategory',methods=['get','post'])
def staffmanagesubcategory():
    data={}

    q="select * from category  "
    data['cat']=select(q)
    if 'submit' in request.form:
        catid=request.form['catid']
        name=request.form['name']
        desc=request.form['desc']
    
        q="insert into subcategory values (null,'%s','%s','%s')"%(catid,name,desc)
        insert(q)
        return redirect(url_for("staff.staffmanagesubcategory"))


    q="select * from subcategory inner join category using (cat_id)"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        subid=request.args['subid']

      
    else:
        action=None

    # if action == "active":
    #     q="update subcategory set status='active' where subcategory_id='%s' "%(subid)
    #     update(q) 
    #     return redirect(url_for("staff.staffmanagesubcategory"))
    # if action == "inactive":
    #     q="update subcategory set status='inactive' where subcategory_id='%s' "%(subid)
    #     update(q)
    #     return redirect(url_for("staff.staffmanagesubcategory"))

    if action == "update":
        q="select * from subcategory inner join category using(cat_id) where subcat_id='%s'"%(subid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']

            q="update subcategory set subcat_name='%s', subcat_desc='%s' where subcat_id='%s' "%(name,desc,subid)
            update(q)
            return redirect(url_for("staff.staffmanagesubcategory"))
    return render_template('staff_manage_subcategory.html',data=data) 



@staff.route('/staffmanageitems',methods=['get','post'])
def staffmanageitems():
    data={}

    q="select * from subcategory "
    data['sub']=select(q)

    if 'submit' in request.form:
        subid=request.form['subid']
        name=request.form['name']
        desc=request.form['desc']
        # price=request.form['price']
        image=request.files['image']
        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)
    
        q="insert into product values (null,'%s','%s','%s','%s',0,'active')"%(subid,name,desc,path)
        insert(q)
        return redirect(url_for("staff.staffmanageitems"))


    q="select * from product"
    data['res']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid']

      
    else:
        action=None

    if action == "active":
        q="update product set status='active' where product_id='%s' "%(pid)
        update(q) 
        return redirect(url_for("staff.staffmanageitems"))
    if action == "inactive":
        q="update product set status='inactive' where product_id='%s' "%(pid)
        update(q)
        return redirect(url_for("staff.staffmanageitems"))

    if action == "update":
        q="select * from product where product_id='%s'"%(pid)
        val=select(q)
        data['raw']=val

        if 'update' in request.form:
            name=request.form['name']
            desc=request.form['desc']
            # price=request.form['price']
            image=request.files['image']
            path="static/uploads/"+str(uuid.uuid4())+image.filename
            image.save(path)
            print(image.filename)
            if image.filename == "":
                q="update product set product_name='%s', product_desc='%s'  where product_id='%s' "%(name,desc,pid)
                update(q)
            else:
                q="update product set product_name='%s', product_desc='%s' , product_image='%s' where product_id='%s' "%(name,desc,path,pid)
                update(q)
            return redirect(url_for("staff.staffmanageitems"))
    return render_template('staff_manage_item.html',data=data) 

@staff.route('/staffmanagepurchase',methods=['get','post'])
def staffmanagepurchase():
    data={}
    q="select * from vendor"
    data['ven']=select(q)
    q="select * from product"
    data['pro']=select(q)
    if 'submit' in request.form:
        ven=request.form['vid']
        proid=request.form['pro']
        cprice=request.form['cprice']
        qty=request.form['qty']
        total=request.form['total']
        selling=request.form['selling']
        q="select * from purchase_master where pstatus='pending'"
        res=select(q)
        if res:
            pmmid=res[0]['pmaster_id']
            q="select * from purchase_details where pmaster_id='%s' and  product_id='%s'"%(pmmid,proid)
            resq=select(q)
            if resq:
                q="update purchase_master set total_amount=total_amount+'%s' where pmaster_id='%s'"%(total,pmmid)
                insert(q)
                q="update purchase_details set quantity=quantity+'%s' where product_id='%s' and pmaster_id='%s'"%(qty,proid,pmmid)
                update(q)
            else:
                q="update purchase_master set total_amount=total_amount+'%s' where pmaster_id='%s'"%(total,pmmid)
                insert(q)
                q="insert into purchase_details values(null,'%s','%s','%s','%s','%s')"%(pmmid,proid,cprice,selling,qty)
                insert(q)
        else:
            q="insert into purchase_master values(null,'%s',%s,'pending','%s',now())"%(ven,session['sid'],total)
            id=insert(q)
            q="insert into purchase_details values(null,'%s','%s','%s','%s','%s')"%(id,proid,cprice,selling,qty)
            insert(q)
            flash('Product Added to Purchase List...')
            return redirect(url_for('staff.staffmanagepurchase'))
    
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id and pstatus='pending'"
    res=select(q)
    data['res']=select(q)

    if 'btn' in request.form:
        q="update purchase_master set pstatus='paid' where pstatus='pending'"
        update(q)
        flash('Purchase Completed...')
        return redirect(url_for('staff.staffmanagepurchase'))
    return render_template('staff_manage_purchase.html',data=data)


@staff.route('/staffviewpur')
def staffviewpur():
    data={}
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id "
    res=select(q)
    data['res']=select(q)
    return render_template('staff_view_purchasedlist.html',data=data)



@staff.route('/staffvieworders')
def staffvieworders():
    data={}
    q="SELECT * FROM order_master om,order_details od,product p,`customer` u WHERE om.order_master_id=od.order_master_id AND od.product_id=p.product_id AND om.customer_id=u.customer_id and ostatus<>'pending' group by om.order_master_id"
    res=select(q)
    data['res']=select(q)
    return render_template('staff_view_booking.html',data=data)

@staff.route('/staffviewdetails')
def staffviewdetails():
    data={}
    omid=request.args['omid']
    q="SELECT * FROM order_master om,order_details od,product p,`customer` u WHERE om.order_master_id=od.order_master_id AND od.product_id=p.product_id AND om.customer_id=u.customer_id and ostatus<>'pending' and om.order_master_id='%s'"%(omid)
    res=select(q)
    data['res']=select(q)
    return render_template('staff_view_details.html',data=data)


@staff.route('/staffviewpayment')
def staffviewpayment():
    data={}
    omid=request.args['omid']
    q="SELECT * FROM payment p,card c,order_master om WHERE p.card_id=c.card_id AND p.order_master_id=om.order_master_id AND p.order_master_id='%s'"%(omid)
    data['pay']=select(q)
    return render_template('staff_view_payments.html',data=data)



@staff.route("/staffviewcomplaints",methods=['get','post'])
def staffviewcomplaints():

    
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
            return redirect(url_for("staff.staffviewcomplaints"))
    return render_template("staff_view_complaints.html",data=data)


