#!/bin/bash

# Digital Ocean variables

domain="wadeallen.me"
api_key="c2cb52d284747408984ef77366643015dbfff513251cbc36d5cc83c0877a69a1"

$(which curl) -ks -X GET -H "Content-Type: application/json" -H "Authorization: Bearer ${api_key}" "https://api.digitalocean.com/v2/domains/${domain}/records" | jq -r '.domain_records[] | "\(.id) \(.name) \(.type) \(.data)"' | column -t
