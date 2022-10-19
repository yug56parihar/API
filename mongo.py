from flask import Flask, request,jsonify
import pymongo

#creating connection
app=Flask(__name__)

client = pymongo.MongoClient("mongodb+srv://yug56parihar:Maahudi123@cluster0.3xprftk.mongodb.net/?retryWrites=true&w=majority")
db = client['taskdb']
collection = db['taskcollection']

#creating function for inserting data
@app.route('/insert/mongo', methods=['POST'])
def insert():
    if request.method=='POST':
        name = request.json['name']
        number = request.json['number']
        collection.insert_one({name:number})
        return jsonify(str('inserted'))
@app.route('/update/mongo', methods=['POST'])
def update():
    if request.method=='POST':
        get_name = request.json['get_name']
        collection.insert_one({get_name})
        return jsonify(str('updated'))

if __name__ == '__main__':
    app.run(port=5001)  #port no is optional you want to give or not