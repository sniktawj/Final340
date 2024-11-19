import cherrypy
from app.models.requirements import get_major_requirements
from jinja2 import Environment, FileSystemLoader

env = Environment(loader=FileSystemLoader('app/templates'))

class RequirementController:
    @cherrypy.expose
    def index(self, major_id=None):
        if not major_id:
            return "Please provide a major ID."
        requirements = get_major_requirements(major_id)
        template = env.get_template('requirements.html')
        return template.render(requirements=requirements)
