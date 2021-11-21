import requests


def handler(event, context):
    if ('queryStringParameters' in event):
        r = requests.get('https://cloudflare-dns.com/dns-query',
                         params={
                             "name": event['queryStringParameters']['d'],
                             "type": event['queryStringParameters']['t']
                         },
                         headers={"accept": "application/dns-json"})
        return r.json()
    else:
        return 'Please pass domain and type'