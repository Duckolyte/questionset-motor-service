import tornado.ioloop
import tornado.web

import motor

# import ui templates
# from view import partials

# import controllers
from questionset_service.controller.question import QuestionHandler
from questionset_service.controller.imagemap import ImageMapHandler


class ApplicationContext(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/question/([^/]+)?", QuestionHandler),
            (r"/imagemap/([^/]+)?", ImageMapHandler)
        ]

        settings = dict(
            db=motor.motor_tornado.MotorClient(
                'mongodb://localhost:27017'
            ).questionary
            # xsrf_cookies=True,
            # cookie_secret='123456789',
            # login_url='/login'
        )

        tornado.web.Application.__init__(self, handlers, **settings)
