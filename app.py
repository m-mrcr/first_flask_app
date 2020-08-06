from flask import Flask, request, Response
from database.db import initialize_db
from database.models import Movie

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
  'host': 'mongodb://localhost/movie-bag'
}

@app.route('/movies')
def get_movies():
  movies = Movie.objects().to_json()
  return Response(movies, mimetype='application/json', status=200)

@app.route('/movies', methods=['POST'])
  body = request.get_json()
  movie = Movie(**body).save()
  id = movie.id
  return {'id': str(id)}, 200

@app.route('/movies/<id>', methods=['PUT'])
def update_movie(id):
  body = request.get_json()
  Movie.objects.get(id=id).update(**body)
  return '', 200



app.run()