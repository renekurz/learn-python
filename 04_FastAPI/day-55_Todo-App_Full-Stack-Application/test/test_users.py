from test.utils import *
from routers.users import get_db, get_current_user
from fastapi import status

app.dependency_overrides[get_db] = override_get_db
app.dependency_overrides[get_current_user] = override_get_current_user

def test_return_user(test_user):
    response = client.get("/users/")

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["username"] == "testuser"
    assert response.json()["email"] == "test@example.com"
    assert response.json()["first_name"] == "Test"
    assert response.json()["last_name"] == "User"
    assert response.json()["is_active"] is True
    assert response.json()["role"] == "admin"
    assert response.json()["phone_number"] == "123456789"

def test_change_password_success(test_user):
    response = client.put("/users/change-password", json={"password": "testpassword", "new_password": "newpassword"})

    assert response.status_code == status.HTTP_204_NO_CONTENT

def test_change_password_invalid_current_password(test_user):
    response = client.put("/users/change-password", json={"password": "wrongpassword", "new_password": "newpassword"})

    assert response.status_code == status.HTTP_401_UNAUTHORIZED
    assert response.json() == {"detail": "Error on password change"}

def test_change_phone_number_success(test_user):
    response = client.put("/users/change-phone-number/2222222222")

    assert response.status_code == status.HTTP_204_NO_CONTENT