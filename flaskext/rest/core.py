# -*- coding: utf-8 -*-

# RestAPI

# Resource,  , response, throttle
from flask import Blueprint
from .packages.decorator import decorator
from functools import wraps


from flask.views import View

class Resource(object):

    def __init__(self, route, *args):
        """
        If there are decorator arguments, the function
        to be decorated is not passed to the constructor!
        """
        print route
        # print "Inside __init__()"
        self.route = route
        self._app = None

    def __call__(self, cls):
        """
        If there are decorator arguments, __call__() is only called
        once, as part of the decoration process! You can only give
        it a single argument, which is the function object.
        """
        # print "Inside __call__()"
        # print cls(self.route)
        def wrapped_f(*args):
            print "Inside wrapped_f()"
            # print "Decorator arguments:", self.arg1, self.arg2, self.arg3
            obj = cls(*args)
            print 'parent adding'

            self.parent.add_url_rule(self.route, '')

            return obj

        return wrapped_f


class RestAPI(Blueprint):
    def __init__(self, *args):
        super(RestAPI, self).__init__(*args)
        self.resource = Resource
        self.resource.parent = self


    # resource = recou


@decorator
def throttle(f, *args, **kwargs):
    pass



class PagedResource(object):
    def __init__(self):
        super(PagedResource, self).__init__()



response = dict()