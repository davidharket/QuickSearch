from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Email
from flask_sqlalchemy import SQLAlchemy
from search import Search

# SET APP
app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'

# CONNECT TO DATABASE
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///search.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# CONFIGURE TABLE
#class StreamingServices(db.Model):
#    id = db.Column(db.Integer, primay_key=True)
#    name = db.Column(db.String(250), unique=True, nullable=False)
#    price = db.Column(db.Integer, nullable=True)


with app.app_context():
    db.create_all()

#def add_service():
#    form = StreamingServices()
#    new_service = StreamingServices(
#                                    name="Amazon Prime",
#                                    price=99,
#    )
#    db.session.add(new_service)
#    db.session.commit()
#add_service()
@app.route("/", methods=["POST", "GET"])
def home():
    email = None
    if request.method == "POST":
        email = request.form["email"]
        bot = Search()
        bot.check_amazon(email)
        amazon = bot.amazon
        bot.check_netflix(email)
        netflix = bot.netflix
        bot.check_viaplay(email)
        viaplay = bot.viaplay
        bot.check_hbo(email)
        hbo = bot.hbo
        return render_template("index.html", email=email, amazon=amazon, netflix=netflix, viaplay=viaplay, hbo=hbo)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
