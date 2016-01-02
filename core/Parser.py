import json
import os
import re

import requests

from core import Constants

def getHtmlFromUrl(url):
    htmlData = requests.get(url).text
    assert isinstance(htmlData, object)
    return htmlData

def getJsonDataFromUrl(url):
    assert isinstance(requests.get(url).json, object)
    return requests.get(url).json()

def getJsonDataFromFile(fileName):
    return json.loads(open(fileName))

def getInputOutputFromHtml(body):
    body = body[body.find("<h3>Example</h3>"):]
    body = body[body.find("<pre>"):body.find("</pre>")]
    body = re.sub("<.*?>", "", body)
    inputString = re.sub("\n\n","\n",body[body.find("Input:")+7:body.find("Output")])
    outputString = re.sub("\n\n","\n",body[body.find("Output:")+8:])
    print("Input string is :")
    print(inputString)
    print("Output string is :")
    print(outputString)
    print('******************************************')
    return (inputString,outputString)

def getContest(contestCode,data):
    problemData = {}
    if 'problems_data' not in data:
        print("Problems not embedded. Fetching individual problems:")
        for problem in data['problems']:
            print(problem)
            problemData[str(problem)] = {}
            problemData[str(problem)]["body"] = getHtmlFromUrl( Constants.CODECHEF_PROBLEM_URL + problem ) # urlopen(CODECHEF_PROBLEM_URL+problem).read())
    else :
        problemData = data["problems_data"]
    if not os.path.exists(Constants.INOUT_DEFAULT_DIR + contestCode):
            os.makedirs(Constants.INOUT_DEFAULT_DIR + contestCode)
    for problem in problemData:
        inputString,outputString = getInputOutputFromHtml(problemData[problem]["body"])
        inputFile = open(Constants.INOUT_DEFAULT_DIR + contestCode + "/" + problem + ".in", 'w')
        inputFile.write(inputString)
        outputFile = open(Constants.INOUT_DEFAULT_DIR + contestCode + "/" + problem + ".out", 'w')
        outputFile.write(outputString)



