from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
import string, random, validators

app = Flask(__name__)
app.secret_key = "supersecretkey"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(10), unique=True, nullable=False)
    visits = db.Column(db.Integer, default=0)

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(chars) for _ in range(length))
        if not URL.query.filter_by(short_url=code).first():
            return code

def is_malicious(url):
    blacklisted_keywords = ['malware', 'phishing', 'virus', 'attack']
    for word in blacklisted_keywords:
        if word in url.lower():
            return True
    return False

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        original_url = request.form.get('url')
        if not validators.url(original_url):
            flash("Invalid URL format!", "danger")
            return redirect(url_for('index'))
        if is_malicious(original_url):
            flash("Malicious URL detected! Cannot shorten.", "danger")
            return redirect(url_for('index'))
        existing = URL.query.filter_by(original_url=original_url).first()
        if existing:
            short_code = existing.short_url
        else:
            short_code = generate_short_code()
            new_url = URL(original_url=original_url, short_url=short_code)
            db.session.add(new_url)
            db.session.commit()
        return render_template('short.html', short_url=request.host_url + short_code)
    return render_template('index.html')

@app.route('/<short_code>')
def redirect_short(short_code):
    url = URL.query.filter_by(short_url=short_code).first_or_404()
    url.visits += 1
    db.session.commit()
    return redirect(url.original_url)

@app.route('/dashboard')
def dashboard():
    urls = URL.query.all()
    return render_template('dashboard.html', urls=urls)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)