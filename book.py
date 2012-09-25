import tornado.ioloop
import tornado.web
import pymongo
import os
import time

connection = pymongo.Connection("localhost", 27017)
db = connection["library"]
collection = db["books"]

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render("index.html")

class BookHandler(tornado.web.RequestHandler):
    def post(self):
        title = self.get_argument("title")
        author = self.get_argument("author")
        year = self.get_argument("year")
        book_id = time.time()

        data = {"book_id":book_id, "title":title, "author":author, "year":year}
        collection.insert(data)
        self.redirect("/books")

class BookResult(tornado.web.RequestHandler):
    def get(self):
        result = collection.find()
        self.render("books.html",books=result)

class BookDelete(tornado.web.RequestHandler):
    def get(self,id):

        print id
        collection.remove({"book_id":id})



application = tornado.web.Application([
    (r"/", MainHandler),(r"/book", BookHandler),(r"/books", BookResult), (r"/delete/([0-9\.]+)", BookDelete)
], debug=True, static_path = os.path.join( os.path.dirname(__file__), "static" ) )

if __name__ == "__main__":
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()