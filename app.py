#!/usr/bin/python2
# -!- coding: utf-8 -!-
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from flask_socketio import SocketIO, emit
from qtwitter import QueryTwitter
import twitter, model, os, sys
from pprint import pprint

app = Flask(__name__)
app.config.from_object("config")
model.db.init_app(app)
twitterApi = twitter.Api(
    consumer_key=app.config['TWITTER_CONSUMER_KEY'], 
    consumer_secret=app.config['TWITTER_CONSUMER_SECRET'], 
    access_token_key=app.config['TWITTER_ACCESS_TOKEN_KEY'],
    access_token_secret=app.config['TWITTER_ACCESS_TOKEN_SECRET'])

queryTw = QueryTwitter(twitterApi)

class VoteManager():
    def getTweetVotes(self, twid):
        votes = model.Vote.query.filter_by(tweetid=twid).all()
        return votes

    def vote(self, twid, vote):
        if vote in model.VoteEnum:
            newVote = model.Vote(twid, vote)
            db.session.add(newVote)
            db.session.commit()

manager = VoteManager()

@app.before_request
def csrf_protect():
    if request.method == "POST":
        if ('csrf_token' not in session or 'csrf_token' not in request.form or request.form['csrf_token'] != session['csrf_token']):
            flash('Falta token CSRF')
            return redirect(url_for('index'))

    if 'csrf_token' not in session:
        session['csrf_token'] = os.urandom(16).encode('hex')

@app.route('/')
def index():
    tweets = queryTw.get()
    return render_template('index.html', tweets=tweets)

@app.route('/vote', methods=['POST'])
def vote():
    vote = request.form['vote']
    twid = request.form['twid']
    manager.vote(twid, vote)
    flash('Voto emitido!')
    return redirect(url_for('index'))

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        if sys.argv[1] == 'createdb':
            app.test_request_context().push()
            model.db.create_all()
        sys.exit(0)
    app.run()