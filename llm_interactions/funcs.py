import openai
import os
import re

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

openai.api_key = os.getenv("OPENAI_API_KEY")

def breakdown_call(topic: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an education assistance engine. Your only task is to break down the incoming topic into subtopics which are prerequesites to become an expert in the incoming topic. You will list out the subtopics in the necessary order of learning separated by commas. In no case should you respond with any other prose than the subtopics. If the input is invalid or inappropriate, you must only respond with INPUT_INVALID."},
            {"role": "user", "content": topic},
        ],
        max_tokens=300,
    )
    generation = response.choices[0].message.content
    if "INPUT_INVALID" in generation:
        return {
            "status": "error",
            "topic": topic,
            "error": "INPUT_INVALID"
        }
    else:
        return {
            "status": "success",
            "topic": topic,
            "subtopics": re.findall(r'\b[\w\s&]+\b', generation)
        }
        
def single_describe_call(subtopic: str, context: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an education assistance engine. Your only task is to return 2 information in the format specified below. 1, a short description in around 50 words of the provided subtopic in the context of the provided context. 2, a google search query to be made to learn that subtopic. you MUST always follow this format and in no case include any prose. format: {\"description\":description,\"query\":search query}"},
            {"role": "user", "content": f"Subtopic: {subtopic}\nContext: {context}"},
        ],
        max_tokens=300,
    )
    generation = response.choices[0].message.content
    try:
        generation = eval(generation)
        return {
            "status": "success",
            "subtopic": subtopic,
            "context": context,
            "description": generation
        }
    except Exception as e:
        return {
            "status": "error",
            "subtopic": subtopic,
            "context": context,
            "error": e.__str__()
        }
    
    

def bulk_description_call(subtopics: list, context: str):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an education assistance engine. Your only task is to return 2 information in the format specified below. 1, a short description in around 50 words of each provided subtopic in the context of the provided context. 2, a google search query to be made to learn that subtopic. you MUST always follow this format and in no case include any prose. format: {\"subtopic\":{\"description\":description,\"query\":search query}, ...}"},
            {"role": "user", "content": f"Subtopic: {str(subtopics)}\nContext: {context}"},
        ],
        max_tokens=1000,
    )
    generation = response.choices[0].message.content
    try:
        generation = eval(generation)
        return {
            "status": "success",
            "subtopics": subtopics,
            "context": context,
            "descriptions": generation
        }
    except Exception as e:
        return {
            "status": "error",
            "subtopics": subtopics,
            "context": context,
            "error": e.__str__()
        }