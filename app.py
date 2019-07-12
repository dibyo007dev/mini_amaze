from flask import Flask,render_template,request,url_for,redirect,session

app = Flask(__name__)

app.secret_key= 'its_a_session_secret_key'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route('/contact.html')
def contact():
    return render_template('contact.html')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        users = {
            'user1':'123',
            'user2':'124',
            'user3':'125',
            'user4':'126',
            'user5':'127',
            'user6':'128',
        }
        username = request.form['username']
        password = request.form['password']

        if username not in users:
            return "User doesn't exists"

        if users[username] != password:
            return "Password does not match"

        session['username'] = username
        return render_template('index.html', user=f'{username}')

    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('home'))

app.run(debug=True)