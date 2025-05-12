import requests

# Test to check if the API returns expected Pokémon data
def test_get_pokemon():
	url = "https://pokeapi.co/api/v2/pokemon/pikachu"

	response = requests.get(url)

	assert response.status_code == 200, "Failed to fest Pikachu data"

	data = response.json()
	assert data ["name"] == "pikachu", "Incorrect Pokémon name"
	assert "abilities" in data, "Abilities not found in response"

	
	print("✅ Pikachu API test passed!")


test_get_pokemon()
