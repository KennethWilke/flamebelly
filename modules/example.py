import cherrypy

class ExampleApplication(object):
    """ Flamebelly example application """

    @cherrypy.expose
    def index(self):
        """ Landing page """
        return "g'day!"

__app__ = ExampleApplication()
