from flask import Flask,render_template,request
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql://root:mysql@localhost/our_users'
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/register')
def about():
    return render_template ('register.html')

@app.route('/login_validation',methods=['Post'])
def login_validation():
    email=request.form.get('email')
    password=request.form.get('password')
    return "The email is {} and the password is {}".format(email,password)

if __name__=="__main__":
    app.run(debug=True)
