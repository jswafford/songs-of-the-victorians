import os
import json
import re

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
        raw_title = re.sub("<.*?>", "", title)
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
            augdata=augdata, snippets=snippets, raw_title=raw_title)
        self.response.write(html)

class ArchivePage(webapp2.RequestHandler):
    credits_snippets = dict(
        norton = '''
            <p>Norton, Caroline. "Juanita." London: Chappell, 1853.</p>
            <p>"Juanita" by Caroline Norton performed by Anthony Rolfe Johnson (tenor) and Graham Johnson (piano). Courtesy of Hyperion Records Ltd, London. <a href="http://www.hyperion-records.co.uk/al.asp?al=CDH55159">http://www.hyperion-records.co.uk/al.asp?al=CDH55159</a></p>
        ''',
        balfe = '''
            <p>Balfe, Michael William. "Come into the Garden, Maud." London: Boosey & Songs, 1857. Courtesy of the British Library.</p>
            <p>"Come into the Garden, Maud" by Michael William Balfe performed by Derek Scott (tenor and piano). Courtesy of Derek Scott.</p>
        ''',
        sullivan = '''
            <p>Sullivan, Arthur.  "The Lost Chord." "The Lost Chord." London:  Boosey &amp; Co, 1877.   Courtesy of the National Library of Australia. &lt; <ref target="http://nla.gov.au/nla.mus-an7686876">http://nla.gov.au/nla.mus-an7686876</ref>&gt;</p>
            <p>"The Lost Chord" by Sir Arthur Sullivan performed by Derek Scott (tenor and piano). Courtesy of Derek Scott.</p>
        ''',

        somervell = '''
            <p>Somervell, Arthur.  "Come into the Garden, Maud." <i>Cycle of Songs from Tennyson's Maud.</i>  London: Boosey & Co, 1898. Courtesy of the San Francisco Public Library.</p>
            <p>"Come into the garden, Maud" performed by David Wilson-Johnson (baritone) and David Owen Norris (piano). Courtesy of Hyperion Records Ltd, London. <a href="http://www.hyperion-records.co.uk/tw.asp?w=W1187&t=GBAJY8618709&al=W1187_66187&vw=dc">http://www.hyperion-records.co.uk/tw.asp?w=W1187&t=GBAJY8618709&al=W1187_66187&vw=dc</a></p>
        ''',
    )

    def get(self, dataset_name):
        template = templates.get_template("archive.mako")
        data = get_data(dataset_name)
        title = data['title']
        npages = len(data['pages'])
        credits = self.credits_snippets.get(dataset_name, '')
        self.response.write(template.render(
            thetitle=title,
            data=data,
            dset=dataset_name,
            npages=npages,
            credits=credits.strip()))

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
