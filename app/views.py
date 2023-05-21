from flask import render_template, redirect, url_for, request

from werkzeug.utils import secure_filename

from . import app, db
from .models import Movie, Review
from .forms import MovieForm, ReviewForm


@app.route('/')
def index():
    movies = Movie.query.all()

    return render_template('index.html', movies=movies)

@app.route('/movie/<id>', methods=['GET', 'POST'])
def movie(id):
    movie = Movie.query.get(id)
    form = ReviewForm()

    if form.validate_on_submit():
        review = Review()

        review.reviewer_name = form.name.data
        review.text = form.text.data
        review.rating = form.rating.data

        review.movie_id = id

        db.session.add(review)
        db.session.commit()

    return render_template('movie.html', movie=movie, form=form)

@app.route('/add_movie', methods=['GET', 'POST'])
def add_movie():
    form = MovieForm()

    if form.validate_on_submit():
        movie = Movie()
        
        movie.title = form.title.data
        movie.description = form.description.data

        upload_folder = app.config['IMAGE_UPLOAD_FOLDER']
        
        image = form.image.data
        image_name = secure_filename(image.filename)
        image.save(f'{upload_folder}/{image_name}')
        movie.image = image_name

        db.session.add(movie)
        db.session.commit()

    return render_template('add_movie.html', form=form)

@app.route('/manage_reviews')
def manage_reviews():
    reviews = Review.query.all()

    return render_template('reviews.html', reviews=reviews)

@app.route('/delete_review/<movie_id>')
def delete_review(movie_id):
    review = Review.query.get(movie_id)
    db.session.delete(review)
    db.session.commit()

    return redirect(
        url_for('manage_reviews')
    )

if __name__ == '__main__':
    app.run(debug=True)
