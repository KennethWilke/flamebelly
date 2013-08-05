import os
import cherrypy
from mako.lookup import TemplateLookup

# Get paths relative to module location
current_dir = os.path.dirname(os.path.abspath(__file__))
static_dir = os.path.join(current_dir, 'static')
template_dirs = [os.path.join(current_dir, 'templates')]

# CherryPy app config
__config__ = {'/static': {'tools.staticdir.on': True,
                          'tools.staticdir.dir': static_dir}}

class Blog(object):
    """ A simple blogging application """

    def __init__(self):
        self.templates = TemplateLookup(directories=template_dirs)

    @cherrypy.expose
    def default(self):
        """ Landing page """
        template = self.templates.get_template('index.html')
        return template.render()

__app__ = Blog()
