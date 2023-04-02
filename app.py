import login as lg
from flask import Flask,render_template,request
import pickle


# print("check")
with open("model1.pkl","rb") as f:
    #   print("check5")
      model= pickle.load(f)

app = Flask(__name__)
# print("print")


@app.route("/")
def login():
    # print("main")
    return render_template("login.html")

# print("check2")
@app.route("/auth",methods =["POST"])
def auth():
    # print("check3")
    user = request.form["usern"]
    password1 = request.form["pwd"]
    # print("trfu")
    username,password = lg.getcredentials()
    if user in username:
       if password1 in password:
            return render_template("home.html")
    else:
        return render_template("login.html",error ="invalid username or password")
    # print("if/else")
    
    
@app.route("/predict",methods=["POST"])
def predict():
    features= [float(i) 
                for i in 
                (request.form.values())]
    pred = model.predict([(features)])
    pred = str(pred)
    pred = pred[1:-1]
    return render_template("result.html",
                           value=pred)
    
if __name__ == "__main__":
    # print("check4")
    app.run(debug=True, port = 3300)