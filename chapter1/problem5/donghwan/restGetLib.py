import requests
import json
import itertools


def getAnswerValue(jsonList, problemNum):
    for i in range(0, len(jsonList)):
        tempDict = jsonList[i]
        if tempDict['QuestionNum'] == str(problemNum):
            return tempDict['SolutionString']


def httpGetReq(problemNum):
    r = requests.get(url='http://178.62.70.235:8000/answers')
    print(r.json())
    array = r.json() #currently stored as array
    answerString = getAnswerValue(array, problemNum)
    return answerString


if __name__ == "__main__":
    httpGetReq(5)
