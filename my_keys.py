import os
from pathlib import Path
from dotenv import load_dotenv

project_root = Path(__file__).resolve().parent
workspace_root = project_root.parent

for env_path in (project_root / ".env", workspace_root / ".env", project_root / "datos" / ".env"):
    if env_path.exists():
        load_dotenv(dotenv_path=env_path)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

if not GEMINI_API_KEY:
    raise RuntimeError(
        "GEMINI_API_KEY is not set. Create a .env file in the project root with:\n"
        "GEMINI_API_KEY=your_gemini_api_key_here\n"
        "COHERE_API_KEY=your_cohere_api_key_here\n"
        "Then rerun the script."
    )
