import ckan.plugins as p
from ckan.lib.base import BaseController


class HelpController(BaseController):

    def index(self):
        return p.toolkit.render('home/help.html')
