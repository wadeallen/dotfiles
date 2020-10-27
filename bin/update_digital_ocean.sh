#!/bin/bash

# Digital Ocean variables
domain="wadeallen.me"
record_id="66831085"  # Get this value from the view_do_dns.sh script output
api_key="c2cb52d284747408984ef77366643015dbfff513251cbc36d5cc83c0877a69a1"
# -----------------------
echo "Checking IP for change on: $(date)"
curip=$(cat /tmp/ip.txt)
ip=$(/usr/bin/curl -ks ipecho.net/plain)
echo "Got IP: ($ip) from wtfismyip.com.  Existing IP is: ($curip)"
# if IP is different
if [ "$ip" != "$curip" ]; then
        # put our new IP into a file to compare against next run
        echo $ip > /tmp/ip.txt
        echo "Updating Digital Ocean."
        /usr/bin/curl -ks -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer $api_key" -d "{\"data\":\"$ip\"}" "https://api.digitalocean.com/v2/domains/$domain/records/$record_id"
        #echo '/usr/bin/curl -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer $api_key" -d "{\"data\":\"$curip\"}" "https://api.digitalocean.com/v2/domains/$domain/records/$record_id"'
        echo "Done."
else
        echo "IP hasn't changed.  Not updating."
fi
