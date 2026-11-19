import app as api_module


def make_client(tmp_path, monkeypatch):
    monkeypatch.setattr(api_module, "DB_PATH", tmp_path / "test.db")
    monkeypatch.setenv("API_KEY", "test-only-api-key")
    monkeypatch.setenv("DEMO_ADMIN_PASSWORD", "AdminTestPassword")
    monkeypatch.setenv("DEMO_STUDENT_PASSWORD", "StudentTestPassword")
    api_module.init_db()
    api_module.app.config.update(TESTING=True)
    return api_module.app.test_client()


def test_health(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    response = client.get("/api/health")
    assert response.status_code == 200
    assert response.get_json()["status"] == "ok"


def test_profile_rejects_invalid_key(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    response = client.get("/api/profile", headers={"X-API-Key": "wrong"})
    assert response.status_code == 401


def test_login_and_sql_injection_rejection(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)

    valid = client.post(
        "/api/login",
        json={"username": "admin", "password": "AdminTestPassword"},  # pragma: allowlist secret
    )
    assert valid.status_code == 200

    injection = client.post(
        "/api/login",
        json={"username": "admin' OR '1'='1", "password": "irrelevant"},  # pragma: allowlist secret
    )
    assert injection.status_code == 401
