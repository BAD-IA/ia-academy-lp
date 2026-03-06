import urllib.request, json, base64, os
TOKEN = os.environ.get('GITHUB_TOKEN', '')
REPO  = 'BAD-IA/store-lp'
PATH  = 'index.html'

# 1. Get current file SHA
req = urllib.request.Request(
    f'https://api.github.com/repos/{REPO}/contents/{PATH}',
    headers={'Authorization': f'token {TOKEN}', 'User-Agent': 'claude-code'}
)
with urllib.request.urlopen(req) as r:
    info = json.loads(r.read())
sha = info['sha']
print('SHA atual:', sha)

# 2. Read updated file
with open('store-lp/index.html', 'r', encoding='utf-8') as f:
    content = f.read()
encoded = base64.b64encode(content.encode('utf-8')).decode('ascii')

# 3. Push update
payload = json.dumps({
    'message': 'fix: atualiza links Coinzz, precos reais e hero com background',
    'content': encoded,
    'sha': sha
}).encode('utf-8')

req2 = urllib.request.Request(
    f'https://api.github.com/repos/{REPO}/contents/{PATH}',
    data=payload,
    method='PUT',
    headers={
        'Authorization': f'token {TOKEN}',
        'Content-Type': 'application/json',
        'User-Agent': 'claude-code'
    }
)
with urllib.request.urlopen(req2) as r:
    result = json.loads(r.read())

print('Commit:', result['commit']['sha'])
print('URL:', result['content']['html_url'])
print('Publicado com sucesso!')
