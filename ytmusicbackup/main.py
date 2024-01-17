#!/usr/bin/env python3

import json
import os
import sys

from ytmusicapi import YTMusic

if not os.path.exists("oauth.json"):
    print("No `oauth.json` file found.")
    print("Please run: `pymusicapi oauth` and follow instructions.")
    sys.exit(1)


ytmusic = YTMusic("oauth.json")

albums = ytmusic.get_library_albums(limit=20000, order="recently_added")

print(json.dumps(albums))
