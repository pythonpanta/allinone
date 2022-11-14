from flask import Flask,render_template,request
import pickle
app = Flask(__name__)
file=open('modal.pkl','rb')
clf=pickle.load(file)
file.close()

@app.route("/",methods=['GET','POST'])
def hello_world():
    print('hello')
    if request.method=='POST':
        mydict=request.form
        fever=int(mydict['fever'])
        bodypain=int(mydict['bodypain'])
        nose=int(mydict['nose'])
        age=int(mydict['age'])
        dib=int(mydict['dib'])
        inputfeature=[fever,bodypain,age,nose,dib]
        info=clf.predict_proba([inputfeature])[0][1]
        return render_template('result.html',info=round(info*100))
    return render_template('index.html')

if __name__=='__main__':
    app.run(debug=True)