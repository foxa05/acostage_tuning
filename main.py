from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message


app = Flask(__name__)
app.config['SECRET_KEY'] = '1998'

# Configure email settings
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'acostagechiptuning@gmail.com'
app.config['MAIL_PASSWORD'] = 'vqposvxxinoqeglw'  # Use the app password here
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_DEFAULT_SENDER'] = 'acostagechiptuning@gmail.com'


mail = Mail(app)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/services')
def services():
    return render_template('services.html')


@app.route('/gallery')
def gallery():
    return render_template('gallery.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        car_make = request.form['car-make']
        engine_type = request.form['engine-type']
        engine_size = request.form['engine-size']

        msg = Message("Contact Form Submission",
                      recipients=['your_email@example.com'])  # Replace with your email
        msg.body = f"""
        Name: {name}
        Email: {email}
        Car Make: {car_make}
        Engine Type: {engine_type}
        Engine Size: {engine_size}
        Message:
        {message}
        """

        try:
            mail.send(msg)
            flash('Mesaj trimis cu succes!', 'success')
        except Exception as e:
            flash(f'Eroare la trimiterea mesajului!: {e}', 'error')

        return redirect(url_for('contact'))

    return render_template('contact.html')


@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    result = None
    if request.method == 'POST':
        try:
            base_hp = float(request.form['base-hp'])
            engine_type = request.form['engine-type'].lower()

            if engine_type == 'naturally aspirated gas':
                tuning_percentage = 7.5
            elif engine_type == 'turbo diesel':
                tuning_percentage = 25.0
            elif engine_type == 'turbo gas':
                tuning_percentage = 20.0

            result = base_hp * (1 + tuning_percentage / 100)
        except Exception as e:
            return f"An error occurred: {e}"
    return render_template('calculator.html', result=result)


if __name__ == '__main__':
    app.run(debug=True)
