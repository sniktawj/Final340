import os
import cherrypy
from app.controllers.courses import CourseController
from app.controllers.requirements import RequirementController
from app.controllers.students import StudentController

class ISATApp:
    @cherrypy.expose
    def index(self):
        # Render the main front page (index.html)
        with open(os.path.join(os.path.dirname(__file__), 'templates', 'index.html')) as f:
            return f.read()

if __name__ == '__main__':
    # Get the absolute path for the static directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    static_dir = os.path.join(current_dir, 'static')

    # Static files configuration
    static_dir_config = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': static_dir,
            'tools.staticdir.index': 'index.html'
        }
    }

    # Mount controllers to specific routes
    cherrypy.tree.mount(ISATApp(), '/', config=static_dir_config)
    cherrypy.tree.mount(CourseController(), '/courses', config=static_dir_config)
    cherrypy.tree.mount(RequirementController(), '/requirements', config=static_dir_config)
    cherrypy.tree.mount(StudentController(), '/students', config=static_dir_config)

    # Start the CherryPy server
    cherrypy.config.update({
        'server.socket_host': '0.0.0.0',
        'server.socket_port': 8080
    })
    cherrypy.engine.start()
    cherrypy.engine.block()
