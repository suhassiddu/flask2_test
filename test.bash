#!/bin/bash

IFSC="abhy0065004"
BANK="hdfc+bank"
BRANCH="mumbai"
LIMIT=10
OFFSET=10

TOKEN=$(curl -d "username=visitor&password=123" -X POST https://suhasfyle.herokuapp.com/api/token/ | python -c "import sys,json; print json.load(sys.stdin)['access']")

curl --location --request GET "https://suhasfyle.herokuapp.com/ifsc/$IFSC" --header "Authorization: Bearer $TOKEN" | jq

curl --location --request GET "https://suhasfyle.herokuapp.com/branchlist/?bank=$BANK&branch=$BRANCH&limit=$LIMIT&offset=$OFFSET" --header "Authorization: Bearer $TOKEN" | jq
