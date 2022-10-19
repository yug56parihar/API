from flask import Flask,request,jsonify
#creating object of flask class
app = Flask(__name__)

#way to send data/giving route to data
@app.route('/abc',methods=['GET', 'POST'])
def test1():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a+b
        return jsonify((str(result)))

#creating new route
@app.route('/abc1',methods=['GET','POST'])
def test2():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a * b
        return jsonify((str(result)))

#creating new route
@app.route('/abc3',methods=['GET','POST'])
def test3():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a - b
        return jsonify((str(result)))

#creating new route
@app.route('/abc4',methods=['GET','POST'])
def test4():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a / b
        return jsonify((str(result)))

#creating new route
@app.route('/abc5',methods=['GET','POST'])
def test5():
    if(request.method=='POST'):
        a = request.json['num1']
        b = request.json['num2']
        result = a ** b
        return jsonify((str(result)))


if __name__=='__main__' :
    app.run()


