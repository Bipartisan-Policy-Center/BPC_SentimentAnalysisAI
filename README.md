# Bipartisan Policy Center Sentiment Analysis on Artificial Intelligence Frameworks

# Table of contents

* [About](#about)
* [Replicate](#replicate)
  * [CURL Request for HTML/web-based frameworks](#curl-request)
  * [Python File for text-based frameworks](#text-frameworks)
* [Future work](#future-work)
* [Results](#results)
* [Data used](#data-used)
* [Contact](#contact)

## About

Curating legislation surrounding technology is quite difficult, especially when features innovate faster than legislators can keep up with. As a result, several sectors of society have proposed frameworks, standards, or other guides to influence behaviors around certain technologies. While most are voluntary, they each propose a different way to act--whether in regard to the risk, impact, or ethical consequence that it poses. This analysis examines different standards of AI usage from the public and private sector, aiming to sense the overal sentiment in regard to different measures (such as region, industry, or even organization). 

This is a repository containing data input used, results found, and steps to recreate the analysis found in TODO: LINK PAPER. The repository is maintained by Bipartisan Policy Center. Please visit the Bipartisan Policy Center website TODO: LINK for more information.


## Replicate

- Request an API token from or request a cluster of [IBM's Watson Natural Language Processing](https://www.ibm.com/cloud/watson-natural-language-understanding?utm_content=SRCWW&p1=Search&p4=43700068006592498&p5=p&gclid=Cj0KCQiAu62QBhC7ARIsALXijXS0qtU7tZeXmW1k_8yrWUedmYLJfw0Ler9UlB6ZXJ3-YmcXbMlnsXEaAp-4EALw_wcB&gclsrc=aw.ds)

 - Clone the Repository
    
    With HTTPS:

    ```https://github.com/Bipartisan-Policy-Center/BPC_SentimentAnalysisAI.git```

    or With SSH:

    ```git@github.com:Bipartisan-Policy-Center/BPC_SentimentAnalysisAI.git```
    
    or With GitHub CLI:
    
    ```gh repo clone Bipartisan-Policy-Center/BPC_SentimentAnalysisAI```


### CURL Request

For web/html based frameworks:

 - Test that curl is installed on your machine by running the command `curl -V`
    
 - Run the curl request on the data contained in the data_input folder or on other html-based AI Frameworks.

    We ran a curl request with the basic syntax (based on the curl request from the [Getting Started Guide](https://cloud.ibm.com/docs/natural-language-understanding?topic=natural-language-understanding-getting-started#getting-started-tutorial):

    ```
    curl -X POST -u "apikey:{api-key}" --header "Content-Type: application/json" --data '{
      "url": "https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community",
      "features": {
        "sentiment": {}
      }
    }' {url}/v1/analyze?version=2019-07-12"
    ```
    
    Note: the {api-key} and {url} tags are meant to be replaced (including the '{' and '}') with the user's API credentials.

    However, curl requests with this API can include more features, such as:

    ```
     "categories": {},
        "concepts": {},
        "entities": {},
        "keywords": {}
    ```


    Note: for Windows users, the command might look a little different:

    ```
    curl -X POST -u "apikey:{apikey}" --header "Content-Type: application/json" --data "{\"url\":\"https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community\",\"features\":{\"sentiment\":{},\"categories\":{},\"concepts\":{},\"entities\":{},\"keywords\":{}}}" "{url}/v1/analyze?version=2019-07-12"
    ```


### Text Frameworks

For pdf/text-based frameworks

- Ensure that you have python3 installed on your machine by running `python --version`
- run `pip install --upgrade "ibm-watson>=5.3.0"`
- Change the `{API Key}` (line 8) to your own key and the `{url}` (line 14) to your service URL as provided by IBM
- Change the name of the file called on `convert_file_to_string` to the name of the file for the framework you're analyzing (line 24)
- run the command `python3 text_sentiment.py`

## Future work

Currently, this project examines AI Frameworks (Ethics, Impact, and Risk) from different sectors (Private, Academia, Advocacy, and Government) using IBM's Watson Natural Language Processing. This project could be furthered by using different sentiment analysis algorithms and the data could be widened to include other technology frameworks or other sectors with the overarching goal of determining sentiment towards technology in policy. From a more technical standpoint, an AI could be trained to detect sentiment and/or emotion of keywords in technology policy specifically.

## Results
TODO: INSERT GRAPHICS HERE


## Data used

The data used in this project is compiled from multiple lists and searches for AI Frameworks (Ethics, Impact, and Risk).


## Contact

If you have any questions or concerns about this project please contact:

- [Rachael Harris](https://github.com/rachaelharris) (harrisr@allegheny.edu)
