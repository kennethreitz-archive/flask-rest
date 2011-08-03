# -*- coding: utf-8 -*-

from flaskext.rest import RestAPI, Resource, PagedResource, response, throttle

api = RestAPI('api', __name__)


@api.resource('/')
class RootResource(Resource):
    def __init__(self, id):
        super(RootResource, self).__init__()

    def get(self):
        return 'yay'


# @throttle(5, 100)
@api.resource('/needles/<id>')
class NeedleResource(Resource):

    def __init__(self, id):
        super(NeedleResource, self).__init__()
        print 'after'

    def get(self):
        return 'oh no!'

    def post(self):
        return 'post'

    def put(self, data):
        pass

    def patch(self, data):
        pass

    def delete(self):
        pass



@api.resource('/needles')
class NeedlesResource(PagedResource):

    def __init__(self, arg):
        super(NeedleResource, self).__init__()

    def get(self):
        pass

    def post(self):
        pass

    def put(self):
        pass

    def patch(self):
        pass

    def delete(self):
        pass

