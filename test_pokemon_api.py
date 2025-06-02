import requests
import pytest
import time

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

# 🧬 Option D: Verify Pikachu's evolution chain
def test_pikachu_evolution_chain():
    species_url = "https://pokeapi.co/api/v2/pokemon-species/pikachu"
    species_response = requests.get(species_url)
    assert species_response.status_code == 200, "❌ Failed to fetch species data"
    evolution_chain_url = species_response.json()["evolution_chain"]["url"]

    evo_response = requests.get(evolution_chain_url)
    assert evo_response.status_code == 200, "❌ Failed to fetch evolution chain data"

    chain = evo_response.json()["chain"]
    baby = chain["species"]["name"]
    middle = chain["evolves_to"][0]["species"]["name"]
    final = chain["evolves_to"][0]["evolves_to"][0]["species"]["name"]

    assert baby == "pichu", "❌ Expected evolution start with Pichu"
    assert middle == "pikachu", "❌ Expected Pikachu as middle evolution"
    assert final == "raichu", "❌ Expected final evolution to be Raichu"

    print("🧬 Evolution chain test passed: Pichu → Pikachu → Raichu")


# 🚦 Option E: Rate limit behavior
def test_rate_limit_behavior():
    url = "https://pokeapi.co/api/v2/pokemon/pikachu"
    success_count = 0
    error_count = 0

    for _ in range(10):  # send 10 rapid requests
        response = requests.get(url)
        if response.status_code == 200:
            success_count += 1
        elif response.status_code == 429:
            error_count += 1
        time.sleep(0.2)  # slight delay to simulate a burst

    print(f"✅ Successful requests: {success_count}")
    print(f"⚠️ Rate-limited responses: {error_count}")
    assert success_count > 0, "❌ No successful responses received."
