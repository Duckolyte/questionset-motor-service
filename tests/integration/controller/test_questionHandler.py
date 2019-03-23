from tornado.testing import AsyncHTTPTestCase

from questionset_service.tornado_questionset import setup_server


class TestQuestionHandler(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_get(self):
        response = self.fetch('/question/1')
        self.assertEquals(response.code, 200)

    def test_get_invalid_url(self):
        response = self.fetch('/question/more/more')
        self.assertEquals(response.code, 404)

