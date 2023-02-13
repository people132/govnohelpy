from flask import Flask, request, render_template, session, url_for, redirect
import sqlite3
import hashlib
import os
import json
import smtplib
import random



app = Flask(__name__, template_folder='pages')
app.secret_key = os.urandom(20).hex()

@app.route('/qu', methods=['GET', 'POST'])
def qu():
    if 'email' in session:
        print(session['email'])
        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        try:
            log1 = cursor_db.execute(('''SELECT name FROM info
                                               WHERE email = '{}';
                                               ''').format(session['email'])).fetchone()[0]
            log2 = cursor_db.execute(('''SELECT surname FROM info WHERE email = '{}'; ''').format(session['email'])).fetchone()[0]
            log = log1 + ' ' + log2
        except:
            return redirect(url_for('reg'))
        if request.method == 'POST':
            mainSkill = request.form['mainSkill']
            mainHour = request.form['mainHour']
            secondSkill = request.form['secondSkill']
            secondHour = request.form['secondHour']
            workHoure = request.form['workHoure']
            language = ' '.join(request.form.getlist('language'))
            typeConnect = ' '.join(request.form.getlist('typeConnect'))
            db_lp = sqlite3.connect('bases/login_password.db')
            cursor_db = db_lp.cursor()
            sql_insert1 = f'''UPDATE info SET mainSkill = "{mainSkill}",mainHour = "{mainHour}",secondSkill = "{secondSkill}",
                    secondHour = "{secondHour}", language = "{language}", workHoure = "{workHoure}", typeConnect = "{typeConnect}" 
                         WHERE email ="{session['email']}";'''
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
        try:
            session['email'] = request.form['username']
            email = request.form['username']
            password = request.form['password']
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
                print(cur[0], hashlib.sha512(password.encode()).hexdigest())
                if cur[0] != str(hashlib.sha512(password.encode()).hexdigest()):
                    db_lp.close()
                    return redirect(url_for('reg'))
                else:
                    skill = cursor_db.execute(('''SELECT mainSkill FROM info
                                                WHERE email = '{}';
                                                ''').format(session['email'])).fetchone()[0]
                    print(skill)
                    print(type(skill))
                    db_lp.close()
            if skill != '0':
                return  redirect(url_for('account'))
            else:
                return redirect(url_for('qu'))
        except UnboundLocalError:
            return redirect(url_for('reg'))
    return render_template('auth.html')


@app.route('/reg', methods=['GET', 'POST'])
def reg():
    error = 'error'
    error_msg = ''
    code = ''
    surname = ''
    name = ''
    patronymic = ''
    email = ''
    number = ''
    tg = ''
    vk = ''
    password = ''
    if request.method == 'POST':
        if request.form['button'] == 'reg':
            surname = request.form['surname']
            name = request.form['username']
            patronymic = request.form['patronymic']
            email = request.form['email']
            number = request.form['number']
            tg = request.form['tg']
            vk = request.form['vk']
            code = request.form['code']
            password = request.form['password']
            try:
                print(code, session['code'])
                if session['code'] == code:
                    session.pop('code', None)
                    db_lp = sqlite3.connect('bases/login_password.db')
                    cursor_db = db_lp.cursor()
                    print('yes')
                    if cursor_db.execute(f'''SELECT password FROM login_password
                                                    WHERE login = "{email}"''').fetchone() == None:
                        sql_insert = f'''INSERT INTO login_password VALUES('{email}','{str(hashlib.sha512(password.encode()).hexdigest())}');'''
                        sql_insert1 = f'''INSERT INTO info VALUES('{email}','{name}', '{surname}', '{patronymic}', '{number}', '{vk}', '{tg}', '{0}', '{0}', '{0}', '{0}', {0}, {0}, {0}, {0});'''
                        cursor_db.execute(sql_insert)
                        cursor_db.execute(sql_insert1)
                        cursor_db.close()
                        db_lp.commit()
                        db_lp.close()
                        return redirect(url_for('auth'))
                    else:
                        print('no')
                        error = 'error active'
                        error_msg = 'Такой аккаунт уже существует'
                else:
                    error = 'error active'
                    error_msg = 'Код введен не верно'
                    session.pop('code', None)
            except KeyError:
                error = 'error active'
                error_msg = 'отправьте новый код на почту'
        if request.form['button'] == 'code':
            session.pop('code', None)
            surname = request.form['surname']
            name = request.form['username']
            patronymic = request.form['patronymic']
            email = request.form['email']
            number = request.form['number']
            tg = request.form['tg']
            vk = request.form['vk']
            password = request.form['password']
            session['code'] = generate(5)
            letter(email, session['code'])
    return render_template('reg.html', Error_msg = error_msg, Error = error, Surname = surname, Username = name, Patronymic = patronymic, Email = email, Number = number, Tg = tg, Vk = vk, Password = password)


@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect(url_for('auth'))


@app.route('/account')
def account():
    if 'email' in session:
        summ = 0
        db_lp = sqlite3.connect('bases/login_password.db')
        cursor_db = db_lp.cursor()
        Log1 = cursor_db.execute(('''SELECT name FROM info
                                               WHERE email = '{}';
                                               ''').format(session['email'])).fetchone()[0]
        Log2 = cursor_db.execute(('''SELECT surname FROM info
                                               WHERE email = '{}';
                                               ''').format(session['email'])).fetchone()[0]
        Log = Log1 + " " + Log2
        

        #Получаю из базы список email-ов
        Des = cursor_db.execute('''SELECT email FROM history;''').fetchall()
        des3 = []
        #прохожу по списку email-ов
        for i in Des:   
            des3.append(i[0])
        for i in set(des3):
            # получаю описание по взятому email-у
            Des1 = cursor_db.execute(('''SELECT des FROM history WHERE email = '{}';''').format(i)).fetchall()
            #  получаю цену по взятому email-у
            Des2 = cursor_db.execute(('''SELECT pr FROM history WHERE email = '{}';''').format(i)).fetchall()
            des = []
            for j in Des1:
                 # создаю массив с описаниями
                des.append(j[0])
            des1 = []
            for j in Des2:
                 # создаю массив с ценами и датами
                des1.append(j[0])
            for j in des1:
                k = j.index('(')
                l = j[:k]
                summ = summ + int(l)
                print(l)
            des5 = []
            for j in range(len(des)):
                # создаю масив с соответсвующими полями из des и des1
                des6 = [des[j], des1[j]] 
                 # создаю общий массив состоящий из масивов 
                des5.append(des6)
                # создает словарь с индетификаторм email и значением масив
            obj = {i:des5} 
            with open('static/animation/temp1.json', 'w') as f:
                # записывает получившийся словарь в json
                json.dump(obj, f, indent=2) 
        if summ == 0:
            summ = 'Вы бомж'
        db_lp.close()
    return render_template('account.html', Log = Log, Sum = summ, Email = session['email'])


@app.route('/')
def main():
    return render_template('main_page.html')


@app.route('/newpassword',  methods=['GET', 'POST'])
def newpassword():
    if request.method == 'POST':
        code1 = str(request.form['code'])
        print(session['code'], code1)
        if code1 == session['code']:
            print('yes')
            session.pop('code', None)
            return redirect(url_for('qu'))
        else:
            session.pop('code', None)
            print('вы мошеник')
    return render_template('code.html')


@app.route('/sent_accept')
def sent_accept():
    session.pop('code', None)
    code = generate(5)
    letter(session['email'], code)
    session['code'] = code
    return redirect(url_for('reg'))

@app.route('/sentps')
def sent():
    session.pop('code', None)
    code = generate(5)
    letter('kuprvvv@gmail.com', code)
    session['code'] = code
    return redirect(url_for('newpassword'))

def generate(length):
    lower_case = "abcdefghiklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

    Use_for = lower_case + upper_case
    length_for_pass = length
    code = "".join(random.sample(Use_for, length_for_pass))
    return code


def letter(email, ms):
    with smtplib.SMTP_SSL("smtp.gmail.com") as smtp:
        smtp.login('kuprvvv@gmail.com', 'gqrl dbwn gfjf gpmb') #https://myaccount.google.com/apppasswords
        smtp.sendmail('kuprvvv@gmail.com', email, msg = ms)
app.run(debug=True)