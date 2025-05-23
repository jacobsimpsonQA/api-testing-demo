HEAD
# API Testing Demo – Pokémon API

## Overview
This is a simple Python project that tests the public [PokéAPI](https://pokeapi.co/) using `requests`.

The test checks:
- API availability (status code 200)
- Correct Pokémon name returned
- That abilities data is present in the response

Great for showcasing beginner-level API testing and Python scripting.

## How to Run
1. Clone this repo
2. Install dependencies:
   ```
   pip3 install requests
   ```
3. Run the test:
   ```
   python3 test_pokemon_api.py
   ```

If successful, you’ll see:
```
✅ Pikachu API test passed!
```

## Tech Stack
- Python 3
- `requests` library
- PokéAPI (public REST API)

## Author

# Pytest API Demo

## Overview
A Pytest-based API test suite that interacts with the [PokéAPI](https://pokeapi.co/), built to demonstrate basic request handling, response validation, and negative test coverage.

This project showcases how to structure small but scalable API tests using Python, `requests`, and `pytest`.

---

## How to Run

1. Clone the repo and set up a virtual environment:
   python3 -m venv venv  
   source venv/bin/activate

2. Install dependencies:
   pip install -r requirements.txt

3. Run all tests:
   pytest

---

## Tests Included

| Test | Description |
|------|-------------|
| `test_get_pokemon()` | Validates that `/pokemon/pikachu` returns a 200 response with correct structure |
| `test_invalid_pokemon_returns_404()` | Sends request to a non-existent Pokémon and expects a 404 |
| `test_broken_endpoint_returns_404()` | Sends request to an invalid endpoint (`/pokemons`) and expects a 404 |
| `test_multiple_pokemon()` (x3) | Parameterized test that loops through multiple valid Pokémon and verifies structure |

---

## Tools Used

- Python 3  
- Pytest  
- requests  
- PokéAPI

---

## Author

Jacob Simpson – QA Engineer  
[github.com/jacobsimpsonQA](https://github.com/jacobsimpsonQA)
