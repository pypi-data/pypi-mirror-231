import pandas as pd
import sys
sys.path.append('/Users/artbrare/Documents/Morant/py_morant/src')

from pymorant import llm, chatbot # noqa

file_path = 'tests/k_escucha_muestra.xlsx'
openai_api_key = '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'
columna = 'body'
modelo = 'gpt-4'

chatbot = chatbot.Chatbot(openai_api_key, modelo, 1)

chatbot.vector_store_local(True)

chatbot.load_chain()
