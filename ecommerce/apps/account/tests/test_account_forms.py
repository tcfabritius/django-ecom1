import pytest
from ecommerce.apps.account.forms import RegistrationForm, UserAddressForm


@pytest.mark.parametrize(
    "full_name, phone, address_line, address_line2, town_city, postcode, validity",
    [
        ("mike", "123456789", "add1", "add2", "town", "postcode", True),
        #("", "123456789", "add1", "add2", "town", "postcode", False),
    ],
)
def test_customer_add(full_name, phone, address_line, address_line2, town_city, postcode, validity):
    form = UserAddressForm(
        data={
            "full_name": full_name,
            "phone": phone,
            "address_line": address_line,
            "address_line2": address_line2,
            "town_city": town_city,
            "postcode": postcode,
        }
    )
    assert form.is_valid() is validity

def test_customer_create_address(client, customer):
    user = customer
    client.force_login(user)
    response = client.post("/account/add_address", data={
        'full_name': 'name',
        'phone': '123456789',
        'address_line': 'add1',
        'address_line2': 'add2',
        'town_city': 'town',
        'postcode': 'postcode',
        },
        )
    assert response.status_code == 302


@pytest.mark.parametrize(
    "user_name, email, password1, password2, validity",
    [
        ("user1", "a@a.com", "12345a", "12345a", True),
        ("user1", "a@a.com", "12345a", "", False),
        # ("user1", "a@a.com", "", "12345a", True),
        ("user1", "a@a.com", "12345a", "12345b", False),
        ("user1", "a@.com", "12345a", "12345a", False),
    ],
)
@pytest.mark.django_db
def test_create_account(user_name, email, password1, password2, validity):
    form = RegistrationForm(
        data={
            "user_name": user_name,
            "email": email,
            "password1": password1,
            "password2": password2,
        },
    )
    assert form.is_valid() is validity


@pytest.mark.parametrize(
    "user_name, email, password1, password2, validity",
    [
        ("user1", "a@a.com", "12345a", "12345a", 200),
        ("user1", "a@a.com", "12345a", "12345", 400),
        ("user1", "", "12345a", "12345", 400),
    ],
)
@pytest.mark.django_db
def test_create_account_view(client, user_name, email, password1, password2, validity):
    response = client.post(
        "/account/register",
        data={
            "user_name": user_name,
            "email": email,
            "password1": password1,
            "password2": password2,
        },
    )
    assert response.status_code == validity


def test_account_register_redirect(client, customer):
    user = customer
    client.force_login(user)
    response = client.get("/account/register/")
    assert response.status_code == 302


@pytest.mark.django_db
def test_account_register_render(client):
    response = client.get("/account/register/")
    assert response.status_code == 200