#install and import the chatterbot module, Listrainers 
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

CORPUS_FILE = "_chat.txt"


chatbot = ChatBot("CraiG")

trainer = ListTrainer(chatbot)
cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(cleaned_corpus)
'''trainer.train([
    "hi",
    "Welcome friend",
])
trainer.train([
    "are you a girl?",
    "how dare you assume my gender???",
])'''
#creat an exit condition instance
exit_conditions = (":q", "quit", "exit")
while True:
    query = input(">")
    if query in exit_conditions:
        break
    else:
        print(f"FHENIX_A:  {chatbot.get_response(query)}")