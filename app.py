
from flask import Flask,jsonify,render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
import datetime
import re
import time

app = Flask(__name__)
app.secret_key = "flash_message"

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'rhu_juban'
global_user_id = 0
mysql = MySQL(app)
@app.route('/')
def Index():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient")
    data = cur.fetchall()
    cur.close()

    return render_template('index.html',patient = data)

def return_anthony():
    return 'Anthony'


@app.context_processor
def context_processor():
    return dict(key='value')





@app.route('/nurse_records/<string:id_data>', methods = ['POST','GET'])
def nurse_records(id_data):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient_individual WHERE id = %s", (id_data,))
    data = cur.fetchall()
    cur.close()
    print(data)
    return render_template('nurse_records.html', patient=data)


@app.route('/nurse_insert', methods = ['POST'])
def nurse_insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")
        id_data = request.form['id_data']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        birthday = request.form['birthday']
        age = request.form['age']
        sex = str(request.form.get('sex'))
        cs = request.form['cs']
        phic = request.form['phic']
        address = request.form['address']
        chief_complaints = request.form['chief_complaints']
        weight = request.form['weight']
        height = request.form['height']
        bp = request.form['bp']
        tt = request.form['tt']
        pr = request.form['pr']
        rr = request.form['rr']
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        full_name = first_name + " " + middle_name + " " + last_name

        cur = mysql.connection.cursor()
        sql = "INSERT INTO patient_individual (id,first_name,middle_name ,last_name,age, sex, cs, phic, address,chief_complaints,weight,height,bp,t,pr,rr,patient_date,birthday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,(id_data,first_name,middle_name,last_name,age,sex,cs,phic,address,chief_complaints,weight,height,bp,tt,pr,rr,date,birthday))
        mysql.connection.commit()
#

        cur = mysql.connection.cursor()
        query= """
                   UPDATE patient
                   SET first_name=%s,middle_name=%s,last_name=%s,age=%s,sex=%s,cs=%s,phic=%s,address=%s,chief_complaints=%s,weight=%s,height=%s,bp=%s,t=%s,pr=%s,rr=%s,patient_date=%s,birthday=%s
                   WHERE id=%s
                """
        cur.execute(query,(first_name,middle_name,last_name,age,sex,cs,phic,address,chief_complaints,weight,height,bp,tt,pr,rr,date,birthday,id_data))
        mysql.connection.commit()


        return redirect(url_for('Patient'))


@app.route('/nurse_print',methods = ['POST'])
def nurse_print():
    if request.method == "POST":
        date_now = request.form['date_now']
        print(date_now)
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM patient_individual WHERE MONTH(patient_date) = MONTH(%s) AND YEAR(patient_date) = YEAR(%s)",(date_now,date_now,))
        monthly = cur.fetchall()
        cur.close()

        cur_2 = mysql.connection.cursor()
        cur_2.execute(
            "SELECT * FROM patient_individual WHERE YEAR(patient_date) = YEAR(%s)",(date_now,))
        yearly = cur_2.fetchall()
        cur_2.close()

        cur_3 = mysql.connection.cursor()
        cur_3.execute(
            "SELECT * FROM patient_individual WHERE DATE(patient_date) = DATE(%s)",(date_now,))
        daily = cur_3.fetchall()
        cur_3.close()

        cur_4 = mysql.connection.cursor()
        cur_4.execute(
            "SELECT * FROM patient_individual WHERE QUARTER(patient_date)=1 ")
        quarter_1 = cur_4.fetchall()
        cur_4.close()

        cur_5 = mysql.connection.cursor()
        cur_5.execute(
            "SELECT * FROM patient_individual WHERE QUARTER(patient_date)=2 ")
        quarter_2 = cur_5.fetchall()
        cur_5.close()

        cur_6 = mysql.connection.cursor()
        cur_6.execute(
            "SELECT * FROM patient_individual WHERE QUARTER(patient_date)=3 ")
        quarter_3 = cur_6.fetchall()
        cur_6.close()

        cur_7 = mysql.connection.cursor()
        cur_7.execute(
            "SELECT * FROM patient_individual WHERE QUARTER(patient_date)=4 ")
        quarter_4 = cur_7.fetchall()
        cur_7.close()

    return render_template('nurse_report.html',date_now = date_now, monthly=monthly,daily=daily,yearly=yearly,quarter_1=quarter_1,quarter_2=quarter_2,quarter_3=quarter_3,quarter_4=quarter_4)



@app.route('/individual')
def individual():
    date_now = datetime.datetime.today().strftime('%Y-%m-%d')
    cur = mysql.connection.cursor()
    cur.execute( "SELECT * FROM patient WHERE DATE(patient_date) = DATE(%s)",(date_now,))
    data = cur.fetchall()
    cur.close()

    return render_template('individual.html',patient = data)

@app.route('/individual_records/<string:id_data>', methods = ['POST','GET'])
def individual_records(id_data):

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient_individual WHERE id = %s ORDER BY key_code DESC",(id_data,))
    data = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT account_name FROM user WHERE id = %s", (global_user_id,))
    name = cur.fetchall()
    cur.close()


    print(data)
    print(name)
    print(global_user_id)
    return render_template('individual_records.html', individual=data, doc=name)

@app.route('/individual_records_update',methods = ['POST'])
def individual_records_update():
    if request.method == "POST":
        individual_id = request.form['individual_id']

        individual_impressions = request.form['individual_impressions']
        individual_management = request.form['individual_management']



        cur_2 = mysql.connection.cursor()
        query= """
                   UPDATE patient_individual
                   SET management=%s,treatment=%s
                   WHERE key_code=%s
                """
        cur_2.execute(query,(individual_impressions,individual_management,individual_id))
        mysql.connection.commit()


        cur= mysql.connection.cursor()
        query= """
                   UPDATE patient
                   SET management=%s,treatment=%s
                   WHERE id=%s
                """
        cur.execute(query,(individual_impressions,individual_management,individual_id))
        mysql.connection.commit()

        return redirect(url_for('individual'))

@app.route('/individual_sort_atoz')
def individual_sort_atoz():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient ORDER BY first_name")
    data = cur.fetchall()
    cur.close()
    return render_template('individual.html', patient=data)

@app.route('/individual_sort_date')
def individual_sort_date():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient ORDER BY id")
    data = cur.fetchall()
    cur.close()
    return render_template('individual.html', patient=data)

@app.route('/individual_search', methods = ['POST'])
def individual_search():
    if request.method == "POST":
        search = request.form['search']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM patient WHERE patient_code LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR middle_name LIKE %s ",("%" + search + "%","%" + search + "%","%" + search + "%","%" + search + "%",))
        data = cur.fetchall()
        cur.close()
    return render_template('individual.html', patient=data)

@app.route('/verify_login',methods = ['POST'])
def verify_login():
    test_cur = mysql.connection.cursor()
    test_cur.execute("SELECT * FROM user")
    test_data = test_cur.fetchall()
    test_cur.close()

    redirect_location = 'Login'
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']

    for arr in test_data:
        for i in range(0,len(arr)):
            account_type = arr[3]
            if arr[1] == username and arr[2] == password and account_type == 'admin':
                global_user_id = int(arr[0])
                redirect_location = 'Admin'
            elif arr[1] == username and arr[2] == password and account_type == 'nurse':
                global_user_id = int(arr[0])
                redirect_location = 'Patient'
            elif arr[1] == username and arr[2] == password and account_type == 'pharmacist':
                global_user_id = int(arr[0])
                redirect_location = 'Inventory'
            elif arr[1] == username and arr[2] == password and account_type == 'doctor':
                global_user_id = int(arr[0])
                redirect_location = 'individual'

    print(redirect_location)
    return redirect(url_for(redirect_location))


@app.route('/login')
def Login():
    return render_template('login.html')

@app.route('/patient')
def Patient():
    date_now = '2019-01-01'
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient")
    data = cur.fetchall()
    cur.close()

    return render_template('patient_2.html',patient = data)


@app.route('/patient_print',methods = ['POST'])
def patient_print():
    if request.method == "POST":
        date_now = request.form['date_now']
        print(date_now)
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM patient WHERE MONTH(patient_date) = MONTH(%s) AND YEAR(patient_date) = YEAR(%s)",(date_now,date_now,))
        monthly = cur.fetchall()
        cur.close()

        cur_2 = mysql.connection.cursor()
        cur_2.execute(
            "SELECT * FROM patient WHERE YEAR(patient_date) = YEAR(%s)",(date_now,))
        yearly = cur_2.fetchall()
        cur_2.close()

        cur_3 = mysql.connection.cursor()
        cur_3.execute(
            "SELECT * FROM patient WHERE DATE(patient_date) = DATE(%s)",(date_now,))
        daily = cur_3.fetchall()
        cur_3.close()

        cur_4 = mysql.connection.cursor()
        cur_4.execute(
            "SELECT * FROM patient WHERE QUARTER(patient_date)=1 ")
        quarter_1 = cur_4.fetchall()
        cur_4.close()

        cur_5 = mysql.connection.cursor()
        cur_5.execute(
            "SELECT * FROM patient WHERE QUARTER(patient_date)=2 ")
        quarter_2 = cur_5.fetchall()
        cur_5.close()

        cur_6 = mysql.connection.cursor()
        cur_6.execute(
            "SELECT * FROM patient WHERE QUARTER(patient_date)=3 ")
        quarter_3 = cur_6.fetchall()
        cur_6.close()

        cur_7 = mysql.connection.cursor()
        cur_7.execute(
            "SELECT * FROM patient WHERE QUARTER(patient_date)=4 ")
        quarter_4 = cur_7.fetchall()
        cur_7.close()

    return render_template('patient_report.html',date_now = date_now, monthly=monthly,daily=daily,yearly=yearly,quarter_1=quarter_1,quarter_2=quarter_2,quarter_3=quarter_3,quarter_4=quarter_4)


@app.route('/invoice_print',methods = ['POST'])
def invoice_print():
    if request.method == "POST":
        date_now = request.form['date_now']
        cur = mysql.connection.cursor()
        cur.execute(
            "SELECT * FROM med_release WHERE MONTH(date_released) = MONTH(%s) AND YEAR(date_released) = YEAR(%s)",(date_now,date_now,))
        monthly = cur.fetchall()
        cur.close()

        cur_2 = mysql.connection.cursor()
        cur_2.execute(
            "SELECT * FROM med_release WHERE YEAR(date_released) = YEAR(%s)",(date_now,))
        yearly = cur_2.fetchall()
        cur_2.close()

        cur_3 = mysql.connection.cursor()
        cur_3.execute(
            "SELECT * FROM med_release WHERE DATE(date_released) = DATE(%s)",(date_now,))
        daily = cur_3.fetchall()
        cur_3.close()

        cur_4 = mysql.connection.cursor()
        cur_4.execute(
            "SELECT * FROM med_release WHERE QUARTER(date_released)=1 ")
        quarter_1 = cur_4.fetchall()
        cur_4.close()

        cur_5 = mysql.connection.cursor()
        cur_5.execute(
            "SELECT * FROM med_release WHERE QUARTER(date_released)=2 ")
        quarter_2 = cur_5.fetchall()
        cur_5.close()

        cur_6 = mysql.connection.cursor()
        cur_6.execute(
            "SELECT * FROM med_release WHERE QUARTER(date_released)=3 ")
        quarter_3 = cur_6.fetchall()
        cur_6.close()

        cur_7 = mysql.connection.cursor()
        cur_7.execute(
            "SELECT * FROM med_release WHERE QUARTER(date_released)=4 ")
        quarter_4 = cur_7.fetchall()
        cur_7.close()

    return render_template('medicine_report.html',date_now = date_now, monthly=monthly,daily=daily,yearly=yearly,quarter_1=quarter_1,quarter_2=quarter_2,quarter_3=quarter_3,quarter_4=quarter_4)



@app.route('/patient_sort_atoz')
def patient_sort_atoz():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient ORDER BY last_name")
    data = cur.fetchall()
    cur.close()
    return render_template('patient.html', patient=data)

@app.route('/patient_sort_date')
def patient_sort_date():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM patient ORDER BY id DESC")
    data = cur.fetchall()
    cur.close()
    return render_template('patient.html', patient=data)

@app.route('/patient_search', methods = ['POST'])
def patient_search():
    if request.method == "POST":
        search = request.form['search']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM patient WHERE patient_code LIKE %s OR first_name LIKE %s OR last_name LIKE %s OR middle_name LIKE %s ",("%" + search + "%","%" + search + "%","%" + search + "%","%" + search + "%",))
        data = cur.fetchall()
        cur.close()

    return render_template('patient.html', patient=data)








@app.route('/patient_delete/<string:id_data>', methods = ['POST','GET'])
def patient_delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM patient WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Patient'))


@app.route('/patient_insert', methods = ['POST'])
def patient_insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")

        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        birthday = request.form['birthday']
        age = request.form['age']
        sex = str(request.form.get('sex'))
        cs = request.form['cs']
        phic = request.form['phic']
        address = request.form['address']
        chief_complaints = request.form['chief_complaints']
        weight = request.form['weight']
        height = request.form['height']
        bp = request.form['bp']
        tt = request.form['tt']
        pr = request.form['pr']
        rr = request.form['rr']
        date = datetime.datetime.today().strftime('%Y-%m-%d')


        cur = mysql.connection.cursor()
        sql = "INSERT INTO patient (first_name,middle_name ,last_name,age, sex, cs, phic, address,chief_complaints,weight,height,bp,t,pr,rr,patient_date,birthday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,(first_name,middle_name,last_name,age,sex,cs,phic,address,chief_complaints,weight,height,bp,tt,pr,rr,date,birthday))
        mysql.connection.commit()
        print('insert data in patient table done :)')

        cur_data = mysql.connection.cursor()
        cur_data.execute("SELECT * FROM patient ORDER BY id")
        data = cur_data.fetchall()
        cur_data.close()
        last_arr = []
        for arr in data:
            last_arr = arr
        print(last_arr)
        print(last_arr[0])
        id_data = last_arr[0]


        cur_2 = mysql.connection.cursor()
        sql = "INSERT INTO patient_individual (id,first_name,middle_name ,last_name,age, sex, cs, phic, address,chief_complaints,weight,height,bp,t,pr,rr,patient_date,birthday) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur_2.execute(sql,(id_data,first_name,middle_name,last_name,age,sex,cs,phic,address,chief_complaints,weight,height,bp,tt,pr,rr,date,birthday))
        mysql.connection.commit()
        print('insert data in patient_individual_table done :)')

        return redirect(url_for('Patient'))

@app.route('/patient_update',methods=['POST'])
def patient_update():
    if request.method == 'POST':
        id_data = request.form['id']
        #patient_code = request.form['patient_code']
        first_name = request.form['first_name']
        middle_name = request.form['middle_name']
        last_name = request.form['last_name']
        birthday = request.form['birthday']
        age = request.form['age']
        sex = str(request.form.get('sex'))
        cs = request.form['cs']
        phic = request.form['phic']
        address = request.form['address']
        chief_complaints = request.form['chief_complaints']
        weight = request.form['weight']
        height = request.form['height']
        bp = request.form['bp']
        tt = request.form['tt']
        pr = request.form['pr']
        rr = request.form['rr']
        cur = mysql.connection.cursor()
        query= """
                   UPDATE patient
                   SET first_name=%s,middle_name=%s,last_name=%s,age=%s,sex=%s,cs=%s,phic=%s,address=%s,chief_complaints=%s,weight=%s,height=%s,bp=%s,t=%s,pr=%s,rr=%s,birthday=%s
                   WHERE id=%s
                """
        cur.execute(query,(first_name,middle_name,last_name,age,sex,cs,phic,address,chief_complaints,weight,height,bp,tt,pr,rr,birthday,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Patient'))

@app.route('/inventory')
def Inventory():

    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM medicine")
    data = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT first_name FROM patient")
    first_name = cur.fetchall()
    cur.close()

    cur = mysql.connection.cursor()
    cur.execute("SELECT last_name FROM patient")
    last_name = cur.fetchall()
    cur.close()

    full_name = []
    for i in range(0,len(first_name)):
        temp_fname = str(first_name[i]) + ' ' + str(last_name[i])
        temp_fname = re.sub('[\(\)\{\}<>]', '', temp_fname)

        full_name.append(temp_fname)

    full_name = sorted(full_name)


    return render_template('inventory.html',medicine = data,full_name = full_name)

@app.route('/inventory_sort_atoz')
def inventory_sort_atoz():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM medicine ORDER BY medicine_name")
    data = cur.fetchall()
    cur.close()
    return render_template('inventory.html', medicine=data)

@app.route('/inventory_sort_date')
def inventory_sort_date():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM medicine ORDER BY id")
    data = cur.fetchall()
    cur.close()
    return render_template('inventory.html', medicine=data)

@app.route('/inventory_sort_exp_date')
def inventory_sort_exp_date():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM medicine ORDER BY exp_date")
    data = cur.fetchall()
    cur.close()
    return render_template('inventory.html', medicine=data)

@app.route('/inventory_search', methods = ['POST'])
def inventory_search():
    if request.method == "POST":
        search = request.form['search']
        cur = mysql.connection.cursor()
        #cur.execute("SELECT * FROM medicine WHERE medicine_name LIKE %s",("%" + search + "%",))
        cur.execute("SELECT * FROM medicine WHERE medicine_name LIKE %s OR batch LIKE %s OR unit LIKE %s",("%" + search + "%","%" + search + "%","%" + search + "%",))
        data = cur.fetchall()
        cur.close()

    return render_template('inventory.html', medicine=data)



@app.route('/med_delete/<string:id_data>', methods = ['POST','GET'])
def med_delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM medicine WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Inventory'))

@app.route('/med_insert', methods = ['POST'])
def med_insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")

        medicine_name = request.form['medicine_name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        description = request.form['description']
        batch = request.form['batch']
        exp_date = request.form['exp_date']
        unit_price = request.form['unit_price']
        amount = request.form['amount']
        date = datetime.datetime.today().strftime('%Y-%m-%d')
        cur = mysql.connection.cursor()
        sql = "INSERT INTO medicine (medicine_name,quantity,unit,description,batch,exp_date,unit_price,amount,en_date) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        cur.execute(sql,(medicine_name,quantity,unit,description,batch,exp_date,unit_price,amount,date))
        mysql.connection.commit()
        return redirect(url_for('Inventory'))

@app.route('/med_update',methods=['POST'])
def med_update():
    if request.method == 'POST':
        id_data = request.form['id']
        medicine_name = request.form['medicine_name']
        quantity = request.form['quantity']
        unit = request.form['unit']
        description = request.form['description']
        batch = request.form['batch']
        exp_date = request.form['exp_date']
        unit_price = request.form['unit_price']
        amount = request.form['amount']


        cur = mysql.connection.cursor()
        query= """
                   UPDATE medicine
                   SET medicine_name=%s,quantity=%s,unit=%s,description=%s,batch=%s,exp_date=%s,unit_price=%s,amount=%s
                   WHERE id=%s
                """
        cur.execute(query,(medicine_name,quantity,unit,description,batch,exp_date,unit_price,amount,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Inventory'))


@app.route('/med_release',methods=['POST'])
def med_release():
    if request.method == 'POST':
        id_data = request.form['id']
        medicine_name = request.form['medicine_name']
        quantity = request.form['quantity']
        quantity_to_release = request.form['quantity_to_release']
        released_to = request.form['released_to']
        exp_date = request.form['exp_date']
        date = datetime.datetime.today().strftime('%Y-%m-%d')

        if int(quantity) < int(quantity_to_release):
            flash("CANNOT RELEASE QUANTITY , LACK OF STOCK!!")
        else:
            left = int(quantity) - int(quantity_to_release)
            cur = mysql.connection.cursor()
            query = """
                                    UPDATE medicine
                                    SET quantity=%s
                                    WHERE id=%s
                                 """
            cur.execute(query, (left, id_data))
            flash("RELEASE SUCCESSFUL!")
            mysql.connection.commit()

            cur_2 = mysql.connection.cursor()
            sql = "INSERT INTO med_release (medicine_name,quantity_released,released_to,exp_date,date_released) VALUES (%s,%s,%s,%s,%s)"
            cur_2.execute(sql,(medicine_name,quantity_to_release,released_to,exp_date,date))
            mysql.connection.commit()

        return redirect(url_for('Inventory'))






@app.route('/admin')
def Admin():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user ORDER BY username")
    data = cur.fetchall()
    cur.close()
    return render_template('admin.html',user = data)

@app.route('/admin_sort_atoz')
def admin_sort_atoz():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user ORDER BY username")
    data = cur.fetchall()
    cur.close()
    cur.close()
    return render_template('admin.html', user=data)

@app.route('/admin_sort_date')
def admin_sort_date():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user ORDER BY id")
    data = cur.fetchall()
    cur.close()
    cur.close()
    return render_template('admin.html', user=data)


@app.route('/admin_sort_account_type')
def admin_sort_account_type():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM user ORDER BY account_type")
    data = cur.fetchall()
    cur.close()
    cur.close()
    return render_template('admin.html', user=data)

@app.route('/admin_search', methods = ['POST'])
def admin_search():
    if request.method == "POST":
        search = request.form['search']
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM user WHERE username LIKE %s",("%" + search + "%",))
        data = cur.fetchall()
        cur.close()
        cur.close()

    return render_template('admin.html', user=data)


@app.route('/admin_delete/<string:id_data>', methods = ['POST','GET'])
def admin_delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM user WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Admin'))

@app.route('/admin_insert', methods = ['POST'])
def admin_insert():
    if request.method == "POST":
        flash("Data Inserted Successfully")

        username = request.form['username']
        password = request.form['password']
        account_type = str(request.form.get('account_type'))
        account_name = request.form['account_name']
        cur = mysql.connection.cursor()

        sql = "INSERT INTO user (username,password,account_type,account_name) VALUES (%s,%s,%s,%s)"

        cur.execute(sql,(username,password,account_type,account_name))
        mysql.connection.commit()

        return redirect(url_for('Admin'))

@app.route('/admin_update',methods=['POST'])
def admin_update():
    if request.method == 'POST':
        id_data = request.form['id']
        username = request.form['username']
        password = request.form['password']
        account_type = str(request.form.get('account_type'))
        account_name = request.form['account_name']

        cur = mysql.connection.cursor()
        query= """
                   UPDATE user
                   SET username=%s,password=%s,account_type=%s,account_name=%s
                   WHERE id=%s
                """
        cur.execute(query,(username,password,account_type,account_name,id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Admin'))

if __name__ == '__main__':
    app.run(debug=True)
