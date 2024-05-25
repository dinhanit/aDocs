from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os
import json

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(api_key=api_key,temperature=0, model_name = "gpt-3.5-turbo")

template_eng = """
based on this contents: {information}. 
what is the "{word}"? and explain it.
Only return json format like this:
    "word": {word},
    "meaning": ...(explain on english),
    "level CEFR": ...,
    "parts of speech": ...,
    "explanation": ... (explain on english))

"""
template_vni = """
based on this contents: {information}. 
what is the "{word}" in vietnamese? and explain it using vietnamese.
Only return json format like this:
    "word": {word},
    "meaning": ...(explain on vietnamese),
    "level CEFR": ...,
    "parts of speech": ...,
    "explanation": ...(explain on vietnamese),)

"""

def explain_new_word(information:str,word:str,type:str="eng"):
    if type == "eng":
        summary_template = template_eng
    elif type == "vni":
        summary_template = template_vni
    else:
        raise ValueError("type must be 'eng' or 'vni'")
    summary_promt_templete = PromptTemplate(input_variables=["information","word"],template=summary_template)
    chain = summary_promt_templete | llm
    res = chain.invoke(input={"information":information,"word":word})
    json_obj = json.loads(res.content)
    return json_obj
