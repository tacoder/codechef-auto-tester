import json,os
import re
from urllib2 import urlopen
CODECHEF_API_URL = 'https://www.codechef.com/api/contests/'
CODECHEF_PROBLEM_URL = 'https://www.codechef.com/problems/'

#contestCode = "DEC15"


def getContest(contestCode):
    data = json.load(urlopen(CODECHEF_API_URL+contestCode))#open('DEC15' + '.json'))
    problemData = {}
    if 'problems_data' not in data:
        print("Problems not embedded. Fetching individual problems:")
        for problem in data['problems']:
            print(problem)
            problemData[str(problem)] = {}
            problemData[str(problem)]["body"] = (urlopen(CODECHEF_PROBLEM_URL+problem).read())
    else :
        problemData = data["problems_data"]
    if not os.path.exists(contestCode):
            os.makedirs(contestCode)
    for problem in problemData:
        body = problemData[problem]["body"]
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
        inputFile = open(contestCode + "/" + problem + ".in",'w')
        inputFile.write(inputString)
        outputFile = open(contestCode + "/" + problem + ".out",'w')
        outputFile.write(outputString)


getContest("DEC15");
