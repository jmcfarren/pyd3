#!/usr/bin/python
# -*- coding: utf-8 -*-

import discogs_client

def main():
	user_agent = 'pyd3/0.1'
	user_token = 'XXXXX'
	d = discogs_client.Client(user_agent, user_token=user_token)
	query = 'Amygdala (Roman Flugel Remix)'
	qtype = 'release'
	results = d.search(query, type=qtype)
	release = results[0]
	label = release.labels[0]
	artist = release.artists[0]
	catno = release.data['labels'][0]['catno']
	print('Search: {!r} as {}'.format(query, qtype))
	print('Release: {}'.format(release.title))
	print('Artist:  {}'.format(artist.name))
	print('Label:   {}'.format(label.name))
	print('Cat#:    {}'.format(catno))
	#print(dir(label))


if __name__ == "__main__":
    main()