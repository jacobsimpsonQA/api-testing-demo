# API Testing Demo

A compact, beginner-friendly API testing suite using `pytest` and the public [PokéAPI](https://pokeapi.co). Built to demonstrate real-world API testing patterns for QA Engineer interviews and portfolio projects.

---

## 🔍 What's Tested

- ✅ Valid API response for a known Pokémon (`pikachu`)
- ❌ Invalid Pokémon name returns `404`
- ♻️ Parameterized test: checks multiple Pokémon by name
- ⚠️ Broken endpoint returns `404` (bad route)
- 🕒 Rate limiting behavior: tests server response to rapid requests

---

## 🧠 Why This Project Matters

This suite showcases:
- Practical QA thinking beyond happy paths
- Handling API failure modes like invalid input and rate limits
- Clean, reusable testing logic in Python
- Familiarity with real-world tools like `pytest`, `requests`, and GitHub workflows

It’s built as a portfolio-ready proof of hands-on QA ability—especially valuable for Senior QA or QA Lead interviews that ask about API-level validation.

---

## 🚀 Running the Tests

1. Clone this repo  
2. Set up your Python environment and install dependencies:  
   ```bash
   pip install pytest requests
   ```
3. Run the suite:  
   ```bash
   pytest
   ```

---

## 📁 Project Structure

```
api-testing-demo/
├── test_pokemon_api.py   # Main test file
├── README.md             # You're looking at it
└── venv/                 # (optional) Virtual environment folder
```

---

## 🧪 Test Sample Output

```
test_pokemon_api.py ......                                     [100%]
7 passed in 3.15s
```

---

## 🤝 Let’s Connect

If you're into QA, automation, or gaming tech, feel free to reach out or fork the repo!

---

## 🏷️ Tags

`#qa` `#pytest` `#automation` `#api-testing` `#opentowork` `#gamingjobs`
