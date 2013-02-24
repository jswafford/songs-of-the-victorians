import webapp2

class MainPage(webapp2.RequestHandler):
    def get(self):
        return webapp2.redirect('/index.html')

app = webapp2.WSGIApplication([('/', MainPage)],
                                debug=True)
