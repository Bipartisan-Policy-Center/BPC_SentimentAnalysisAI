import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions

""" Analyzes the sentiment of text files. """"

authenticator = IAMAuthenticator('{API Key}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('{url}')

def convert_file_to_string(file):
    #open text file in read mode
    text_file = open(file, "r")

    #read whole file to a string
    data = text_file.read()
return data

string_contents = convert_file_to_string('file')

response = natural_language_understanding.analyze(
    text=string_contents,
    features=Features(categories=CategoriesOptions(limit=3))).get_result()

print(json.dumps(response, indent=2))
