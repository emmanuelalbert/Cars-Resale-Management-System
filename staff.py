from flask import *
from database import *
import uuid

staff=Blueprint('staff',__name__)

@staff.route('/shome')
def shome():

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
    
    
    return render_template('staff_home.html')



# @staff.route('/staffmanagestaff',methods=['get','post'])
# def staffmanagestaff():
#     data={}
#     if 'submit' in request.form:
#         email=request.form['email']
#         password=request.form['password']
#         fname=request.form['fname']
#         lname=request.form['lname']
#         house=request.form['house']
#         street=request.form['street']
#         city=request.form['city']
#         district=request.form['district']
#         # state=request.form['state']
#         pin=request.form['pin']
#         phone=request.form['phone']
#         gender=request.form['gender']
#         dob=request.form['dob']

#         q="select * from login where username='%s'"%(email)
#         res=select(q)
#         if res:
#             flash("Username Already Exist!")
#         else:
#             q="insert into login values ('%s','%s','staff','active')"%(email,password)
#             insert(q)
#             q="insert into staff values (null,'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','inactive')"%(email,fname,lname,house,street,city,district,pin,phone,email,gender,dob)
#             insert(q)
#             return redirect(url_for("staff.staffmanagestaff"))

#     data={}
#     q="select * from staff"
#     data['res']=select(q)


    # if 'action' in request.args:
    #     action=request.args['action']
    #     uname=request.args['uname']
    #     stid=request.args['stid']
      
    # else:
    #     action=None

    # if action == "active":
    #     q="update login set status='active' where username='%s' "%(uname)
    #     update(q)
    #     q="update staff set staff_status='active' where staff_id='%s' "%(stid)
    #     update(q)
    #     return redirect(url_for("staff.staffmanagestaff"))
    # if action == "inactive":
    #     q="update login set status='inactive' where username='%s' "%(uname)
    #     update(q)
    #     q="update staff set staff_status='inactive' where staff_id='%s' "%(stid)
    #     update(q)
    #     return redirect(url_for("staff.staffmanagestaff"))

    # if action == "update":
    #     q="select * from staff where staff_id='%s'"%(stid)
    #     val=select(q)
    #     data['up']=val


    # if 'update' in request.form:
    #     # email=request.form['email']
    #     # password=request.form['password']
    #     fname=request.form['fname']
    #     lname=request.form['lname']
    #     house=request.form['house']
    #     street=request.form['street']
    #     city=request.form['city']
    #     district=request.form['district']
    #     # state=request.form['state']
    #     pin=request.form['pin']
    #     phone=request.form['phone']
    #     gender=request.form['gender']
    #     dob=request.form['dob']

    #     q="update staff set staff_fname='%s', staff_lname='%s', staff_house_name='%s', staff_street='%s', staff_city='%s', staff_dist='%s', staff_pincode='%s', staff_phone='%s', staff_gender='%s', staff_dob='%s' where staff_id='%s' "%(fname,lname,house,street,city,district,pin,phone,gender,dob,stid)
    #     update(q)
    #     return redirect(url_for("staff.staffmanagestaff"))
    # return render_template('staff_manage_staff.html',data=data) 




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

        q="select * from vendor where v_email='%s'"%(email)
        res=select(q)
        if res:
            flash("Alredy Exists......")
        else:
            q="insert into vendor values (null,'0','%s','%s','%s','%s','%s','%s','active')"%(name,email,street,city,pin,phone)
            insert(q)
            return redirect(url_for("staff.staffmanagevendor"))
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
        q="update login set status='active' where username=(select username from courier where courier_id='%s')"%(vid)
        update(q)
        return redirect(url_for("staff.staffmanagecourier"))
    if action == "inactive":
       
        q="update courier set status='inactive' where courier_id='%s' "%(vid)
        update(q)
        q="update login set status='inactive' where username=(select username from courier where courier_id='%s')"%(vid)
        update(q)
        return redirect(url_for("staff.staffmanagecourier"))

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
            return redirect(url_for("staff.staffmanagecourier"))
    return render_template('staff_manage_courier.html',data=data) 



@staff.route('/staffmanagecaterogy',methods=['get','post'])
def staffmanagecaterogy():
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
        q="select * from category where category_id='%s'"%(cat_id)
        val=select(q)
        data['raw']=val

    if 'update' in request.form:
        name=request.form['name']
        desc=request.form['desc']

        q="update category set category_name='%s', category_description='%s' where category_id='%s' "%(name,desc,cat_id)
        update(q)
        return redirect(url_for("staff.staffmanagecaterogy"))
    if action=='delete':
        a="delete from category where category_id='%s'"%(cat_id)
        delete(a)
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
    #     return redirect(url_for("staff.staffmanagesubcategory"))
    # if action == "inactive":
    #     q="update subcategory set status='inactive' where subcategory_id='%s' "%(subid)
    #     update(q)
    #     return redirect(url_for("staff.staffmanagesubcategory"))

    if action == "update":
        q="select * from subcategory inner join category using(category_id) where subcat_id='%s'"%(subid)
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

    q="select * from category "
    data['sub']=select(q)
    s="select * from brand"
    data['brand']=select(s)
    if 'submit' in request.form:
        bid=request.form['bid']
        subid=request.form['subid']
        name=request.form['name']
        desc=request.form['desc']
        # price=request.form['price']
        image=request.files['image']
        prop=request.form['prop']
        speci=request.form['speci']
        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)
        q="select * from vehicle where vehicle_name='%s'"%(name)
        res=select(q)
        if res:
            flash("Already Added....")
        else:
            
            q="insert into vehicle values (null,'%s','%s','%s','%s','%s','%s','%s','available')"%(bid,subid,name,desc,path,prop,speci)
            insert(q)
            return redirect(url_for("staff.staffmanageitems"))


    q="select * from vehicle"
    data['value']=select(q)


    if 'action' in request.args:
        action=request.args['action']
        pid=request.args['pid']

      
    else:
        action=None

    if action == "available":
        q="update vehicle set status='available' where vehicle_id='%s' "%(pid)
        update(q) 
        return redirect(url_for("staff.staffmanageitems"))
    if action == "inactive":
        q="update vehicle set status='sold' where vehicle_id='%s' "%(pid)
        update(q)
        return redirect(url_for("staff.staffmanageitems"))

    if action == "update":
        q="select * from vehicle inner join category using(category_id) inner join brand using(brand_id) where vehicle_id='%s'"%(pid)
        val=select(q)
        data['up']=val
    else:
        action=None

    if 'update' in request.form:
        bid=request.form['bid']
        subid=request.form['subid']
        name=request.form['name']
        desc=request.form['desc']
        # price=request.form['price']
        image=request.files['image']
        prop=request.form['prop']
        speci=request.form['speci']
        path="static/uploads/"+str(uuid.uuid4())+image.filename
        image.save(path)
        print(image.filename)
        if image.filename == "":
            q="update vehicle set vehicle_name='%s', vehicle_description='%s',features='%s',specification='%s'  where vehicle_id='%s' "%(name,desc,prop,speci,pid)
            update(q)
        else:
            q="update vehicle set vehicle_name='%s', vehicle_description='%s' , vehicle_image='%s',features='%s',specification='%s' where vehicle_id='%s' "%(name,desc,path,prop,speci,pid)
            update(q)
        return redirect(url_for("staff.staffmanageitems"))
    if action=='delete':
        a="delete from vehicle where vehicle_id='%s'"%(pid)
        delete(a)
        return redirect(url_for("staff.staffmanageitems"))
    return render_template('staff_manage_item.html',data=data) 

@staff.route('/staffmanagepurchase',methods=['get','post'])
def staffmanagepurchase():
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
            return redirect(url_for('staff.staffmanagepurchase'))
    
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
                    
        
        
        
        
        return redirect(url_for('staff.staffmanagepurchase'))
    return render_template('staff_manage_purchase.html',data=data)


@staff.route('/staffviewpur')
def staffviewpur():
    data={}
    q="SELECT * FROM purchase_master pm,purchase_details pd,product p,vendor v WHERE pm.pmaster_id=pd.pmaster_id AND pd.product_id=p.product_id AND pm.vendor_id=v.vendor_id "
    res=select(q)
    data['res']=select(q)
    return render_template('staff_view_purchasedlist.html',data=data)



@staff.route('/staffvieworders',methods=['get','post'])
def staffvieworders():
    data={}
    q="select * from `booking` inner join `customer` using(`customer_id`) inner join `vehicle` using(`vehicle_id`)"
    res=select(q)
    data['res']=select(q)
    if 'action' in request.args:
        action=request.args['action']
        omid=request.args['omid']
    else:
        action=None
    if action=='deliver':
        a="update booking set booked_status='delivered' where booking_id='%s'"%(omid)
        update(a)
        return redirect(url_for('staff.staffvieworders'))
    return render_template('staff_view_booking.html',data=data)

@staff.route('/staffviewdetails')
def staffviewdetails():
    data={}
    omid=request.args['omid']
    q="select * from `booking` inner join `customer` using(`customer_id`) inner join `vehicle` using(`vehicle_id`) where booking_id='%s'"%(omid)
    res=select(q)
    data['res']=select(q)
    return render_template('staff_view_details.html',data=data)


@staff.route('/staffviewpayment')
def staffviewpayment():
    data={}
    omid=request.args['omid']
    q="SELECT * FROM `payment` INNER JOIN `card` USING(`card_id`) WHERE `booking_id`='%s'"%(omid)
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



@staff.route('/staffviewsales',methods=['get','post'])
def staffviewsales():
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
    return render_template('staff_view_sales.html',data=data)



@staff.route('/viewcustomer',methods=['get','post'])
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
        return redirect(url_for("staff.viewcustomer"))
    if action == "inactive":
        q="update login set status='inactive' where username='%s' "%(uname)
        update(q)
        q="update customer set c_status='inactive' where customer_id='%s' "%(cid)
        update(q)
        return redirect(url_for("staff.viewcustomer"))
    
    if 'sc' in request.form:
        search="%"+request.form['search']+"%"
        q="select * from customer where c_fname like '%s'"%(search)
        data['viewcus']=select(q)
    return render_template('staff_view_customer.html',data=data)




@staff.route('/staffassignorder',methods=['get','post'])
def staffassignorder():
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
            return redirect(url_for('staff.staffvieworders'))
    
    return render_template ('staff_assign_orders.html',data=data)
    
    
    
@staff.route('/staffmanagebrand',methods=['get','post'])
def managebrand():
    data={}
    s="select * from brand"
    data['value']=select(s)
    if 'brand' in request.form:
        bname=request.form['bname']
        bdescription=request.form['bdescription']
        a="insert into brand values(null,'%s','%s','Active')"%(bname,bdescription)
        insert(a)
        return redirect(url_for('staff.managebrand'))
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
    else:
        action=None
    if action=='delete':
        b="delete from brand where brand_id='%s'"%(id)
        delete(b)
        return redirect(url_for('staff.managebrand'))
    if action=='update':
        b="select * from brand where brand_id='%s'"%(id)
        data['up']=select(b)
        
    if 'update' in request.form:
        bname=request.form['bname']
        bdescription=request.form['bdescription']
        b="update brand set brand_name='%s',brand_description='%s' where brand_id='%s'"%(bname,bdescription,id)
        update(b)
        return redirect(url_for('staff.managebrand'))
    return render_template('staff_manage_brand.html',data=data)


@staff.route('/staff_return_request',methods=['get','post'])
def staff_return_request():
    data={}
    s="select *,`return_table`.`status` AS rstatus from return_table inner join booking using(booking_id) inner join customer using(customer_id) inner join vehicle using(vehicle_id) where booked_status='cancelled'"
    data['value']=select(s)
    if 'action' in request.args:
        action=request.args['action']
        id=request.args['id']
        amount=request.args['amount']
    else:
        action=None
    if action=='return':
        a="update return_table set status='returned' where return_id='%s'"%(id)
        update(a)
        return redirect(url_for('staff.staff_return_request'))
    if action=='payment':
        b="insert into refund values(null,'%s','%s',curdate())"%(id,amount)
        insert(b)
        a="update return_table set status='refund' where return_id='%s'"%(id)
        update(a)
        return redirect(url_for('staff.staff_return_request'))
    
    return render_template('staff_return_request.html',data=data)