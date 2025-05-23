import requests
import pytest

# ✅ Happy path: Pikachu API test
def test_get_pokemon():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu")
    assert response.status_code == 200, "❌ Failed to fetch Pikachu data"
    data = response.json()
    assert data["name"] == "pikachu", "❌ Incorrect Pokémon name"
    assert "abilities" in data, "❌ Abilities not found in response"

# 🛑 Option A: 404 for invalid Pokémon
def test_invalid_pokemon_returns_404():
    response = requests.get("https://pokeapi.co/api/v2/pokemon/pikachu999")
    assert response.status_code == 404, "❌ Expected 404 for non-existent Pokémon"

# ♻️ Option B: Parameterized test for multiple Pokémon
@pytest.mark.parametrize("name", ["bulbasaur", "charmander", "mewtwo"])
def test_multiple_pokemon(name):
    response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{name}")
    assert response.status_code == 200, f"❌ Failed to fetch {name}"
    data = response.json()
    assert data["name"] == name.lower()

# ⚠️ Option C: Broken endpoint returns error
def test_broken_endpoint_returns_404():
    response = requests.get("https://pokeapi.co/api/v2/pokemons")  # invalid endpoint
    assert response.status_code == 404, "❌ Expected 404 from broken endpoint"
