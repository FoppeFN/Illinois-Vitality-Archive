import pytest
from datetime import date
from django.urls import reverse
from records.models import Birth, Death, Person, Sex


@pytest.mark.django_db
def test_birth_search_returns_expected_result(client):
    mother = Person.objects.create(
        first_name="Mary",
        last_name="Doe",
        sex=Sex.FEMALE,
    )
    father = Person.objects.create(
        first_name="John",
        last_name="Doe",
        sex=Sex.MALE,
    )
    child = Person.objects.create(
        first_name="Alice",
        last_name="Doe",
        sex=Sex.FEMALE,
        mother=mother,
        father=father,
    )

    Birth.objects.create(
        person=child,
        birth_date=date(1901, 2, 3),
        birth_county="057",
        birth_city="Edwardsville",
    )

    url = reverse("search_birth_records")
    response = client.get(
        url,
        {
            "first_name": "Alice",
            "last_name": "Doe",
            "birth_county": "057",
        },
        HTTP_HX_REQUEST="true",
    )

    assert response.status_code == 200
    html = response.content.decode()
    assert "Alice" in html
    assert "Doe" in html


@pytest.mark.django_db
def test_birth_results_page_loads(client):
    person = Person.objects.create(
        first_name="Robert",
        last_name="Smith",
        sex=Sex.MALE,
    )

    Birth.objects.create(
        person=person,
        birth_date=date(1905, 1, 1),
        birth_county="057",
        birth_city="Edwardsville",
    )

    url = reverse("birth_results")
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_death_search_returns_expected_result(client):
    person = Person.objects.create(
        first_name="John",
        last_name="Doe",
        sex=Sex.MALE,
    )

    Death.objects.create(
        person=person,
        death_date=date(2000, 1, 1),
        death_age=75,
        death_county="057",
        death_city="Edwardsville",
    )

    url = reverse("search_death_records")
    response = client.get(
        url,
        {
            "first_name": "John",
            "last_name": "Doe",
            "death_county": "057",
        },
        HTTP_HX_REQUEST="true",
    )

    assert response.status_code == 200
    html = response.content.decode()
    assert "John" in html
    assert "Doe" in html