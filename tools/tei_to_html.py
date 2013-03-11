'''
This parses MEI files and outputs box data.
Usage: python parse_mei.py <mei_file> <dataset_name>
'''
from pyquery import PyQuery as pq


def changeAll(doc, oldtag, newtag):
    tags = doc(oldtag).items()
    [t.replaceWith(str(newtag.html(t.html()))) for t in tags]

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

def fix_tei(tei):
    doc = pq(tei).remove_namespaces()
    title = doc("title").text()
    author = doc("author").text()
    text = pq(doc("text").html())
    changeAll(text, "hi", pq("<i>"))
    changeAll(text, "lg l", pq("<div>"))
    changeAll(text, "lg", pq("<blockquote>"))
    changeAll(text, "q", pq("<blockquote>"))
    for i, note in enumerate(text("note").items()):
        n = i+1
        tmp = "<div class='footnote'><a name='foot{0}'></a>{0}. {1} <a href='#foot{0}-back'>&uarr;</a></div>".format(n, note("p").eq(0).html())
        text.append(tmp)
        l = "<sup><a href='#foot{0}' name='foot{0}-back'>{0}</a></sup>".format(n)
        note.replaceWith(l)
    links = {}
    for node in text('xref').items():
        doc, type = format_xref(node)
        if type == 'augnotes':
            links[doc] = type
        elif type == 'snippet' and links.get(doc) != 'augnotes':
            links[doc] = type
    return title, author, text, links

if __name__ == '__main__':
    import sys
    import json
    title, author, text, links = fix_tei(open(sys.argv[1]).read())
    print json.dumps(dict(title=title, author=author, text=str(text), links=links))

