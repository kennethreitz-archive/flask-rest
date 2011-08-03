#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flaskext.script import Manager

from haystack import app

manager = Manager(app)

@manager.command
def hello():
    print "hello"

if __name__ == "__main__":
    manager.run()