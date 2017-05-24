import os,sqlite3
from flask import Flask, request, render_template, url_for, flash,redirect,session
from werkzeug.utils import secure_filename

app = Flask(__name__)
app.secret_key = "solcon@123"
db = '/home/vivek/Desktop/ThinkOfIt/solconpower/solcon.db'


@app.route('/')
def index():
	return redirect(url_for('home'))

@app.route('/home')
def home():
   return render_template('home.html')

@app.route('/products')
def products():
   return render_template('products.html')

@app.route('/contact',methods=['GET','POST'])
def contact():
	if request.method=='POST':
		name = request.form['name']
		email = request.form['email']
		message = request.form['message']
		con = sqlite3.connect(db)
		sql = "insert into users values (NULL,'%s','%s','%s')" %(name,email,message)
		print sql
		cursor = con.cursor()
		res = cursor.execute(sql)
		print res.fetchall()
		con.commit()
		data = cursor.execute('select * from users')
		print data.fetchall()
		con.close()
		flash('Our Expert Will Get Back To You Soon........!')
		return redirect(request.url)
	return render_template('contact.html')

@app.route('/products/SolarMeter')
def solarMeter():
   return render_template('home.html')         

@app.route('/products/RoofTop')
def rooftop():
   return render_template('rooftop.html') 

@app.route('/products/WaterPump')
def waterpump():
   return render_template('waterpump.html')    

@app.route('/products/SolarLight')
def solarlight():
   return render_template('solarlight.html')   

if __name__ == '__main__':
    app.run(debug='true',port=8000)    