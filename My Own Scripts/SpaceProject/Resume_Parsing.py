import spacy #nlp
import pdfminer #pdf2tx
import re #regex
import os #file manip
import pandas as pd #csv - tabular
import pdf2txt

pd.set_option('display.max_columns', None)


def convert_pdf(f):

    output_filename = os.path.basename(os.path.splitext(f)[0]) + ".txt"
    output_filepath = os.path.join("Output/txt/", output_filename)
    pdf2txt.main(args=[f, "--outfile", output_filepath]) #pdf to txt and save it in the given location
    print(output_filepath + " saved successfully!!!")
    return open(output_filepath).read()


# load the language model
nlp = spacy.load("en_core_web_sm")

result_dict = {'name': [], 'phone': [], 'email': [], 'skills': []}
names = []
phones = []
emails = []
skills = []


def parse_content(text):
    skillset = re.compile("python|excel|sql|mssql|power bi")
    phone_num = re.compile(
        "(\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4})"
    )
    doc = nlp(text)
    # First name you detect on the resume file
    # Instead writing for loop, we write on list comprehension
    name = [entity.text for entity in doc.ents if entity.label_ is "PERSON"][0]
    print(name)
    email = [word for word in doc if word.like_email is True][0]
    print(email)
    # text.lower() - is to find all string that equal to text - upper and lower string
    phone = str(re.findall(phone_num, text.lower()))
    # text.lower() - is to find all string that equal to text - upper and lower string
    skills_list = re.findall(skillset, text.lower())
    # Convert to a single skills of list to string
    unique_skills_list = str(set(skills_list))
    names.append(name)
    emails.append(email)
    phones.append(phone)
    skills.append(unique_skills_list)
    print("Extraction completed successfully!!!")


for file in os.listdir('Resumes/'):
    if file.endswith('.pdf'):
        print('Reading.....' + file)
        txt = convert_pdf(os.path.join('Resumes/', file))
        parse_content(txt)


result_dict['name'] = names
result_dict['phone'] = phones
result_dict['email'] = emails
result_dict['skills'] = skills

result_df = pd.DataFrame(result_dict)
print(result_df)
result_df.to_csv('output/csv/parsed_resumes.csv')