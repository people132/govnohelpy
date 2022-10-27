from flask import Flask, request, render_template, session, url_for, redirect
import sqlite3
import hashlib

app = Flask(__name__, template_folder='pages')


@app.route('/authorization', methods=['GET', 'POST'])
def form_authorization():

   if request.method == 'POST':
       Login = request.form.get('Login')
       Password = request.form.get('Password')
#       session['login'] = Login


       db_lp = sqlite3.connect('bases/login_password.db')
       cursor_db = db_lp.cursor()
       cursor_db.execute(('''SELECT password FROM login_password
                                               WHERE login = '{}';
                                               ''').format(Login))
       pas = cursor_db.fetchall()

       cursor_db.close()
       try:
           if pas[0][0] != Password:
               return render_template('auth_bad.html')
       except:
           return render_template('auth_bad.html')

       db_lp.close()
       return render_template('successfulauth.html')

   return render_template('authorization.html')

@app.route('/registration', methods=['GET', 'POST'])
def form_registration():

   if request.method == 'POST':
       Login = request.form.get('Login')
       Password = request.form.get('Password')
       Phone = request.form.get('Phone')
       FIO = request.form.get('FIO')
       Password1 = hashlib.sha512(Password.encode()).hexdigest()

       db_lp = sqlite3.connect('bases/login_password.db')
       cursor_db = db_lp.cursor()
       sql_insert = '''INSERT INTO login_password VALUES('{}','{}');'''.format(Login, Password1)
       sql_insert1 = '''INSERT INTO info VALUES('{}','{}', '{}');'''.format(Login, FIO, Phone)


       cursor_db.execute(sql_insert)
       cursor_db.execute(sql_insert1)

       cursor_db.close()

       db_lp.commit()
       db_lp.close()

       return render_template('successfulregis.html')

   return render_template('registration.html')


if __name__ == "__main__":
 app.run()