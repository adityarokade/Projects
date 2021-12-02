from flask import Flask, render_template, request,jsonify
from databasemanagement import cassandramanagement
from werkzeug.utils import redirect
from notification import email_alert
from log import log_info




app = Flask(__name__)


#homepage
@app.route('/', methods=['GET', 'POST']) # To render Homepage
def home_page():
    log_info("hi every one home page")
    return render_template('html/homepage.html')




@app.route('/studentregistration',methods=['GET','POST'])
def studentregistration():
    
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        mobno=int(request.form['mobno'])
        datebirth=request.form['datebirth']
        password=request.form['password']
        
        try:
            my_connection=cassandramanagement()
            conn=my_connection.conection_open()
            log_info("student login data sended to -addmission.studentlogindata")
            my_connection.insert_studentlogindata(conn,email,fname,lname,mobno,datebirth,password)

            return redirect('/login')
        except:
            print("error in studentregistration")

    return render_template('html/studentregistration.html')

@app.route('/falcultyregistration',methods=['GET','POST'])
def falcultyregistration():
    
    if request.method=='POST':
        fname=request.form['fname']
        lname=request.form['lname']
        email=request.form['email']
        mobno=int(request.form['mobno'])
            
        idno=str(request.form['idno'])
        datebirth=request.form['datebirth']
        password=request.form['password']
        try:
            my_connection=cassandramanagement()
            conn=my_connection.conection_open()
            log_info("student login data sended to -addmission.falcultylogindata")
            my_connection.insert_falcultylogindata(conn,email,fname,lname,mobno,idno,datebirth,password)
            
            return redirect('/login')
        except:
            print("Error in falculty registartion")

        
   
    return render_template('html/falcultyregistration.html')

@app.route('/login',methods=['GET','POST'])
def login():
    
   
   
        
    if request.method=='POST':
        my_connection=cassandramanagement()
        conn=my_connection.conection_open()
        username=request.form['username']
        password=request.form['password']
        categary=request.form['radiobu']
        if categary=="falculty":
            l1,l2=my_connection.get_studentlogindata(conn)
            for i in l1:
                if(i==username):
                    global fusername
                    fusername=username
                    user=True
                else:
                    pass
            for j in l2:
                if(j==password):
                    pwd=True
                else:
                    pass
            try:
                if(user==True and pwd==True):
                    log_info("falculty username and password is correct")
                    return redirect('/falculty')
            except:
                log_info("falculty username and password is incorrect")
                print("not valid falcuty")
        else:
            print("student")
            l1,l2=my_connection.get_studentlogindata(conn)
            for i in l1:
                if(i==username):
                    global susername
                    susername=username
                    user=True
                else:
                    pass
            for j in l2:
                if(j==password):
                    pwd=True
                else:
                    pass
            try:
                if(user==True and pwd==True):
                    log_info("student username and password is correct")
                    return redirect('/student')
                else:
                    log_info("student username and password is incorrect")
                    print("NOT valid")
            except:
                print("not valid user")
            
                
        return render_template('html/loginpage.html')
    
      
    return render_template('html/loginpage.html') 



@app.route('/student',methods=['GET','POST'])
def applicationstatus():
    try:

        my_connection=cassandramanagement()
        conn=my_connection.conection_open()
            
        l1=my_connection.get_studentdata(conn,susername)
            
            
        d1=my_connection.get_addmissiondata(conn,susername)
    except:
        print("Error in student page")
        
        # c1=['none']    
# l11=l1,d11=d1,
# <!-- {% if {{data1['applicationstatus']}} is none %} -->
    return render_template('html/student.html',l11=l1,d11=d1)
@app.route('/falculty',methods=['GET','POST'])
def falculty():
    try:
        my_connection=cassandramanagement()
        conn=my_connection.conection_open()
        d1=my_connection.get_falcultydata(conn,fusername)

        a1=my_connection.get_sdataforfal(conn)
            
        b1=[]
        b2=[]
        b3=[]
        for i in a1:
            if i[3]=="none":
                print(i[3])
                b1.append(i)
            elif i[3]=="Approve":
                print(i[3])
                b2.append(i)
            else:
                print(i[3])
                b3.append(i)

        if request.method=='POST':
            global student_email
            student_email=request.form['email']
            email=student_email
            my_connection=cassandramanagement()
            conn=my_connection.conection_open()
            l1=my_connection.get_data_tocheck(conn,email)
                
                


            log_info("data sended to checking ")
            return render_template('html/checkpage.html',d11=l1)
        

        
    except:
        print("Error in falculty page")
    return render_template('html/falculty.html',d11=d1,a11=b1,a22=b2,a33=b3)
@app.route('/check',methods=['GET','POST'])
def check():
    try:

        if request.method=='POST':
            review=request.form['review']
            apponmentdate=request.form['date']
            if apponmentdate !="none":
                subject="addmission form status"
                body="your form is -{},and apponment date is-{}".format(review,apponmentdate)
                to=student_email
                email_alert(subject, body, to)
                log_info("email is sended to student about application status")
                
               
            my_connection=cassandramanagement()
            conn=my_connection.conection_open()
            my_connection.update_addmissionform(conn, review, apponmentdate, student_email)
            return redirect('/falculty')
       
    except:
        return render_template('html/checkpage.html')




@app.route('/form',methods=['POST','GET'])
def form():
    

    if request.method=='POST':
        fullname=request.form['fullname']
        fname=request.form['fname']
        fathereducation=request.form['fathereducation']
        fatherOccupation=request.form['fatherOccupation']
        mname=request.form['mname']
        mothereducation=request.form['mothereducation']
        motherOccupation=request.form['motherOccupation']
        gender=request.form['gender']
        age=int(request.form['age'])
        dob=str(request.form['dob'])
        addher=str(request.form['addher'])
        mob=int(request.form['mob'])
            
        email=str(request.form['email'])
        current_address=str(request.form['current_address'])
        permanent_address=str(request.form['permanent_address'])
        Xthbordname=request.form['Xthbordname']
        Xthpassyear=str(request.form['Xthpassyear'])
        Xthmark=str(request.form['Xthmark'])
        Xthschoolname=request.form['Xthschoolname']
        XIIthbordname=request.form['XIIthbordname']
        XIIthpassyear=str(request.form['XIIthpassyear'])
        XIIthmark=str(request.form['XIIthmark'])
        inpercentage=str(request.form['inpercentage'])
        schoolname=request.form['schoolname']
        XIIthgroup=request.form['XIIthgroup']
        math=str(request.form['math'])
        biology=str(request.form['biology'])
        chemistary=str(request.form['chemistary'])
        physics=str(request.form['physics'])
        coursename=request.form['coursename']
        subcourse=request.form['subcourse']
        applicationstatus="none"
        interview_appointment="none"
        log_info("form data collected")

        try:

            my_connection=cassandramanagement()
            conn=my_connection.conection_open()
            log_info("form data is sended to database")
            my_connection.insert_addmissionformdata(conn,fullname,fname,fathereducation,fatherOccupation,mname,mothereducation,motherOccupation,gender,age,dob,addher,mob,email,current_address,permanent_address,Xthbordname,Xthpassyear,Xthmark,Xthschoolname, XIIthbordname,XIIthpassyear,XIIthmark,inpercentage,schoolname,XIIthgroup,math,biology,chemistary,physics,coursename,subcourse,applicationstatus,interview_appointment)
            
                
            
            return redirect('/student')
        except:
            print("Error in data inserting formdata")
            
            
        


   
    return render_template('html/admissionform.html')
@app.route('/mo',methods=['GET','POST'])
def mo():
    
    if request.method=="POST":
        newcoursename=request.form['newcoursename']
        newcoursetrend=request.form['newcoursetrend']
        try:

            my_connection=cassandramanagement()
            conn=my_connection.conection_open()
            my_connection.modify_course(conn,susername, newcoursename, newcoursetrend)
            subject="course modifying"
            body="your course is now modifyed course={},subcourse={}".format(newcoursename,newcoursetrend)
            to=susername
            email_alert(subject, body, to)
            log_info("course is modifyed")
        except:
            print("Error in updating course")
        

    
    return render_template('html/modifycourse.html')


@app.route('/contact',methods=['GET','POST'])
def contact():
    
    return  render_template('html/contact.html')
   


@app.route('/logout',methods=['GET','POST'])
def logout():
    susername=None
    student_email=None
    fusername=None
    return render_template('html/homepage.html')

if __name__ == '__main__':
    app.run()
