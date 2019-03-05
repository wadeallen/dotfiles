#!/bin/bash

TOKEN="KN1ZQ4OWvleMqGGEs5Sl0oESdoutAX6o"  # The API v2 OAuth token
ACCOUNT_ID="22667"        # Replace with your account ID
ZONE_ID="wadeallen.me"  # The zone ID is the name of the zone (or domain)
RECORD_ID="7765630"       # Replace with the Record ID
IP=`curl -s http://ipv4.icanhazip.com/`

curl -H "Authorization: Bearer $TOKEN" \
     -H "Content-Type: application/json" \
     -H "Accept: application/json" \
     -X "PATCH" \
     -i "https://api.dnsimple.com/v2/$ACCOUNT_ID/zones/$ZONE_ID/records/$RECORD_ID" \
     -d "{\"content\":\"$IP\"}"
