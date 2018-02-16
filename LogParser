#!/usr/bin/python

#This script sort user agent and shows the IP's related with it
# we need  to import defaultdict from collections library 'cause we're gonna need it to create a list on a dictionary
# the script could be improved adding more arguments like fields to use as keys and items
# Dependencies pip install pyyaml ua-parser user-agents
# filter([char_to_filter], [list_to_filter]) is used to clean quotes and blank spaces

import sys
from  collections import defaultdict
from user_agents import parse

def main():
    r = []
    i = defaultdict(list)
    f = open(sys.argv[1],"r")
    for line in f.readlines():
        r = line.strip("\"")
        ip = r.split(" ")[0]
        ua = parse(filter(None, line.split("\""))[5])
#        print ua.browser[0] #for debug
#        print "la ip:" + ip # for debugging prupose
#        raw_input() # for debug
        if i.has_key(ua.browser[0]):
            i[ua.browser[0]].append(ip)
        else:
            i[ua.browser[0]] = []
            i[ua.browser[0]].append(ip)

    f.close()
    for key in i.keys():
        print key + ":\n" + str(i[key])[1:-1]


if __name__ == '__main__':
    main()
