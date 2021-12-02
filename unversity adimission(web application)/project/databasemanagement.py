import cassandra

from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from notification import email_alert




class cassandramanagement:
    def __init__(self):
        pass
#connection
    def conection_open(self):
        try:
            cloud_config= {
            'secure_connect_bundle': 'secure-connect-aditya.zip'}
            auth_provider = PlainTextAuthProvider('YUurZHRYhUKJrXdlPBPaFbCP', '39tbgput7JNL01ixFCwRLRwQ+7Ya,NsB,MqRv56G.Cd4h80nYR69ALKaE77cS6ZKxxh.MXQ7E7iQaH20LBb2EyLyuh-9G-ZCfO_nZ5r9a1q3jIKYs7CP39.bfw.ekY18')
            cluster = Cluster(cloud=cloud_config, auth_provider=auth_provider)
            session = cluster.connect()
            print("connection secssecful")
            return session
            
        except:
            print("Error occured in connection")
    
#create table to create table studentlogin
    def create_tabel_studentlogin(self):
        try:

            query = "CREATE TABLE addmission.studentlogindata(email text PRIMARY KEY,fname text,lname text,mobno varint,datebirth text,password text)"
            self.session.execute(query)
            print("table created-slogin")
        except:
            print("Error occured in creating table-")
    

    def create_table_falcultylogin(self):
        try:
            query = "CREATE TABLE addmission.falcultylogindata(email text PRIMARY KEY,fname text,lname text,mobno varint,idno text,datebirth text,password text)"
            self.session.execute(query)
        except:
            print("Error occured in create table falculty")


    def create_table_admissionform(self):
        try:

            
            query="CREATE TABLE addmission.formdata(fullname text,fname text,fathereducation text,fatherOccupation text,mname text,mothereducation text,motherOccupation text,gender text,age int,dob text,addher text PRIMARY KEY,mob int,email text,current_address text,permanent_address text,Xthbordname text,Xthpassyear text,Xthmark text,Xthschoolname text,XIIthbordname text,XIIthpassyear text,XIIthmark text,inpercentage text,schoolname text,XIIthgroup text,math text,biology text,chemistary text,physics text,coursename text,subcourse text,applicationstatus text,interview_appointment text);"
            self.session.execute(query)
            print("table create addmission")
        except:
            print("Error occured in create table-formdata")
#insert data in table
    def insert_studentlogindata(self,conn,email,fname,lname,mobno,datebirth,password):
       
        self.conn=conn
        self.email=email
        self.fname=fname
        self.lname=lname
        self.mobno=mobno
        self.datebirth=datebirth
        self.password=password
        try:

            session=self.conn
            session.execute("insert into addmission.studentlogindata(email,fname,lname,mobno,datebirth,password) values(%s,%s,%s,%s,%s,%s)",[self.email,self.fname,self.lname,self.mobno,self.datebirth,self.password])
           
            
            subject="registartion completed"
            body="your registration is done ,you can login using Email:-{},and Password :-{}".format(self.email,self.password)
            to=self.email
            email_alert(subject, body, to)
        except:
            print("Error in insert_studentlogindata")  
        
        
    def insert_falcultylogindata(self,conn,email,fname,lname,mobno,idno,datebirth,password):
        self.conn=conn
        self.email=email
        self.fname=fname
        self.lname=lname
        self.mobno=mobno
        self.idno=idno
        self.datebirth=datebirth
        self.password=password
        try:

            session=self.conn
            session.execute("insert into addmission.falcultylogindata(email,fname,lname,mobno,idno,datebirth,password) values(%s,%s,%s,%s,%s,%s,%s)",[self.email,self.fname,self.lname,self.mobno,self.idno,self.datebirth,self.password])
            print("good -falculty registration")
        except:
            print("error in insert_falcultylogindata")

    def insert_addmissionformdata(self,conn,fullname,fname,fathereducation,fatherOccupation,mname,mothereducation,motherOccupation,gender,age,dob,addher,mob,email,current_address,permanent_address,Xthbordname,Xthpassyear,Xthmark,Xthschoolname, XIIthbordname,XIIthpassyear,XIIthmark,inpercentage,schoolname,XIIthgroup,math,biology,chemistary,physics,coursename,subcourse,applicationstatus,interview_appointment):
        try:
            self.conn=conn
            self.fullname=fullname
            self.fname=fname
            self.fathereducation=fathereducation
            self.fatherOccupation=fatherOccupation
            self.mname=mname
            self.mothereducation=mothereducation
            self.motherOccupation=motherOccupation
            self.gender=gender
            self.age=int(age)
            self.dob=dob
            self.addher=addher
            self.mob=int(mob)
            self.email=email
            self.current_address=current_address
            self.permanent_address=permanent_address
            self.Xthbordname=Xthbordname
            self.Xthpassyear=Xthpassyear
            self.Xthmark=Xthmark
            self.Xthschoolname=Xthschoolname
            self.XIIthbordname=XIIthbordname
            self.XIIthpassyear=XIIthpassyear
            self.XIIthmark=XIIthmark
            self.inpercentage=inpercentage
            self.schoolname=schoolname
            self.XIIthgroup=XIIthgroup
            self.math=math
            self.biology=biology
            self.chemistary=chemistary
            self.physics=physics
            self.coursename=coursename
            self.subcourse=subcourse
            self.applicationstatus=applicationstatus
            self.interview_appointment=interview_appointment

        
            session=self.conn
            session.execute("insert into addmission.formdata(fullname,fname,fathereducation,fatherOccupation,mname,mothereducation,motherOccupation,gender,age,dob,addher,mob,email,current_address,permanent_address,Xthbordname,Xthpassyear,Xthmark,Xthschoolname,XIIthbordname,XIIthpassyear,XIIthmark,inpercentage,schoolname,XIIthgroup,math,biology,chemistary,physics,coursename,subcourse,applicationstatus,interview_appointment) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",[self.fullname,self.fname,self.fathereducation,self.fatherOccupation,self.mname,self.mothereducation,self.motherOccupation,self.gender,self.age,self.dob,self.addher,self.mob,self.email,self.current_address,self.permanent_address,self.Xthbordname,self.Xthpassyear,self.Xthmark,self.Xthschoolname,self.XIIthbordname,self.XIIthpassyear,self.XIIthmark,self.inpercentage,self.schoolname,self.XIIthgroup,self.math,self.biology,self.chemistary,self.physics,self.coursename,self.subcourse,self.applicationstatus,self.interview_appointment])
            print("good-form data")
            subject="form filling"
            body="Form filling is done"
            to=self.email
            email_alert(subject, body, to)
            
        except:
            print("Error in inserting formdata in database")

           
#get data from table
    def get_studentlogindata(self,conn):
        try:
            self.conn=conn
            session=self.conn
            query="SELECT email,password FROM addmission.studentlogindata "
            data1=session.execute(query)
            l1=[]
            l2=[]
            for i in data1:
                l1.append(i[0])
                l2.append(i[1])
            return l1,l2

        except:
            print("Error in geting student data in ")

    def get_studentdata(self,conn,susername):
        try:
            self.conn=conn
            self.susername=susername
            session=self.conn
            
            data1=session.execute("select email,fname,lname,mobno,datebirth from addmission.studentlogindata WHERE email=%s ",[self.susername])
            l1=[]
            
            for i in data1:
                l1.append(i)
                
            return l1
        except:
            print("Error in student data-reg")

    def get_falcultylogindata(self,conn):
        try:
            self.conn=conn
            session=self.conn
            query="SELECT email,password FROM addmission.falcultylogindata "
            data1=session.execute(query)
            l1=[]
            l2=[]
            for i in data1:
                l1.append(i[0])
                l2.append(i[1])
            return l1,l2

        except:
            print("Error in geting data in ")

    def get_falcultydata(self,conn,fusername):
        self.conn=conn
        self.fusername=fusername

        try:
            session=self.conn
            data1=session.execute("SELECT email,fname,lname,idno FROM addmission.falcultylogindata WHERE email=%s",[self.fusername])
            l1=[]
            
            for i in data1:
                l1.append(i)
                
            return l1
        except:
            print("Error in get fdata")

    def get_addmissiondata(self,conn,susername):
        try:
            self.conn=conn
            self.susername=susername
            session=self.conn
            data1=session.execute("SELECT coursename,subcourse,applicationstatus,interview_appointment FROM addmission.formdata WHERE email=%s",[self.susername])
            l1=[]
            
            for i in data1:
                l1.append(i)
                
            return l1
        except:
            print("error in get form data")


    def get_data_tocheck(self,conn,email):
        self.conn=conn
        self.email=email
        session=self.conn
        try:
            data1=session.execute("SELECT fullname,fname,fathereducation,fatherOccupation,mname,mothereducation,motherOccupation,gender,age,dob,addher,current_address,permanent_address,Xthbordname,Xthpassyear,Xthmark,Xthschoolname,XIIthbordname,XIIthpassyear,XIIthmark,inpercentage,schoolname,XIIthgroup,math,biology,chemistary,physics,coursename,subcourse FROM addmission.formdata WHERE email=%s",[self.email])

            l1=[]
            

            for i in data1:
                l1.append(i)
                
                


            return l1
        except:
            print("error in get data to check")

    def get_sdataforfal(self,conn):
        self.conn=conn
        try:
            session=self.conn
            data1=session.execute("SELECT fullname,coursename,email,applicationstatus FROM addmission.formdata ")
            l1=[]
            
            for i in data1:
                l1.append(i)
              
            return l1

        except:
            print("Error in sdataforfu1")
    
   

 
    

#update data
    def update_addmissionform(self,conn,review,apponmentdate,student_email):
        self.conn=conn
        self.review=review
        self.apponmentdate=apponmentdate
        self.student_email=student_email
        try:
            session=self.conn
            
            prepare_st= "update addmission.formdata SET applicationstatus= ?,interview_appointment= ? where email= ? ;"
            prepare_ud= session.prepare(prepare_st)
            session.execute(prepare_ud,[self.review,self.apponmentdate,self.student_email])
        except:
            print("Error in updata data")



    def modify_course(self,conn,email,newcoursename,newcoursetrend):
        try:
            self.conn=conn
            self.email=email
            self.newcoursename=newcoursename
            self.newcoursetrend=newcoursetrend

            session=self.conn

            prepare_st= "update addmission.formdata SET coursename= ?,subcourse= ? where email= ? ;"
            prepare_ud= session.prepare(prepare_st)
            session.execute(prepare_ud,[self.newcoursename,self.newcoursetrend,self.email])

        except:
            print("Error in modify the course")

