from tornado.testing import AsyncHTTPTestCase

from questionset_service.tornado_questionset import setup_server


class TestImageMapHandler(AsyncHTTPTestCase):

    def get_app(self):
        return setup_server()

    def test_get(self):
        response = self.fetch('/question/1')
        self.assertEquals(response.code, 200)

    def test_get_invalid_url(self):
        response = self.fetch('/question/more/more')
        self.assertEquals(response.code, 404)
        #self.assertIn('error', response.code)

    '''
        def get_app(self):
        return setup_server()

    def test_get(self):
        response = self.fetch('/questionary/test_000321')
        self.assertEquals(response.code, 200)

    def test_get_invalid_url(self):
        response = self.fetch('/questionary/more/more')
        self.assertEquals(response.code, 404)

    '''
