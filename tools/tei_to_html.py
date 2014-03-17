'''
This parses TEI files and outputs box data.
Usage: python tei_to_html.py <tei_file> > <json_file>
'''
from pyquery import PyQuery as pq


def changeAll(doc, oldtag, newtag):
    tags = list(doc(oldtag).items())
    for t in tags:
        t.replaceWith(str(newtag.html(t.html())))

def esc(s):
    return s.replace("'", "\\'")

def format_xref(node):
    doc = node.attr("doc")
    if doc.startswith('augnotes:'):
        doc = doc[9:]
        title = node.attr("title")
        doc, title = map(esc, [doc, title])
        x = pq('<a onclick="show_augnote(\''+doc+'\', \''+title+'\')">[<img src="/static/img/speaker.svg" height="14px"/>]</span>')
        node.replaceWith(str(x))
        return (doc, 'augnotes')
    elif doc.startswith('snippet:'):
        doc = doc[8:]
        title = node.attr("title")
        doc, title = map(esc, [doc, title])
        x = pq('<a onclick="play_snippet(\''+doc+'\', \''+title+'\')">[<img src="/static/img/speaker.svg" height="14px"/>]</span>')
        node.replaceWith(str(x))
        return (doc, 'snippet')
    return None, None

def basic_htmlify(node):
    changeAll(node, 'hi[rend="bold"]', pq("<div class='center bold'>"))
    changeAll(node, "hi", pq("<i>"))
    changeAll(node, "lg l", pq("<div>"))
    changeAll(node, "lg", pq("<blockquote>"))
    changeAll(node, "q", pq("<blockquote>"))
    tags = list(node("graphic").items())
    for t in tags:
        t.replaceWith(str(pq("<img>").attr("src", t.attr("url")).html(t.html())))

def extract_footnotes(node, prefix=""):
    result = []
    for i, note in enumerate(node("note").items()):
        n = i+1
        anchor = "{}{}".format(prefix, n)
        tmp = u"<div class='footnote'><a name='foot{0}'></a>{2}. {1} <a href='#foot{0}-back'>&uarr;</a></div>".format(anchor, note("p").eq(0).html(), n)
        l = u"<sup><a href='#foot{0}' name='foot{0}-back'>{1}</a></sup>".format(anchor, n)
        note.replaceWith(l)
        result.append(tmp)
    return result

def extract_links(node):
    links = {}
    for xref in node('xref').items():
        doc, type = format_xref(xref)
        if type == 'augnotes':
            links[doc] = type
        elif type == 'snippet' and links.get(doc) != 'augnotes':
            links[doc] = type
    return links

def fix_tei(tei):
    doc = pq(tei).remove_namespaces()
    title = pq(doc("title").html()).remove_namespaces()
    changeAll(title, "hi", pq("<i>"))
    author = doc("author").text()
    text = pq(doc("text").html()).remove_namespaces()
    links = {}
    if text.find('div[type="section"]'):
        def process(i, elt):
            elt = pq(elt)
            basic_htmlify(elt)
            for note in extract_footnotes(elt, prefix='{}-'.format(i)):
                elt.append(note)
            links.update(extract_links(elt))
            return elt
        pages = pq(text('div[type="section"]').map(process))
        return title, author, map(pq, pages), links
    else:
        basic_htmlify(text)
        for note in extract_footnotes(text):
            text.append(note)
        links = extract_links(text)
        return title, author, [text], links

if __name__ == '__main__':
    import sys
    import json
    title, author, text, links = fix_tei(open(sys.argv[1]).read())
    print json.dumps(dict(title=str(title), author=author, pages=map(str, text), links=links))

