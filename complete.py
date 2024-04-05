import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from langchain import OpenAI, ConversationChain, LLMChain, PromptTemplate
# from langchain.chains.conversation.memory import ConversationBufferWindowMemory
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI, OpenAI
from langchain.prompts import PromptTemplate

# Load environment variables from .env file
load_dotenv('.env')

# Initializes your app with your bot token and socket mode handler
app = App(token=os.environ.get("SLACK_BOT_TOKEN"))


prompt_template1 = PromptTemplate.from_template(

   """You're the expert in writing job proposals. Your task is to craft the perfect proposal based on the provided details.
   remove all memory give me answer only from this context
                    DOCUMENT:
                    ==========
                    this is client job description
                    +++++++++++++++++++++++++++
                    {job_description}
                    ++++++++++++++++++++++++++

                    
                    
                    5)at last add this
                    modify template according to my information. 
                   
                    INSTRUCTIONS:
                    ==========
                    1)if message is irrelvent like hi, how are you, hello etc then you give responce please provide proper information
                    2)output in the form of as a perposal of job description.
                    3)write projects which only relevent to job description. only mentioned name and link at end.
                    4)all details will be simple and easy understandable.
                    5)all information will be as humen written.
                    

                    QUESTION
    """

)

chat = ChatOpenAI(temperature=0.5, model_name= "gpt-3.5-turbo-0125")

#Message handler for Slack
@app.message(".*")
def message_handler(message, say, logger):
    # global prompt_template
    # print(message, "\n"*20)ss
    
    # output = chatgpt_chain.predict(human_input = message['text']) 
    # print(prompt_template)
    print("working start")
    # prompt_template = prompt_template1
    prompt_template1 = prompt_template1.format(job_description=message['text'])
    # print(prompt_template)
    output = chat.predict(prompt_template)
    # print(output) 
    say(output)


@app.event("app_mention")
def handle_app_mention_events(body, say, logger):
    print("body is :", body['event']['text'])


    prompt_template = prompt_template1
    prompt_template = prompt_template.format(job_description=body['event']['text'])
    # print(prompt_template)
    output = chat.predict(prompt_template)
    say(output)



# Start your app
if __name__ == "__main__":
    SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"]).start()