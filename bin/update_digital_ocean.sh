#!/bin/bash

current_date_time="`date '+%Y-%m-%d %H:%M:%S'`";

# Digital Ocean variables
domain="wadeallen.me"
record_id="66831085"  # Get this value from the view_do_dns.sh script output
api_key="714fdd2f86948d786a3dc670bf6f6ddcbb2bf16df0011cb3dcb622eb3753fdfb"
# -----------------------
# echo "Checking IP for change on: $(date)"
curip=$(cat /tmp/ip.txt)
ip=$(curl https://ipinfo.io/ip)
# echo "Got IP: ($ip).  Existing IP is: ($curip)"
# if IP is different
if [ "$ip" != "$curip" ]; then
        # put our new IP into a file to compare against next run
        echo $ip > /tmp/ip.txt
        echo "Updating Digital Ocean."
        /usr/bin/curl -ks -X PUT -H "Content-Type: application/json" -H "Authorization: Bearer $api_key" -d "{\"data\":\"$ip\"}" "https://api.digitalocean.com/v2/domains/$domain/records/$record_id"
        message="Updated IP to $ip"
else
        message="IP hasn't changed"
fi

echo "Checked IP on: $current_date_time    $message" >> /home/wadeallen/update_ip.log
