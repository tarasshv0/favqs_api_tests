# FavQs API Test Automation

This project contains automated tests for the FavQs API, structured similarly to the OTT portal API tests.

## Project Structure

```
favqs_api/
├── requests/              # API request classes
│   ├── favqs_api_base_request.py
│   ├── favqs_api_post_request.py
│   └── favqs_api_put_request.py
├── tests/                # Test cases
│   ├── base_tc.py
│   └── test_user_management.py
├── requirements.txt      # Python dependencies
└── README.md
```

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Generate your API key from https://favqs.com/api_keys

3. Set the API key as an environment variable:
```bash
export FAVQS_API_KEY='your_api_key_here'
```

   Or on Windows:
```bash
set FAVQS_API_KEY=your_api_key_here
```

   **Note:** The API key is required for all API requests. You must generate it from https://favqs.com/api_keys before running the tests.

## Running Tests

Run tests using unittest:
```bash
python -m unittest favqs_api.tests.test_user_management
```

Or run with verbose output:
```bash
python -m unittest favqs_api.tests.test_user_management -v
```

## Tests

### Test 1: Create User and Retrieve User Information
- Creates a new user via API
- Retrieves user information using PUT /api/users/:login
- Verifies that login and email fields match

### Test 2: Update User
- Creates a user
- Updates user login and email
- Retrieves updated user information
- Verifies that updated fields match expected values

## Requirements

- Python 3.6+
- requests library
- unittest (built-in Python module)

## Troubleshooting

### API Key Error
If you see an error about `FAVQS_API_KEY` not being set:
1. Make sure you've generated an API key from https://favqs.com/api_keys
2. Set it as an environment variable before running tests:
   ```bash
   export FAVQS_API_KEY='your_api_key_here'
   python -m unittest favqs_api.tests.test_user_management -v
   ```

### Verify API Key is Set
You can verify your API key is set correctly:
```bash
echo $FAVQS_API_KEY  # Linux/Mac
echo %FAVQS_API_KEY%  # Windows
```
