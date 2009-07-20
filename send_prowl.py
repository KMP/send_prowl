"""
Send iPhone Push Notification using Prowl (Zachary West) and Prowlpy (Jacob Burch).

send_prowl.py V2

Written by KMP, 7/9/2009

Wrapper around the prowlpy (http://github.com/jacobb/prowlpy/tree/master)
Python module for posting to the iPhone Push Notification service Prowl (http://prowl.weks.net/)

send_prowl.py sets up and sends the actual notification
using an external configuration file for the values. 

"""
import ConfigParser
import prowlpy
import sys

def main(cfgfile):
    
    #-----------------------
    # Default Configuration
    
    default_values = {
    'apikey' : 'NOT SET',
    'app' : 'Generic App',
    'event' : 'Generic Event',
    'desc' : 'Generic Description',
    'debug': 'false'}
    
    #------------------------
    
    config = ConfigParser.ConfigParser(default_values)
    config.read(cfgfile)
    
    apikey = config.get('DEFAULT', 'apikey')
    app = config.get('DEFAULT', 'app')
    event = config.get('DEFAULT', 'event')
    desc = config.get('DEFAULT', 'desc')
    debug = config.get('DEFAULT', 'debug')
    
    
    if debug == "true":
        print "---------------------------"
        print "Configuration Settings:\n"
        for key, value in config._defaults.iteritems():
            print key + " = " + value 
        print "---------------------------"
    

    # Send Notification
    if apikey != "NOT SET":
        p = prowlpy.Prowl(apikey)
        try:
            p.post(app,event,desc)
            if debug == "true":
                print 'Success'
        except Exception,msg:
            print msg
    else:
        print '''
API key is needed!
                
Create a file named send_prowl.cfg in the 
same location you are running send_prowl from.

OR

Optionally, you may specify a path to the 
configuration file as an argument:
Example:
    send_prowl c:\path\\to\config.cfg

The contents of this file should be as follows:

    #----------------------
    [DEFAULT]
    apikey: YOUR_API_KEY_HERE #This is required
    app: APP Name
    event: Event Name
    desc: Event Description
    debug: true|false
    #----------------------
'''
        
        
if __name__ == '__main__':
    if sys.argv[1:]:
        cfgfile = sys.argv[1:]
    else:
        cfgfile = "send_prowl.cfg"
    main(cfgfile)