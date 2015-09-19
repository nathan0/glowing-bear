#!/usr/bin/python2
import web, os
from mimetypes import MimeTypes

web.internalerror = web.debugerror

urls = (
    "/",        "Index",
    "/(.*?)",   "Return404",
)

app = web.application(urls, globals())
render = web.template.render("templates")

class Index:
    def GET(self):
        web.header("Content-Type", "text/html")
        yield render.index()

class Return404:
    def GET(self, url):
        yield web.notfound()
    def POST(self, url):
        yield web.notfound()
    def HEAD(self, url):
        yield web.notfound()
    def OPTIONS(self, url):
        yield web.notfound()

if __name__ == "__main__":
    app.run()