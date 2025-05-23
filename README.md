# API Testing Demo – Pokémon API

## Overview
This is a simple Python project that tests the public [PokéAPI](https://pokeapi.co/) using `requests` and `pytest`.

The test suite includes:

- ✅ API availability checks (status 200)
- ⚠️ Error validation for invalid Pokémon
- 🔁 Parameterized tests across multiple responses

Great for showcasing beginner-to-mid-level API testing and Python scripting.

---

## How to Run

1. Clone this repo  
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Run all tests:
   ```bash
   pytest
   ```

---

## Tests Included

| Test | Description |
|------|-------------|
| `test_get_pokemon()` | Validates that `/pokemon/pikachu` returns a 200 response with correct structure |
| `test_invalid_pokemon_returns_404()` | Sends request to a non-existent Pokémon and expects a 404 |
| `test_broken_endpoint_returns_404()` | Sends request to an invalid endpoint (`/pokemons`) and expects a 404 |
| `test_multiple_pokemon()` (x3) | Parameterized test that loops through multiple valid Pokémon and verifies content |

---

## Tech Stack

- Python 3  
- Pytest  
- requests  
- PokéAPI (public REST API)

---

## Author

Jacob Simpson – QA Engineer  
[github.com/jacobsimpsonQA](https://github.com/jacobsimpsonQA)
