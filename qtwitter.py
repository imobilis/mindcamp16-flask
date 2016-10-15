#!/usr/bin/python2
# -!- coding: utf-8 -!-
from pprint import pprint
template = u"""
<div class="row"><div class="small-4 columns">
<blockquote class="twitter-tweet" lang="%s">
<p lang="%s">%s</p>
— %s (%s)
<a href="https://twitter.com/%s/status/%s">
%s
</a>
</blockquote>
</div><div class="small-8"></div></div>
"""

class QueryTwitter(object):
    __api = None

    def __init__(self, api):
        self.__api = api

    def get(self):
        return self.__api.GetUserTimeline(64465656)


