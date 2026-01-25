import pytest
from django.urls import reverse

@pytest.mark.django_db
def test_homepage_loads(client):
    url = reverse("upload")
    response = client.get(url)
    assert response.status_code == 200
