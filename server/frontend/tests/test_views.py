import pytest

from django.test import Client

pytestmark = pytest.mark.django_db


@pytest.mark.django_db
class TestRequests:
    pytestmark = pytest.mark.django_db

    def test_index(self):
        client = Client()
        response = client.get('/')
        assert response.status_code == 200
