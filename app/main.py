import cherrypy
from app.controllers.courses import CourseController
from app.controllers.requirements import RequirementController
from app.controllers.students import StudentController

class ISATApp:
    @cherrypy.expose
    def index(self):
        return "Welcome to the ISAT Course Finder!"

if __name__ == '__main__':
    # Static files configuration
    static_dir_config = {
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './app/static',
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
