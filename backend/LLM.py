from openai import OpenAI

class LLM:
    def __init__(self):
        self.client = OpenAI(
            base_url = 'http://localhost:11434/v1',
            api_key='llama',
        )

    def get_ideal_profiles(self, idea, designations):
        ceo_query =  "what are the technical and management skills essentail for the CEO to implement the idea '"+idea+"'"
        cmo_query =  "what are the technical and marketing skills essentail for the CMO to implement the idea '"+idea+"'"
        cto_query =  "what are the technical and strategic skills essentail for the CTO to implement the idea '"+idea+"'"
        ceo_description = ''
        cmo_description = ''
        cto_description = ''
        if "ceo" in designations:
            response_ceo = self.client.chat.completions.create(
                model="llama2",                                       
                messages=[
                    {"role": "system", "content": ceo_query },]
            )
            ceo_description = response_ceo.choices[0].message.content

        if "cmo" in designations:
            response_cmo = self.client.chat.completions.create(
                model="llama2",                                       
                messages=[
                    {"role": "system", "content": cmo_query },]
            )
            cmo_description = response_cmo.choices[0].message.content

        if "cto" in designations:
            response_cto = self.client.chat.completions.create(
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
