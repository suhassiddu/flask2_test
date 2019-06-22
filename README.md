# Flask Rest Api Test

Hosted on [https://suhasflask.herokuapp.com/](https://suhasflask.herokuapp.com/)

# Check with Curl
```
$ curl https://suhasflask.herokuapp.com/ifsc/<string:ifsc_code>

Example:

http post http://127.0.0.1:8000/api/token/ username=visitor password=123
HTTP/1.1 200 OK
Allow: POST, OPTIONS
Content-Length: 438
Content-Type: application/json
Date: Sat, 22 Jun 2019 09:49:00 GMT
Server: WSGIServer/0.2 CPython/3.6.8
Vary: Accept
X-Frame-Options: SAMEORIGIN

{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTU2MTI4Mzc1MywianRpIjoiOWM2OTg4OWIwNmNjNDc0YjlkN2YzYzRmZTE5MjgyODUiLCJ1c2VyX2lkIjoxfQ.sam5mXrfyzoZr4O98QlBiZoO2S6dnQkXMiapGacggGw",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYxMTk3NjUzLCJqdGkiOiI0NzU1NTM3NjQxNGM0M2E0OTAzOTY2M2QxNTc4NzZjMSIsInVzZXJfaWQiOjF9.WFda72NnegYJzrag-ExJQP5QlrWcaOVkNlZgddQ3hic"
}

$ curl --location --request GET "localhost:8000/ifsc/abhy0065004" \
>   --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYxMTk3NjUzLCJqdGkiOiI0NzU1NTM3NjQxNGM0M2E0OTAzOTY2M2QxNTc4NzZjMSIsInVzZXJfaWQiOjF9.WFda72NnegYJzrag-ExJQP5QlrWcaOVkNlZgddQ3hic" | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100   181  100   181    0     0     18      0  0:00:10  0:00:10 --:--:--    47
{
  "ifsc": "ABHY0065004",
  "branch": "BHANDUP",
  "address": "CHETNA APARTMENTS, J.M.ROAD, BHANDUP, MUMBAI-400078",
  "city": "MUMBAI",
  "district": "GREATER MUMBAI",
  "state": "MAHARASHTRA",
  "bank": 60
}

$ curl --location --request GET "localhost:8000/branchlist/?bank=hdfc+bank&branch=mumbai"   --header "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTYxMTk3NjUzLCJqdGkiOiI0NzU1NTM3NjQxNGM0M2E0OTAzOTY2M2QxNTc4NzZjMSIsInVzZXJfaWQiOjF9.WFda72NnegYJzrag-ExJQP5QlrWcaOVkNlZgddQ3hic" | jq
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100  2374  100  2374    0     0    114      0  0:00:20  0:00:20 --:--:--   524
{
  "count": 193,
  "next": "http://localhost:8000/branchlist/?bank=hdfc+bank&branch=mumbai&limit=10&offset=10",
  "previous": null,
  "results": [
    {
      "ifsc": "HDFC0000001",
      "branch": "TULSIANI CHMBRS - NARIMAN PT",
      "address": "101-104 TULSIANI CHAMBERSFREE PRESS JOURNAL MARGNARIMAN POINTMUMBAIMAHARASHTRA400 021",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000002",
      "branch": "MUMBAI - KHAR (WEST)",
      "address": "SWAGATAM,OPP. KHAR POLICE STATION,S.V.ROAD, KHAR (WEST)MUMBAIMAHARASHTRA400 052",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000005",
      "branch": "MUMBAI - BHULABHAI DESAI ROAD",
      "address": "TIRUPATI APARTMENTS,SHOP NO. 4,BHULABHAI DESAI ROAD,MUMBAIMAHARASHTRA400 026",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000012",
      "branch": "MUMBAI - PRABHADEVI",
      "address": "EL-DORADONARAYAN DHURU MARGOPP. VEER SAVARKAR MARG,PRABHADEVIMUMBAIMAHARASHTRA400 025",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000013",
      "branch": "MUMBAI - CHEMBUR",
      "address": "ANCHORAGE  BUILDING170/171 CENTRAL  AVENUECHEMBURMUMBAIMAHARASHTRA400 071",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000015",
      "branch": "MULUND WEST- SHANKARDHAN PLAZA",
      "address": "RATAN GALAXIE, JUNCTION OF J. N. ROAD AND GOSHALA ROAD, MULUND WEST  MUMBAI MAHARASHTRA 400 080",
      "city": "MUMBAI",
      "district": "GREATER BOMBAY",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000016",
      "branch": "MUMBAI - PALI HILL - BANDRA",
      "address": "LANDMARK BUILDINGPALI NAKA,PALI HILL,BANDRA -WESTMUMBAIMAHARASHTRA400 050",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000019",
      "branch": "MUMBAI - VERSOVA",
      "address": "THE AMALTAS CO-OP HSG.SOC.LTDJUHU-VERSOVA LINK ROADWARD-K (WEST)  ANDHERIWESTMUMBAI-400049",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000038",
      "branch": "MUMBAI - VASAI (EAST)",
      "address": "POOJA TOWERS, GR FLOOREVERSHINE CITYVASAI (E),THANEMAHARASHTRA",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    },
    {
      "ifsc": "HDFC0000047",
      "branch": "MUMBAI - MALAD (WEST)",
      "address": "ARBOUR , 180-A,MARVE ROAD,ORLEM,MALAD - WESTMUMBAIMAHARASHTRA400064",
      "city": "MUMBAI",
      "district": "GREATER MUMBAI",
      "state": "MAHARASHTRA",
      "bank": 5
    }
  ]
}
```

