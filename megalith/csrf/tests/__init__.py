import unittest

from pyramid.config import Configurator
from pyramid.interfaces import ISession
from webtest import TestApp
from zope.interface import implementer

def dummy_view(request):
    from pyramid.response import Response
    return Response("OK")


@implementer(ISession)
class FakeSession(dict):

    def get_csrf_token(self):
        return "Unit Testing Token"

    def new_crsf_token(self):
        return self.get_csrf_token()


def fake_session(request):
    return FakeSession()


class TestCSRF(unittest.TestCase):

    def setUp(self):
        config = Configurator(session_factory=fake_session)
        config.include("megalith.csrf")
        config.add_route("route", "/")
        config.add_view(dummy_view, route_name="route")
        self.app = TestApp(config.make_wsgi_app())

    def test_get(self):
        response = self.app.get("/")
        self.assertEqual(response.body, b"OK")

    def test_no_token(self):
        response = self.app.post("/", expect_errors=True)
        self.assertEqual(response.status, "400 Bad CSRF Token")

    def test_invalid_token(self):
        response = self.app.post("/", params={"csrf_token": "bla"}, expect_errors=True)
        self.assertEqual(response.status, "400 Bad CSRF Token")

    def test_valid_token(self):
        response = self.app.post("/", params={"csrf_token": "Unit Testing Token"})
        self.assertEqual(response.body, b"OK")