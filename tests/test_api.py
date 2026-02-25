import pytest
from httpx import AsyncClient


@pytest.mark.asyncio
async def test_root(client: AsyncClient):
    """Test health check endpoint."""
    response = await client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
    assert data["docs"] == "/docs"


@pytest.mark.asyncio
async def test_register(client: AsyncClient):
    """Test user registration."""
    response = await client.post(
        "/api/v1/auth/register",
        json={
            "email": "user@example.com",
            "username": "newuser",
            "password": "password123",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "user@example.com"
    assert data["username"] == "newuser"
    assert "id" in data
    assert "hashed_password" not in data


@pytest.mark.asyncio
async def test_login(client: AsyncClient):
    """Test login and token."""
    await client.post(
        "/api/v1/auth/register",
        json={"email": "login@test.com", "username": "loginuser", "password": "pass123"},
    )
    response = await client.post(
        "/api/v1/auth/login",
        json={"username": "loginuser", "password": "pass123"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"


@pytest.mark.asyncio
async def test_create_and_get_tasks(client: AsyncClient, auth_headers: dict):
    """Test creating and retrieving tasks."""
    response = await client.post(
        "/api/v1/tasks",
        json={"title": "My first task", "description": "Do something"},
        headers=auth_headers,
    )
    assert response.status_code == 201
    task = response.json()
    assert task["title"] == "My first task"
    assert task["description"] == "Do something"
    assert task["is_completed"] is False

    response = await client.get("/api/v1/tasks", headers=auth_headers)
    assert response.status_code == 200
    tasks = response.json()
    assert len(tasks) >= 1
    assert any(t["title"] == "My first task" for t in tasks)


@pytest.mark.asyncio
async def test_unauthorized_access(client: AsyncClient):
    """Test that tasks require authentication."""
    response = await client.get("/api/v1/tasks")
    assert response.status_code == 401
