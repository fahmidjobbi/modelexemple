from flask import Flask ,render_template,url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mongoengine import MongoEngine
from flask_pymongo import PyMongo
import uuid
from datetime import datetime
import joblib as joblib
from flask_cors import  CORS
from flask import jsonify
import os


app=Flask(__name__)
CORS(app)
DB_URI="mongodb+srv://FahmiDJOBBI:55046258@cluster0.nraui4d.mongodb.net/API?retryWrites=true&w=majority"
app.config['MONGODB_SETTINGS'] = {
    'db': 'API',
    'host': DB_URI
}
db=MongoEngine()
db.init_app(app)


class Todo(db.Document):
     _id=db.StringField(default=str(uuid.uuid4()),primary_key=True)
     content=db.StringField()
     completed=db.IntField(default=0)
     date_created=db.DateTimeField(default=datetime.utcnow)
     def to_json(self):
         return {
             "id":self._id,
             "content":self.content,
             "completed":self.completed,
             "date_created":self.date_created
         }


@app.route('/',methods=['POST','GET']) #decorator
def index():
    if request.method == 'POST':
        try:
            taskcontent=request.form['task']
            new_task=Todo(
                _id=str(uuid.uuid4()),
                content=taskcontent,
                completed=0,
                date_created=datetime.utcnow()
                )
            print(new_task._id)
            new_task.save()
           
               
            return redirect('/')
        except:
            return 'There was an issue adding your task'
    else:
        tasks=Todo.objects.all()
        return render_template('index.html',tasks=tasks)


@app.route('/delete/<id>')
def delete(id):
    task_to_delete=Todo.objects.get(_id=id)
    try:
        task_to_delete.delete()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

    
@app.route('/update/<id>',methods=['GET','POST'])
def update(id):
    task=Todo.objects.get(_id=id)
    if request.method=='POST':
        task.content=request.form['task']
        try:
            task.save()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html',task=task)
    

@app.route('/predict',methods=['POST','GET'])                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
def classify():

        model=joblib.load('modelhotel.sav')
        #dictionary to label all traffic signs class.
        classes = { 
        'happy':'Good news it was  a happy experience',
        'not happy':'Sorry it was not a happy experience',
 
        }
        if request.method == 'POST':
            
                predictcontent=request.form['predict']
                pred = model.predict([predictcontent])
                sign=classes[pred[0]]
        
                print(sign)
                return render_template('predict.html',sign=sign)
    
                
        else:
            return render_template('predict.html')
        
        
@app.route('/upload-image', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image found', 400

    file = request.files['image']
    file.save(os.path.join(r'C:\Users\Fahmi\dev\Job-e\demo\Back\static\img', file.filename))

    return jsonify({'message': 'Image uploaded successfully!'})
            





if __name__ == '__main__' :
    app.run(debug=True) #debug=True is optional