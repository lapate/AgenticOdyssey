"""
Setup Validation Script for AgenticOdyssey Workshop

Run this script to verify your environment is correctly configured:
    python docs/validate_setup.py
"""

import sys
import os
import importlib


def check(label: str, ok: bool, detail: str = "") -> bool:
    status = "✅" if ok else "❌"
    suffix = f"  ({detail})" if detail else ""
    print(f"  {status}  {label}{suffix}")
    return ok


def main() -> int:
    print("\n🔍 AgenticOdyssey — Environment Validation\n")
    failures = 0

    # Python version
    py_ok = sys.version_info >= (3, 10)
    if not check("Python 3.10+", py_ok, f"found {sys.version.split()[0]}"):
        failures += 1

    # Required packages
    packages = {
        "openai": "openai",
        "azure-identity": "azure.identity",
        "pyautogen": "autogen",
        "azure-search-documents": "azure.search.documents",
        "python-dotenv": "dotenv",
        "rich": "rich",
    }
    for display_name, module_path in packages.items():
        try:
            importlib.import_module(module_path)
            check(display_name, True)
        except ImportError:
            check(display_name, False, "not installed — run: pip install -r requirements.txt")
            failures += 1

    # .env file
    env_path = os.path.join(os.path.dirname(__file__), "..", ".env")
    env_exists = os.path.isfile(env_path)
    if not check(".env file found", env_exists, "copy .env.example to .env and fill in your credentials"):
        failures += 1

    # Load .env and check required keys
    if env_exists:
        from dotenv import load_dotenv  # noqa: PLC0415

        load_dotenv(env_path)

    required_keys = [
        "AZURE_OPENAI_ENDPOINT",
        "AZURE_OPENAI_API_KEY",
        "AZURE_OPENAI_API_VERSION",
        "AZURE_OPENAI_DEPLOYMENT_NAME",
    ]
    for key in required_keys:
        val = os.getenv(key)
        key_ok = bool(val and val.strip() and not val.startswith("<"))
        if not check(f"  {key} set", key_ok, "missing or placeholder value in .env"):
            failures += 1

    # Live Azure OpenAI ping
    if not failures:
        print()
        print("  🌐 Testing Azure OpenAI connection …")
        try:
            from openai import AzureOpenAI  # noqa: PLC0415

            client = AzureOpenAI(
                azure_endpoint=os.environ["AZURE_OPENAI_ENDPOINT"],
                api_key=os.environ["AZURE_OPENAI_API_KEY"],
                api_version=os.environ["AZURE_OPENAI_API_VERSION"],
            )
            resp = client.chat.completions.create(
                model=os.environ["AZURE_OPENAI_DEPLOYMENT_NAME"],
                messages=[{"role": "user", "content": "Reply with exactly: PONG"}],
                max_tokens=10,
            )
            reply = resp.choices[0].message.content or ""
            check("Azure OpenAI ping", True, f"model: {os.environ['AZURE_OPENAI_DEPLOYMENT_NAME']}, reply: {reply.strip()}")
        except Exception as exc:  # noqa: BLE001
            check("Azure OpenAI ping", False, str(exc))
            failures += 1

    print()
    if failures:
        print(f"  ⚠️  {failures} issue(s) found. Fix them before starting the labs.\n")
        return 1

    print("  🎉 All checks passed! You're ready for the workshop.\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
