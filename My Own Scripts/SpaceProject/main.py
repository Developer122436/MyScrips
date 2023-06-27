import spacy

# Download the English language model
nlp = spacy.load("en_core_web_sm")

text = "Google was initially funded by an August 1998 contribution of $100,000 from Andy Bechtolsheim, co-founder of Sun Microsystems; the money was given before Google was incorpora"

# Makes word tokenization - creates text that knows what is the part of speech tagging in it
# and split the input text based on token, we are going to split the entire text word by word
# so word is the token for us here.
doc = nlp(text)

for token in doc:
    if token.pos == 'NOUN':
        print(token)

for token in doc:
    if token.pos_ == "ADJ":
        print(token)

for entity in doc.ents:
    print(entity.text, entity.label_)
