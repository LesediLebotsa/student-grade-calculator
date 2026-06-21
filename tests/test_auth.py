from services.auth_services import hash_password

def test_hash_password():

    result = hash_password("password")

    assert result is not None
    assert len(result) > 0