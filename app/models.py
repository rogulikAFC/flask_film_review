from datetime import datetime

from . import db


class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    image = db.Column(db.String(255), nullable=False)
    reviews = db.relationship('Review', back_populates='movie')

    def get_rate(self):
        ratings = [review.rating for review in self.reviews]
        
        return round(sum(ratings) / len(ratings), 2)
    

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    reviewer_name = db.Column(db.String(255), nullable=False)
    text = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.id'), nullable=False) 
    movie = db.relationship('Movie', back_populates='reviews')   
