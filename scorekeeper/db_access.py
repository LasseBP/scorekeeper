#!/usr/bin/env python
# coding=utf-8
# all the imports
from scorekeeper import app
from flask import g
import sqlite3

def get_danish_day_name(dayNo):
    """Get danish name of weekday. Sunday is 0."""
    days = [u'søndag', u'mandag', u'tirsdag', u'onsdag', u'torsdag', u'fredag', u'lørdag']
    return days[dayNo]

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
        query_db('PRAGMA foreign_keys = on;')
        g.sqlite_db.commit()
    return g.sqlite_db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'sqlite_db'):
        g.sqlite_db.close()