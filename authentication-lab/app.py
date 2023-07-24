from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/signout' , methods=['GET','POST'])
def signout():
    login_session['user']=""
    return redirect(url_for('signin'))

@app.route('/', methods=['GET', 'POST'])
def signin():
    error = ""
    if request.method=='POST':
        try: 
            login_session['user']=auth.sign_in_with_email_and_password(request.form['email'] ,request.form['password'])
            return redirect(url_for('add_tweet'))        
        except:
            error="auth error"
    return render_template("signin.html" , error = error)



@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error= ""
    if request.method == 'POST':
        try: 
            login_session['user'] = auth.create_user_with_email_and_password(request.form['email'] ,request.form['password'])
            return redirect(url_for('add_tweet'))
        except:
            error = "auth error"
    return render_template("signup.html" , error = error)


@app.route('/add_tweet', methods=['GET', 'POST'])
def add_tweet():
    return render_template("add_tweet.html")

Config = {
    "apiKey": "AIzaSyABkRKeFBOffKXpU5N1ww1RDbPIboHmchM",
    "authDomain": "labtime-7afa9.firebaseapp.com",
    "projectId": "labtime-7afa9",
    "storageBucket": "labtime-7afa9.appspot.com",
    "messagingSenderId": "254101586962",
    "appId": "1:254101586962:web:aba5aeb5945b63b0e704cb",
    "measurementId": "G-4PQNRTGY1Q",
    "databaseURL":""
}
firebase = pyrebase.initialize_app(Config)
auth = firebase.auth()


if __name__ == '__main__':
    app.run(debug=True)