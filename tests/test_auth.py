import json
from run import app

def test_register_usuario():
    tester = app.test_client()
    response = tester.post('/register', 
        data=json.dumps({
            "cedula": "1234567890",
            "nombres": "Carlos",
            "apellidos": "Nuñez",
            "fecha_nacimiento": "2000-01-01",
            "email": "carlos@example.com",
            "password": "securepassword"
        }),
        content_type='application/json'
    )
    assert response.status_code in (201, 409)  # 201 si es nuevo, 409 si ya existe
