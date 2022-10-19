from flask import Flask,request,jsonify
import mysql.connector as conn

#creating app
app = Flask(__name__)

#create connection with mysql
mydb = conn.connect(host='localhost',user='root',passwd='Maahudi@123')
#create cursor
cursor = mydb.cursor()
cursor.execute('create database if not exists taskyug')
cursor.execute('create table if not exists taskyug.mytable(name varchar(30), number int)')

@app.route('/insert', methods=['POST'])
#creating function
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
#Now to execute in database
        cursor.execute('insert into taskyug.mytable values(%s, %s)',(name, number))
        mydb.commit()
        return jsonify(str('successfully inserted'))

#To update records
@app.route('/update',methods=['POST'])
def update():
    if request.method=='POST':
        get_name = request.json['get_name']
        cursor.execute('update taskyug.mytable set number=number+500 where name=%s', (get_name,))
        mydb.commit()
        return jsonify(str('updated'))

#To delete record
@app.route('/delete', methods=['POST'])
def delete():
    if request.method=='POST':
        name_del=request.json['name_del']
        cursor.execute('delete from taskyug.mytable where name=%s', (name_del,))
        mydb.commit()
        return jsonify(str('deleted'))

#function to fetch all record
@app.route('/fetch', methods=['POST'])
def fetch_data():
    l=[]
    cursor.execute('select * from taskyug.mytable')
    for i in cursor.fetchall():
        l.append(i)
    return jsonify(str(l))
if __name__=='__main__':
    app.run()

#Now check database and then insert records
#Insert records via Postman through URL