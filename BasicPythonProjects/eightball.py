from random import choice

answers = ["It is certain", "Outlook good", "You may rely on it", "Ask again later", "Concentrate and ask again", "Reply hazy, try again", "My reply is no", "My sources say no"]
raw_input("Ask your question to magic eight ball: ")

print("Answer: {}".format(choice(answers)))