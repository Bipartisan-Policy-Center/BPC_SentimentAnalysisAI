import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 import Features, CategoriesOptions
from ibm_watson.natural_language_understanding_v1 import Features, EntitiesOptions, KeywordsOptions
import os

""" Analyzes the sentiment of text files. """

authenticator = IAMAuthenticator('{API_TOKEN}')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2021-08-01',
    authenticator=authenticator
)

natural_language_understanding.set_service_url('{API_}')

def convert_file_to_string(file):
    #open text file in read mode
    text_file = open(file, "r")

    #read whole file to a string
    data = text_file.read()
    return data

string_contents = convert_file_to_string('data/UNGP_BigDataGuide2016_ Web (1).txt')


# directory_name = 'data'
#
# for file_name in os.listdir(directory_name):
#     i = os.path.join(directory_name, file_name)
#     if os.path.isfile(i):
#         string_contents = convert_file_to_string(i)
#         string_contents = string_contents.encode().decode()
response = natural_language_understanding.analyze(
    text=string_contents,
    features=Features(
        keywords=KeywordsOptions(emotion=True, sentiment=True, limit=2))).get_result()
print(json.dumps(response, indent=2))
