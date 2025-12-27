# llama_llm.py
from crewai import LLM
from settings import HUGGINGFACE_API_KEY, HF_MODEL
llama_llm = LLM(
model=HF_MODEL,
api_key=HUGGINGFACE_API_KEY,
temperature=0.1,
max_tokens=1024,
)