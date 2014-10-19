#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = 'patas'

import urllib
import lxml.html
import subprocess

list = []
ADR='http://www.uchlupatyhoducha.cz/restaurace/denni-menu/'

def runcmd(cmd):
    p = subprocess.Popen(cmd, shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
    out = p.stdout.read().strip('\n')
    err = p.stderr.read().strip('\n')
#    print out
#    print err

def htmlParser(adresa):
	connection = urllib.urlopen(adresa)
	dom = lxml.html.fromstring(connection.read())
	for link in dom.xpath('//a/@href'): list.append(link)

#MAIN
htmlParser(ADR)
content = list[3]
adresa = content.replace(' ', '%20')
cmd='curl '+adresa+' > ./duch.pdf'
runcmd(cmd)
cmd='pdftotext ./duch.pdf ./duch.txt'
runcmd(cmd)
