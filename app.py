import os
from flask import Flask, request, render_template
from lib.database_connection import get_flask_database_connection
from lib.album_repository import AlbumRepository
from lib.album import Album
from lib.artist_repository import ArtistRepository
from lib.artist import Artist

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==
@app.route('/albums', methods=['GET'])
def return_albums():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    albums = repository.all()
    return render_template("albums/index.html", albums=albums)

@app.route('/albums/<int:id>', methods = ['GET'])
def return_an_album(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    album = repository.find(id)
    return render_template("albums/album_id.html", album=album)

@app.route('/albums', methods=['POST'])
def add_album():
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    if not request.form:
        return "No data provided. Please enter some data!", 400

    new_album = Album(None, request.form['title'],request.form['release_year'], request.form['artist_id'])
    repository.create(new_album)
    return f"{request.form['title']} ({request.form['release_year']}) has been added!"

@app.route('/albums/<int:id>', methods=['DELETE'])
def delete_album_by_id(id):
    connection = get_flask_database_connection(app)
    repository = AlbumRepository(connection)
    repository.delete(id)
    return f"Album with id = {id} has been successfully deleted"



if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
