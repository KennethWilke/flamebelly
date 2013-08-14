import cherrypy
import uwsgi
import importlib
import ConfigParser

# Read and parse config
config = ConfigParser.SafeConfigParser()
config.read(uwsgi.opt['ini'])

def application(env, start_response):
    """ uWSGI entry point """
    # Instantiate and configure flamebelly server
    flamebelly = Flamebelly()
    flamebelly.load_modules(config.items('flamebelly_modules'))
    return cherrypy.tree(env, start_response)

class Flamebelly(object):
    """ Main class used to represent the server and core functionality """

    def load_modules(self, modules):
        """ Loads modules from a list of tuples (<route>, <module_name>) """
        for route, module_name in modules:
            try:
                mod = importlib.import_module("modules.%s" % module_name)
                if hasattr(mod, '__config__'):
                    cherrypy.tree.mount(mod.__app__, route, mod.__config__)
                else:
                    cherrypy.tree.mount(mod.__app__, route)
            except Exception as error:
                print "Error loading %s module: %s" % (module_name, str(error))
