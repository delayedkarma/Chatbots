from __future__ import absolute_import
from __future__ import division
from __future__ import unicode_literals

from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

class ActionTopTracks(Action):
	def name(self):
		return 'action_top_tracks'
		
	def run(self, dispatcher, tracker, domain):
       		
		client_id = '' #Add client_id here
		client_secret = '' #Add client_secret here

		dict = {'Bob Dylan': 'spotify:artist:74ASZWbe4lXaubB36ztrGX', 'Led Zeppelin': 'spotify:artist:36QJpDe2go2KgaRleHCDTp', \
			'The Beatles': 'spotify:artist:3WrFJ7ztbogyGnTHbHJFl2', 'The Doors': 'spotify:artist:22WZ7M8sxp5THdruNY3gXt', \
				'The Rolling Stones': 'spotify:artist:22bE4uQ6baNwSHPVcDxLCe', 'bob dylan': 'spotify:artist:74ASZWbe4lXaubB36ztrGX', \
				'led zeppelin': 'spotify:artist:36QJpDe2go2KgaRleHCDTp', 'the beatles': 'spotify:artist:3WrFJ7ztbogyGnTHbHJFl2', \
				'the doors': 'spotify:artist:22WZ7M8sxp5THdruNY3gXt', 'the rolling stones': 'spotify:artist:22bE4uQ6baNwSHPVcDxLCe'}

		artist_name = tracker.get_slot('artist')
		artist_uri = dict[artist_name]
		
		client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
		sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

		results = sp.artist_top_tracks(artist_uri)
		
		response_lst=[]

		for track in results['tracks'][:5]:
			response_lst.append(track['name'])

		response = """The top tracks for {} are {}""".format(artist_name,response_lst)

		dispatcher.utter_message(response)
		
		return [SlotSet('artist',artist_name)]

