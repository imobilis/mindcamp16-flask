#!/usr/bin/python2
# -!- coding: utf-8 -!-
import enum
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class VoteEnum(enum.Enum):
    esbueno = "esbueno"
    esmalo = "esmalo"

class Vote(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tweetid = db.Column(db.Integer)
    vote = db.Column(db.Enum(VoteEnum))

    def __init__(self, tweetid, vote):
        self.tweetid = tweetid
        self.vote = vote

    def __repr__(self):
        return u'<Vote for %r:%r>' % (self.tweetid, self.vote)

