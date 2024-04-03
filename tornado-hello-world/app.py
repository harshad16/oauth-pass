import asyncio
import tornado

from tornado.options import define, options

define("port", default=8888, help="run on the given port", type=int)


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")
        tornado_headers = self.request.headers
        print(tornado_headers) 
        # print x-forwarded-for header
        print(tornado_headers.get('X-Forwarded-Access-Token'))


async def main():
    tornado.options.parse_command_line()
    application = tornado.web.Application([(r"/", MainHandler)])
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(options.port)
    await asyncio.Event().wait()


if __name__ == "__main__":
    print("Starting server...")
    asyncio.run(main())