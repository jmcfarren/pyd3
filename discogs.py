#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import getopt
import discogs_client
from pprint import pprint

NAME = 'pyd3'
VERSION = '0.1'
URL = 'https://github.com/jmcfarren/pyd3.git'
RELEASE_BASE_URL = 'https://www.discogs.com/release/'

def main(argv):
    try:
        opts, args = getopt.getopt(argv,'r:m:',['release=','master='])
    except getopt.GetoptError:
        usage()
    for opt, arg in opts:
        if not arg:
            usage()
        else:
            if opt in ('-r', '--release'):
                qtype = 'release'
            elif opt in ('-m', '--master'):
                qtype = 'master'
            else:
                usage()
            query = arg
            user_agent = '{}/{} +{}'.format(NAME, VERSION, URL)
            user_token = os.environ.get('DISCOGS_USER_TOKEN')
            discogs = discogs_client.Client(user_agent=user_agent, user_token=user_token)
            results = discogs.search(query, type=qtype)
            if not results:
                print('No results for {} search: {}'.format(qtype, query))
            else:
                if qtype == 'master':
                    release = results[0].main_release
                    label = release.labels[0]
                    artist = release.artists[0]
                    catno = release.data['labels'][0]['catno']
                    year = release.data['released']
                elif qtype == 'release':
                    release = results[0]
                    label = release.labels[0]
                    artist = release.artists[0]
                    catno = release.data['labels'][0]['catno']
                    year = release.data['released']
                print('Release: {}'.format(release.title))
                print('Artist:  {}'.format(artist.name))
                print('Label:   {}'.format(label.name))
                print('Cat#:    {}'.format(catno))
                print('Year:    {}'.format(release.year))
                print('Discogs: {}{}'.format(RELEASE_BASE_URL, release.id))


def usage():
    print('Usage:')
    print("    {} -release 'search phrase'".format(sys.argv[0]))
    print("    {} -master 'search phrase'".format(sys.argv[0]))
    sys.exit(2)


if __name__ == '__main__':
    main(sys.argv[1:])