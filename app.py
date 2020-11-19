from flask import Flask,render_template,url_for,request,redirect
import pickle
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():
    if request.method=='GET':
        return render_template('index.html')
    else:
        model=pickle.load(open('churn.pkl','rb'))
        score=int(request.form.get("creditscore"))
        geo=int(request.form.get("geography"))
        gen=int(request.form.get("gender"))
        age=int(request.form.get("age"))
        bal=float(request.form.get("balance"))
        np=int(request.form.get("nproducts"))
        cred=int(request.form.get("creditcard"))
        mem=int(request.form.get("member"))
        ten=int(request.form.get("tenure"))
        sal=float(request.form.get("salary"))
        X_in=[[score,geo,gen,age,ten,bal,np,cred,mem,sal]]
        Y=model.predict(X_in)
        if Y[0]==0:
           return render_template('index.html',result="Customer will not leave")
        else:
            return render_template('index.html',result="Customer will leave")

if __name__=='__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)