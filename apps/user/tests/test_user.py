import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_create_user(api_client):
    url = reverse("user-register")
    response = api_client.post(url, {"username": "testuser", "password": "pass"})
    assert response.status_code == 201
