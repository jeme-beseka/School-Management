from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_create_student():
    response = client.post(
        "/students",
        json={"firstName": "John", "lastName": "Doe", "email": "john@example.com", "dateOfBirth": "2005-03-25"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["firstName"] == "John"
    assert "id" in data
    return data["id"]

def test_get_student():
    # First, create a student
    student_id = test_create_student()
    
    # Then, retrieve the student's details
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id
    assert data["firstName"] == "John"
    assert data["lastName"] == "Doe"
    assert data["email"] == "john@example.com"
    assert data["dateOfBirth"] == "2005-03-25"

def test_update_student():
    # First, create a student
    student_id = test_create_student()
    
    # Then, update the student's information
    update_data = {
        "firstName": "Jane",
        "lastName": "Smith",
        "email": "jane.smith@example.com",
        "dateOfBirth": "2006-04-26"
    }
    response = client.put(f"/students/{student_id}", json=update_data)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == student_id
    assert data["firstName"] == "Jane"
    assert data["lastName"] == "Smith"
    assert data["email"] == "jane.smith@example.com"
    assert data["dateOfBirth"] == "2006-04-26"

    # Verify the update by getting the student details
    response = client.get(f"/students/{student_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["firstName"] == "Jane"
    assert data["lastName"] == "Smith"
    assert data["email"] == "jane.smith@example.com"
    assert data["dateOfBirth"] == "2006-04-26"
