from flask import Flask,render_template,request
import sqlite3

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index_3.html')

def db_connection():
    conn = sqlite3.connect('sign.db')
    c = conn.cursor()
    return c
@app.route('/')
def index2():
    return render_template('index_4.html')

#@app.route('/')
#def index():
    #return render_template('sign.db')


@app.route('/signup', methods = ['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['Email']
        nickname = request.form['Nickname']
        password = request.form['Password']
        c = db_connection()
        c.execute('INSERT INTO user (type_user,password,nickname) VALUES (?,?,?)', (email,nickname,password))
        data = c.execute('SELECT * FROM user').fetchall()

        #query = 'SELECT * FROM user WHERE type_user=? AND password=?'
        #result_user = c.execute(query, (email, password)).fetchone()
        #if result_user:
            #return render_template('text.html')'
        #else:
    return render_template('text.html')



if __name__ == '__main__':
    app.run(debug = True)

