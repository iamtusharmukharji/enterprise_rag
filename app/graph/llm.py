from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from typing import Literal
from app.credentials import credentials

def get_llm(provider : Literal['openai', 'google'] = 'google') -> ChatGoogleGenerativeAI | ChatOpenAI:

    if provider == 'google':
        llm = ChatGoogleGenerativeAI(
            api_key = credentials.gemini_api_key,
            model=credentials.gemini_model,
            temperature=0.0,
        )
    
    elif provider == 'openai':
        llm = ChatOpenAI(
            model=credentials.openai_model,
            temperature=0,
            # max_tokens=None,
            # timeout=None,
            max_retries=2,
            api_key=credentials.openai_api_key,)
    
    else:

        raise TypeError("Invalid model provider, select between 'openai' or 'gemini'")

    return llm


