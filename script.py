import requests

addr='https://cdn.hackerrank.com/hackerrank/static/contests/capture-the-flag/secret/secret_json/'
f = open('keys.txt', 'r')
out = open('phrases.txt', 'w')
inp = f.read()
keys = inp.strip().split('": "",\n  "')
keys[len(keys)-1] = keys[len(keys)-1][:5]
keys[0] = keys[0][1:]

phrases = []
for key in keys:
    r = requests.get(addr+key+'.json')
    phrases.append(r.json()['news_title'])

phrases.sort()
for phrase in phrases:
    out.write(phrase+'\n')
