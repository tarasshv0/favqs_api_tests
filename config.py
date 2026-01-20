import os

BASE_URL = "https://favqs.com/api"
FAVQS_API_KEY = os.getenv("FAVQS_API_KEY")

if not FAVQS_API_KEY:
    raise RuntimeError(
        "FAVQS_API_KEY is not set. "
        "Generate it at https://favqs.com/api_keys "
        "and set it as environment variable."
    )
