from core.security import hash_password

fake_user = {
    "email": "admin@vapt.com",
    "password": hash_password("admin123")
}
