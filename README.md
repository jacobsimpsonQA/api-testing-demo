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
Jacob Simpson – QA Engineer  
[github.com/jacobsimpsonQA](https://github.com/jacobsimpsonQA)
