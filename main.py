import os
import json

import webapp2
from mako.lookup import TemplateLookup

# from lxml import etree

# from tools import tei_to_html

here = os.path.dirname(__file__)
templates = TemplateLookup(directories=[os.path.join(here, 'templates')])

class IndexPage(webapp2.RequestHandler):
    def get(self, index):
        template = templates.get_template("index.html")
        self.response.write(template.render())

class AnalysisPage(webapp2.RequestHandler):
    def get(self, dataset_name):
        template = templates.get_template("analysis.mako")
        data = json.loads(open(here+"/data2/{0}/analysis.json".format(dataset_name)).read())
        title = data['title']
        html = data['text']
        self.response.write(template.render(thetitle=title, analysis_html=html))

class ArchivePage(webapp2.RequestHandler):
    def get(self, dataset_name):
        template = templates.get_template("archive.mako")
        data = json.loads(open(here+"/data2/{0}/data.js".format(dataset_name)).read())
        title = data['title']
        self.response.write(template.render(thetitle=title, data=data, dset=dataset_name))

app = webapp2.WSGIApplication([
    ('/(index.html)?', IndexPage),
    ('/(.*)/analysis.html', AnalysisPage),
    ('/(.*)/archive.html', ArchivePage),
    ], debug=True)
