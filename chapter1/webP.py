#!/usr/bin/python3
# -*- coding: utf-8 -*-

import codecs
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as bs
import time


def startPoint():
    print('Welcome to KERT Web parser application')
    print('please type 1 to start the program')
    command = input()
    if command is '1':
        print ('enter target URL address')
        pointURL = input()
        print ('enter description')
        pageDesc = input()
    return (pointURL, pageDesc)


class testParser:

    fileWebHref = []
    siteWebHref = []
    webTitle = []
    targetURL = ''
    changes = 0
    newWebHref = []

    def __init__(self, targetURL, pageDesc):
        self.targetURL = targetURL
        self.changes = 0
        soup = bs(uReq(targetURL).read(), 'html.parser')
        fileName = './test/' + pageDesc + '.txt'
        fileSoup = codecs.open(fileName, 'w', encoding='utf8')

        for links in soup.findAll('a'):
            eachLink = str(links.get('href'))
            if '/102' in eachLink:
                # print(eachLink)
                fileSoup.write(eachLink + '\n')
        fileSoup.close()

    def readLinksFromFile(self):
        with open('./test/ilbe.txt') as fileEntry:
            links = fileEntry.readlines()
            for link in links:
                # print(link.replace('\n',''))
                self.fileWebHref.append(link.replace('\n', ''))

    def readLinksFromSite(self, targetURL):
        soup = bs(uReq(targetURL).read(), 'html.parser')

        for links in soup.findAll('a'):
            eachLink = str(links.get('href'))
            if '/102' in eachLink:
                self.siteWebHref.append(eachLink)

    def linksCompare(self):
        # print("\n\n\n")
        for i in range(0, len(self.siteWebHref)-1):
            # print((i, self.fileWebHref[i]))
            # print((i, self.siteWebHref[i]))
            # print(("\n\n"))
            if self.siteWebHref[i] == self.fileWebHref[i]:
                continue
            else:
                self.newWebHref.append(self.siteWebHref[i])
                self.changes = 1

    def updateFileHref(self):
        with open('./test/ilbe.txt', 'w', encoding='utf8') as fileEntry:
            for i in range(0, len(self.siteWebHref) - 1):
                fileEntry.write(self.siteWebHref[i] + '\n')
        fileEntry.close()

    def updateAlert(self):
        for i in range(0, len(self.newWebHref) - 1):
            print(self.newWebHref[i])
        self.newWebHref = []

if __name__ == '__main__':
    tempList = []  # incharge of old announce lists
    pointURL = ''  # incharge of targetURL
    pageDesc = ''  # incharge of Page Description

    (pointURL, pageDesc) = startPoint()
    ilbeParser = testParser(pointURL, pageDesc)

    while True:
        ilbeParser.readLinksFromSite(pointURL)
        ilbeParser.readLinksFromFile()

        tempValue = ilbeParser.linksCompare() #value return test
        if ilbeParser.changes == 1:
            ilbeParser.updateAlert()
            ilbeParser.updateFileHref()
        time.sleep(5)
