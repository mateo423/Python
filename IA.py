import nltk
from nltk.stem import WordNetLemmatizer
import numpy as np
import random
import json
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
import requests
from bs4 import BeautifulSoup

nltk.download("punkt")
nltk.download("wordnet")

lemmatizer = WordNetLemmatizer()

with open("intents.json") as file:
    data = json.load(file)

words = []
labels = []
docs_x = []
docs_y = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokenized_words = nltk.word_tokenize(pattern)
        words.extend(tokenized_words)
        docs_x.append(tokenized_words)
        docs_y.append(intent["tag"])
    
    if intent["tag"] not in labels:
        labels.append(intent["tag"])

words = [lemmatizer.lemmatize(w.lower()) for w in words if w != "?"]
words = sorted(list(set(words)))

labels = sorted(labels)

training = []
output = []

out_empty = [0 for _ in range(len(labels))]

for x, doc in enumerate(docs_x):
    bag = []
    
    tokenized_doc = [lemmatizer.lemmatize(word.lower()) for word in doc]
    
    for word in words:
        bag.append(1) if word in tokenized_doc else bag.append(0)
        
    output_row = out_empty[:]
    output_row[labels.index(docs_y[x])] = 1
    
    training.append(bag)
    output.append(output_row)

training = np.array(training)
output = np.array(output)

model = Sequential()
model.add(Dense(128, input_shape=(len(training[0]),), activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(64, activation="relu"))
model.add(Dropout(0.5))
model.add(Dense(len(output[0]), activation="softmax"))

initial_learning_rate = 0.01
lr_schedule = tf.keras.optimizers.schedules.ExponentialDecay(
    initial_learning_rate,
    decay_steps=10000,
    decay_rate=0.96,
    staircase=True
)
sgd = SGD(learning_rate=lr_schedule, momentum=0.9, nesterov=True)
model.compile(loss="categorical_crossentropy", optimizer=sgd, metrics=["accuracy"])

model.fit(training, output, epochs=200, batch_size=5, verbose=1)

def predict_intent(sentence):
    tokenized_words = nltk.word_tokenize(sentence)
    tokenized_words = [lemmatizer.lemmatize(word.lower()) for word in tokenized_words]
    bag = [0 for _ in range(len(words))]
    for w in tokenized_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i] = 1
                
    result = model.predict(np.array([bag]))[0]
    threshold = 0.25
    results = [[i, r] for i, r in enumerate(result) if r > threshold]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": labels[r[0]], "probability": str(r[1])})
    
    return return_list

def get_response(intents_list, intents_json):
    tag = intents_list[0]["intent"]
    list_of_intents = intents_json["intents"]
    for i in list_of_intents:
        if i["tag"] == tag:
            result = random.choice(i["responses"])
            break
# Ask for feedback if response is not satisfactory
    feedback = input("Bot: " + result + "\nBot: Was this response helpful? (yes/no): ").lower()
    while feedback not in ["yes", "no"]:
      feedback = input("Bot: Please enter 'yes' or 'no': ").lower()
    if feedback == "no":
      new_response = input("Bot: Please enter a better response: ")
      i["responses"].append(new_response)
      with open("intents.json", "w") as file:
        json.dump(intents_json, file)
      print("Bot: Response added to intents.json")

    return result
print("Bot: Bienvenido a la IA de respuesta de mensajes. Escribe 'bye' para salir.")
while True:
  user_input = input("You: ")
  if user_input.lower() == "bye":
    print("Bot: Bye! Take care.")
    break
  intents = predict_intent(user_input)
  response = get_response(intents, data)
  print("Bot:", response)