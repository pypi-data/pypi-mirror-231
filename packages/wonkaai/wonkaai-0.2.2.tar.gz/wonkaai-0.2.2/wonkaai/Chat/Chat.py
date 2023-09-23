from langchain.chat_models import ChatOpenAI
from os import getenv


class Chat():

    def __init__(self, prompt_template, **kwargs) :
        self.chat_model = ChatOpenAI(model="gpt-3.5-turbo-0613", **kwargs)
        self.prompt_template = prompt_template

    def generate(self, no_error=True, **input):
        try :
            response = self.chat_model(self.prompt_template.format_messages(**input))
            return response.content
        except Exception as e:
            if no_error:
                print(e)
                return("ERROR")
            else :
                raise e
            


    