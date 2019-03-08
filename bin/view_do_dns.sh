#!/bin/bash

# your domain ID
domain_name="wadeallen.me"

# subdomain
subdomain="church"

# record to update
record_id="66831085"

#your api key
api_key="714fdd2f86948d786a3dc670bf6f6ddcbb2bf16df0011cb3dcb622eb3753fdfb"

current_date_time="`date '+%Y-%m-%d %H:%M:%S'`";

ip="$(curl  http://ipecho.net/plain)"

if [ -f "ip" ] && [ "$ip" == "$(cat ip)" ] ;then
    result=$current_date_time" match"
else
    echo content="$(curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer $api_key" -d '{"name": "'"$subdomain"'", "data": "'"$ip"'"}' "https://api.digitalocean.com/v2/domains/$domain_name/records/$record_id")"
    result=$current_date_time" mismatch"
fi

echo "$result" >> log
