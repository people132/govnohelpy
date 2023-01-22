from flask import Flask, request, render_template, session, url_for, redirect
import sqlite3
import hashlib
import os



app = Flask(__name__, template_folder='pages')
app.secret_key = os.urandom(20).hex()
@app.route('/qu', methods=['GET', 'POST'])
def qu():
    if 'email' in session:
        print(session['email'])
        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        try:
            log = cursor_db.execute(('''SELECT fio FROM info
                                               WHERE login = '{}';
                                               ''').format(session['email'])).fetchone()[0]
        except:
            return redirect(url_for('reg'))
        if request.method == 'POST':
            mainSkill = request.form['mainSkill']
            mainHour = request.form['mainHour']
            secondSkill = request.form['secondSkill']
            secondHour = request.form['secondHour']
            #hgjlfjjfhl
            workHoure = request.form['workHoure']
            language = ' '.join(request.form.getlist('language'))
            typeConnect = ' '.join(request.form.getlist('typeConnect'))

            db_lp = sqlite3.connect('bases/login_password.db')
            cursor_db = db_lp.cursor()
            sql_insert1 = f'''UPDATE info SET mainSkill = "{mainSkill}",mainHour = "{mainHour}",secondSkill = "{secondSkill}",
                    secondHour = "{secondHour}", language = "{language}", workHoure = "{workHoure}", typeConnect = "{typeConnect}" 
                         WHERE login ="{session['email']}";'''

            cursor_db.execute(sql_insert1)

            cursor_db.close()

            db_lp.commit()
            db_lp.close()
            print(mainSkill, mainHour, secondSkill, secondHour, language, typeConnect)
            return redirect(url_for('account'))
        return render_template('qu.html', log=log)
    else:
        return redirect(url_for('auth'))

@app.route('/auth', methods=['GET', 'POST'])
def auth():
    if request.method == 'POST':
        session['email'] = request.form['email']
        email = request.form['email']
        print(email)
        Password = request.form['password']
        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        cur = cursor_db.execute(f'''SELECT password FROM login_password
                                            WHERE login = "{email}"''').fetchone()
        cur1 = cursor_db.execute(f'''SELECT password FROM login_password
                                            WHERE login = "{email}"''').fetchone()
        print(cur1)
        print(cur)
        if cur1 is None:
            print('reg')
            db_lp.close()
            redirect(url_for('reg'))
        else:
            print(cur[0], hashlib.sha512(Password.encode()).hexdigest())
            if cur[0] != str(hashlib.sha512(Password.encode()).hexdigest()):
                db_lp.close()
                return redirect(url_for('reg'))
            else:
                skill = cursor_db.execute(('''SELECT mainSkill FROM info
                                               WHERE login = '{}';
                                               ''').format(session['email'])).fetchone()[0]
                print(skill)
                print(type(skill))
                db_lp.close()

        if skill != '0':
            return  redirect(url_for('account'))
        else:
            print('qu')
            return redirect(url_for('qu'))

    return render_template('auth.html')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']
        phone = request.form['phone']
        fio = request.form['fio']

        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        if cursor_db.execute(f'''SELECT password FROM login_password
                                            WHERE login = "{login}"''').fetchone() == None:
            sql_insert = f'''INSERT INTO login_password VALUES('{login}','{str(hashlib.sha512(password.encode()).hexdigest())}');'''
            sql_insert1 = f'''INSERT INTO info VALUES('{login}','{fio}', '{phone}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}', '{0}');'''

            cursor_db.execute(sql_insert)
            cursor_db.execute(sql_insert1)

            cursor_db.close()

            db_lp.commit()
            db_lp.close()
        return redirect(url_for('auth'))

    return render_template('reg.html')


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('auth'))



@app.route('/neworder')
def neworder():
    db_lp = sqlite3.connect('bases/requeset.db')
    db_lp1 = sqlite3.connect('bases/login_password.db')
    cursor_db_lp = db_lp.cursor()
    cursor_db_lp1 = db_lp1.cursor()
    skill1 = cursor_db_lp1.execute(f'''SELECT mainSkill FROM info WHERE login = '{session['email']}';''').fetchone()[0]
    skill2 = cursor_db_lp1.execute(f'''SELECT mainHour FROM info WHERE login = '{session['email']}';''').fetchone()[0]
    hour1 = cursor_db_lp1.execute(f'''SELECT secondSkill FROM info WHERE login = '{session['email']}';''').fetchone()[0]
    houre2 = cursor_db_lp1.execute(f'''SELECT secondHour FROM info WHERE login = '{session['email']}';''').fetchone()[0]
    email = session['email']
    fio =  cursor_db_lp1.execute(f'''SELECT fio FROM info WHERE login = '{session['email']}';''').fetchone()[0]
    sql_insert = f'''INSERT INTO requeset VALUES('{skill1}','{hour1}','{skill2}','{houre2}','{fio}', '{email}');'''
    print('ready')
    cursor_db_lp.execute(sql_insert)
    cursor_db_lp.close()
    db_lp.commit()
    db_lp.close()
    cursor_db_lp1.close()
    db_lp1.close()
    return redirect(url_for('account'))
#ap
@app.route('/account')
def account():
    if 'email' in session:
        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        Log = cursor_db.execute(('''SELECT fio FROM info
                                               WHERE login = '{}';
                                               ''').format(session['email'])).fetchone()[0]
        db_lp1 = sqlite3.connect('bases/ready.db')
        cursor_db1 = db_lp1.cursor()
        Des = cursor_db1.execute((f'''SELECT description FROM ready WHERE email='{format(session['email'])}';''')).fetchall()
        des1=[]
        for i in Des:
           des1.append(i[0])
        db_lp.close()
        db_lp1.close()                        
        print(Des)
        print(des1)
    return render_template('account.html', Log = Log)
    



app.run(debug=True)