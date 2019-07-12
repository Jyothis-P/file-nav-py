# import flask dependencies
from flask import Flask, request, make_response, jsonify
from crawl import get_list
from fuzzywuzzy import fuzz 
from fuzzywuzzy import process
from pygame import mixer
import os

mixer.init()    
files = {}

# initialize the flask app
app = Flask(__name__)

# default route
@app.route('/')
def index():
    return 'Hello World!'

def play_file(path):
    mixer.music.load(path)
    mixer.music.play()

def fuzzy_match(query):
    
    choices = list(files.keys())
    print(query)
    best_res, val = process.extractOne(query, choices)
    print( "Best among the above list: ",best_res )
    os.startfile(files[best_res])

    return best_res

# function for responses
def results():
    # build a request object
    req = request.get_json(force=True)
    data = request.get_json(silent=True)
    movie = data['queryResult']['parameters']['filename']
    song_name = fuzzy_match(movie)
    
    # fetch action from json
    action = req.get('queryResult').get('action')

    # return a fulfillment response
    return {'fulfillmentText': 'playing ' + str(song_name)}

# create a route for webhook
@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    # return response
    if request.get_json(force=True)['queryResult']['parameters']['filename']
    return make_response(jsonify(results()))

# run the app
if __name__ == '__main__':
    files = get_list()
    app.run()
    
   
