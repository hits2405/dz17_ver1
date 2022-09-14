from flask import Flask, request
from flask_restx import Api, Resource


from config import app, db
from models import Movie
from shemas import MovieSchema

api = Api(app)

movie_ns = api.namespace('movies')
director_ns = api.namespace('directors')
genre_ns = api.namespace('genres')


@movie_ns.route("/")
class MoviesViews(Resource):
    def get(self):
        director_id = request.args.get('director_id')
        genre_id = request.args.get('genre_id')
        query = Movie.query
        if director_id:
            query = query.filter(Movie.director_id == director_id)
        if genre_id:
            query = query.filter(Movie.genre_id == genre_id)

        return MovieSchema(many=True).dump(query.all()), 200

    def post(self):
        data = request.json
        try:
            db.session.add(
                Movie(**data)
            )
            db.session.commit()
            return "Load Try"
        except Exception as e:
            print(e)
            db.session.rollback() #rollback - это отмена записи, лучше делать обвязку через тру
            return "Load False", 500


@movie_ns.route("/<int:id>/")
class MoviesViews(Resource):
    def get(self, id):
        a = MovieSchema().dump(Movie.query.filter(Movie.id == id))
        return a, 200

    def put(self, id):
        data = request.json
        try:
            result = Movie.query.filter(Movie.id == id).one()
            result.title = data.get('title')
            db.session.add(result)
            db.session.commit()
            return "UpLoad True"
        except Exception:
            db.session.rollback()
            return "UpLoad False", 500

    def delete(self, id):
        try:
            result = Movie.query.filter(Movie.id == id).one()
            db.session.delete(result)
            db.session.commit()
            return "Delete True"
        except Exception:
            db.session.rollback()
            return "Delete False", 500


if __name__ == '__main__':
    app.run(port=8081, debug=True)
