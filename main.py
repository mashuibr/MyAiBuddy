import nltk
from nltk.chat.util import Chat, reflections

pairs = [
    ["hi", ["Hello!", "Hi there!"]],
    ["what is your name?", ["I'm your AiBuddy."]],
    ["quit", ["Bye!"]]
]

chat = Chat(pairs, reflections)
chat.converse()