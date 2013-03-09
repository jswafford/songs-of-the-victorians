import os
import json

import webapp2
from mako.lookup import TemplateLookup

# from lxml import etree

# from tools import tei_to_html

here = os.path.dirname(__file__)
templates = TemplateLookup(directories=[os.path.join(here, 'templates')])

def get_data(name):
    return json.loads(open(here+"/data2/{0}/data.js".format(name)).read())

def has_data(name):
    return os.path.exists(here+"/data2/{0}".format(name))

class IndexPage(webapp2.RequestHandler):
    def get(self, index):
        template = templates.get_template("index.mako")
        self.response.write(template.render())

class AnalysisPage(webapp2.RequestHandler):
    def get(self, dataset_name):
        template = templates.get_template("analysis.mako")
        data = json.loads(open(here+"/data2/{0}/analysis.json".format(dataset_name)).read())
        title = data['title']
        html = data['text']
        links = data['links']
        augdata = {}
        snippets = []
        for (dset, type) in links.items():
            if type == 'snippet':
                snippets.append(dset)
            elif type == 'augnotes':
                augdata[dset] = get_data(dset)
        html = template.render(thetitle=title, analysis_html=html,
            augdata=augdata, snippets=snippets)
        self.response.write(html)

class ArchivePage(webapp2.RequestHandler):
    def get(self, dataset_name):
        template = templates.get_template("archive.mako")
        data = get_data(dataset_name)
        title = data['title']
        self.response.write(template.render(thetitle=title, data=data, dset=dataset_name))

class ExcerptPage(webapp2.RequestHandler):
    def get(self, dataset_name):
        template = templates.get_template("excerpt.mako")
        data = get_data(dataset_name)
        title = data['title']
        self.response.write(template.render(thetitle=title, data=data, dset=dataset_name))

app = webapp2.WSGIApplication([
    ('/(index.html)?', IndexPage),
    ('/(.*)/analysis.html', AnalysisPage),
    ('/(.*)/archive.html', ArchivePage),
    ('/(.*)/excerpt.html', ExcerptPage),
    ], debug=True)
