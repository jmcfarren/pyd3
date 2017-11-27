#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import getopt
import discogs_client

NAME = 'pyd3'
VERSION = '0.1'
URL = 'https://github.com/joshuamcfarren/pyd3.git'

def main(argv):
	try:
		opts, args = getopt.getopt(argv,"r:",["release="])
	except getopt.GetoptError:
		print('{} -r <release>'.format(sys.argv[0]))
		sys.exit(2)
	user_agent = '{}/{} +{}'.format(NAME, VERSION, URL)
	user_token = os.environ.get('DISCOGS_USER_TOKEN')
	discogs = discogs_client.Client(user_agent, user_token=user_token)
	for opt, arg in opts:
		if opt in ("-r", "--release"):
			query = arg
			#query = 'Amygdala (Roman Flugel Remix)'
			qtype = 'release'
			results = discogs.search(query, type=qtype)
			release = results[0]
			label = release.labels[0]
			artist = release.artists[0]
			catno = release.data['labels'][0]['catno']
			#print('Request: {} {} {} {!r}'.format(user_agent, user_token, qtype, query))
			print('Release: {}'.format(release.title))
			print('Artist:  {}'.format(artist.name))
			print('Label:   {}'.format(label.name))
			print('Cat#:    {}'.format(catno))
			#print(dir(label))


if __name__ == "__main__":
    main(sys.argv[1:])