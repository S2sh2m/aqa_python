import uuid

def test_user_registration(open_registration, register_user):
    open_registration()

    email = f"user_{uuid.uuid4().hex[:6]}@yopmail.com"

    register_user(
        name="Alex",
        lastname="Me",
        email=email,
        password="Alex1213!@"
    )
