# settings.py
import os
from dotenv import load_dotenv
load_dotenv()
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
HF_MODEL = os.getenv(
    "HF_MODEL",
    "huggingface/meta-llama/Meta-Llama-3-8B-Instruct",
)
# Normalize any unicode minus signs to ASCII hyphen to avoid invalid model ids
if HF_MODEL:
    HF_MODEL = HF_MODEL.replace("−", "-")
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
if HUGGINGFACE_API_KEY is None:
    raise RuntimeError("Missing HUGGINGFACE_API_KEY")
if SERPER_API_KEY is None:
    raise RuntimeError("Missing SERPER_API_KEY")