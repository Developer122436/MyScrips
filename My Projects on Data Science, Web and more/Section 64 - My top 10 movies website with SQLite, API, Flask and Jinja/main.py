import os
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_secret_key')
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///movies.db"
MOVIE_DB_API_KEY = os.getenv('MOVIE_DB_API_KEY', 'default_api_key')
MOVIE_DB_INFO_URL = 'https://api.themoviedb.org/3/movie'
MOVIE_DB_IMAGE_URL = 'https://image.tmdb.org/t/p/w500'

Bootstrap5(app)
db = SQLAlchemy()
db.init_app(app)


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, unique=True, nullable=False)
    year = db.Column(db.Integer)
    description = db.Column(db.Text)
    rating = db.Column(db.Float)
    ranking = db.Column(db.Integer)
    review = db.Column(db.Text)
    img_url = db.Column(db.String)


class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField('Add Movie')


class EditMovieForm(FlaskForm):
    rating = StringField('Rating')
    review = StringField('Review')
    submit = SubmitField('Update')


@app.before_request
def create_tables():
    db.create_all()


@app.route("/", methods=["GET", "POST"])
def home():
    result = db.session.execute(db.select(Movie).order_by(Movie.rating))
    movies = result.scalars().all()

    for i in range(len(movies)):
        movies[i].ranking = len(movies) - i
    db.session.commit()

    return render_template("index.html", movies=movies)


@app.route("/find")
def find():
    movie_api_id = request.args.get("id")

    if not movie_api_id:
        flash("No Movie ID provided.")
        return redirect(url_for("home"))

    movie_api_url = f"{MOVIE_DB_INFO_URL}/{movie_api_id}"
    response = requests.get(movie_api_url, params={"api_key": MOVIE_DB_API_KEY, "language": "en-US"})

    if response.status_code != 200:
        flash("Error fetching data from the MovieDB API.")
        return redirect(url_for("home"))

    data = response.json()

    new_movie = Movie(
        title=data["title"],
        year=data["release_date"].split("-")[0],
        img_url=f"{MOVIE_DB_IMAGE_URL}{data['poster_path']}",
        description=data["overview"]
    )
    db.session.add(new_movie)
    db.session.commit()

    return redirect(url_for("edit", id=new_movie.id))


@app.route("/add", methods=["GET", "POST"])
def add():
    form = AddMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get("https://api.themoviedb.org/3/search/movie", params={"api_key": "f841b381713312e703c4efa41b025774", "query": movie_title})
        if response.status_code == 200:
            data = response.json()
            if "results" in data and data["results"]:
                return render_template("select.html", options=data["results"])
            else:
                flash("No results found.")

    return render_template("add.html", form=form)


@app.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):
    movie = Movie.query.get_or_404(id)
    form = EditMovieForm()

    if form.validate_on_submit():
        movie.rating = form.rating.data
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))

    form.rating.data = movie.rating  # Pre-fill the rating field

    return render_template('edit.html', movie=movie, form=form)


@app.route("/delete/<int:id>", methods=["POST"])  # Changed to use route parameter
def delete(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))


@app.errorhandler(404)
def not_found(e):
    return render_template("404.html"), 404


@app.errorhandler(500)
def internal_error(e):
    db.session.rollback()
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
