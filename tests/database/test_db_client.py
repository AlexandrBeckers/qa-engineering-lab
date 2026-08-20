def test_database_connection(db_client):
    assert db_client.fetchone("SELECT 1") == (1,)
