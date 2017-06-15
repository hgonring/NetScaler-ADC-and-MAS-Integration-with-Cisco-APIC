#!/usr/bin/python

import glob
import json
import os
import os.path
import requests
import sys
import time
import xml.dom.minidom
import yaml
requests.packages.urllib3.disable_warnings()

try:
    cfgFile = sys.argv[1]
except Exception as e:
    print str(e)
    sys.exit(0)

with open( cfgFile, 'r' ) as config:
    config = yaml.safe_load( config )

auth = {
    'aaaUser': {
        'attributes': {
            'name': config['name'],
            'pwd': config['passwd']
            }
        }
    }

status = 0
while( status != 200 ):
    url = 'https://%s/api/aaaLogin.json' % config['host']
    while(1):
        try:
            r = requests.post( url, data=json.dumps(auth), timeout=1, verify=False )
            break;
        except Exception as e:
            print "timeout"
    status = r.status_code
#    print r.text
    cookies = r.cookies
    time.sleep(1)





def isTestCalled(i):
    testCalled = False
    if len(sys.argv)>2:
        testListString = sys.argv[2].split(",")
        testList = [int(numeric_string) for numeric_string in testListString]
        for testnum in testList:
            if i==testnum:
                testCalled = True
            
    else:
        testCalled = True
    return testCalled

def runConfig( status, config):
    i = 0
    tests = config['tests']
    for t in tests:
        
        if isTestCalled(i):
            type = t['type']
            url = 'https://%s/%s' % (config['host'],t['path'])
            file = t['file']
            passme = t['pass']
            validate = t['check']

            if type=='file':
                with open(file,'r') as package:
                    myinput=''
                    #if( status==200) and ('wait' in t):
                    #    time.sleep( t['wait'] )

                    r = requests.post( url, 
                                        cookies=cookies,
                                        files={'file':package}, verify=False )
                    result = xml.dom.minidom.parseString( r.text )
                    status = r.status_code
                    if (status==200):
                        print  'Script Succeeded - Step '+str(i)

            elif type=='xml':
                with open( file, 'r' ) as payload:
                    myinput=''
                    #if( status==200) and ('wait' in t):
                    #    time.sleep( t['wait'] )

                    data = payload.read()

                    url = 'https://%s/api/node/mo/.xml' % config['host']
                    r = requests.post( url, cookies=cookies, data=data, verify=False )
                    result = xml.dom.minidom.parseString( r.text )
                    status = r.status_code
                    if (status==200):
                        print  'Script Succeeded - Step '+str(i)

            else:
                print 'Unknown type:', type
        i=i+1

        #sleep for 50 ms between tests
        time.sleep(0.05);

def TestsToRun (tests):
    testList = tests.split(",")

runConfig( status, config )
print 'The End'