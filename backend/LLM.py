from openai import OpenAI
import re
import random

def get_ideal_profiles(idea, designations):
    client = OpenAI(
        base_url = 'http://localhost:11434/v1',
        api_key='llama',
    )

    ceo_query =  "what are the technical and management skills essentail for the CEO to implement the idea '"+idea+"'"
    cmo_query =  "what are the technical and marketing skills essentail for the CMO to implement the idea '"+idea+"'"
    cto_query =  "what are the technical and strategic skills essentail for the CTO to implement the idea '"+idea+"'"
    ceo_description = ''
    cmo_description = ''
    cto_description = ''

    if "ceo" in designations:
        print("inside ceo")
        response_ceo = client.chat.completions.create(
            model="llama2",                                       
            messages=[
                {"role": "system", "content": ceo_query },]
        )
        ceo_description = response_ceo.choices[0].message.content

    if "cmo" in designations:
        print("inside cmo")
        response_cmo = client.chat.completions.create(
            model="llama2",                                       
            messages=[
                {"role": "system", "content": cmo_query },]
        )
        cmo_description = response_cmo.choices[0].message.content

    if "cto" in designations:
        print("inside cto")
        response_cto = client.chat.completions.create(
            model="llama2",                                       
            messages=[
                {"role": "system", "content": cto_query },]
        )
        cto_description = response_cto.choices[0].message.content

    descriptions = {}

    descriptions['ceo'] = ceo_description
    descriptions['cmo'] = cmo_description
    descriptions['cto'] = cto_description

    return descriptions

def generate_profile_names():
    client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='llama',
    )

    response = client.chat.completions.create(
    model="llama2",                                  
    messages=[
        {"role": "system", "content": "generate any 5 completely random indian names with surnames and just return the names in python list. give one line response"},]
    )
    names_string = str(response.choices[0].message.content)
    print(names_string)

    pattern = r'\b[A-Z][a-z]+\s[A-Z][a-z]+\b'
    names = re.findall(pattern, names_string)

    if names == []:
        names = ['Rajiv Tiwari', 'Nivedita Sharma', 'Aravind Kumar', 'Megha Verma', 'Arjun Rai']

    return names

def generate_community_names():
    client = OpenAI(
    base_url = 'http://localhost:11434/v1',
    api_key='llama',
    )

    response = client.chat.completions.create(
    model="llama2",                                  
    messages=[
        {"role": "system", "content": "list down 90 unique and rare indian names with surnames in the format name surname. give one line response."},]
    )
    names_string = str(response.choices[0].message.content)
    names = re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', names_string)

    print(names)

    random_number1 = random.randint(8, 20)
    names1 = names[0:random_number1]
    random_number2 = random.randint(8, 20)
    names2 = names[random_number1:random_number1+random_number2]
    random_number3 = random.randint(8, 20)
    names3 = names[random_number1+random_number2:random_number1+random_number2+random_number3]


    community = [names1, names2, names3]

    return community
