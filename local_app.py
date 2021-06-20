from flask import Flask, jsonify, request

app = Flask(__name__)
songs = [
{
    "title": "Bling",
    "artist": "Drake",
    "genre": "rap",
},
{
    "title": "Hello",
    "artist": "Adele",
    "genre": "Pop",
},
{
    "title": "Andhadhi",
    "artist": "Govind Vasantha",
    "genre": "Indian"
}
]

@app.route('/')
def welcome():
    return 'My app'

@app.route('/songs')
def home():
    return jsonify(songs)

@app.route('/songs', methods=['POST'])
def add_songs():
    song = request.get_json()
    songs.append(song)
    return jsonify(songs)

if __name__ == '__main__':
    app.run(debug=True)
