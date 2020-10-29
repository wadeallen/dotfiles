#!/bin/bash

source ~/bin/config.sh

# Digital Ocean variables

domain="wadeallen.me"
api_key=$doapi

$(which curl) -ks -X GET -H "Content-Type: application/json" -H "Authorization: Bearer ${api_key}" "https://api.digitalocean.com/v2/domains/${domain}/records" | jq -r '.domain_records[] | "\(.id) \(.name) \(.type) \(.data)"' | column -t
