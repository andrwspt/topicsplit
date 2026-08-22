import json, base64, urllib.request, os

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN', '')
REPO = 'andrwspt/topicsplit'

# Read fixed embed.html
with open('C:/Users/evana/Documents/ai-workspace/topicsplit-repo/embed.html', 'rb') as f:
    embed_content = base64.b64encode(f.read()).decode()

# Read fixed badge.html
with open('C:/Users/evana/Documents/ai-workspace/topicsplit-repo/badge.html', 'rb') as f:
    badge_content = base64.b64encode(f.read()).decode()

# Update embed.html
data = json.dumps({
    'message': 'Fix broken CSS in embed.html and badge.html',
    'content': embed_content,
    'sha': '48187c3b160242bd4770561b85dc90b2a611b63f'
}).encode()

req = urllib.request.Request(
    f'https://api.github.com/repos/{REPO}/contents/embed.html',
    data=data,
    method='PUT',
    headers={
        'Authorization': f'token {GITHUB_TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v3+json'
    }
)
try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f'embed.html updated: {result["content"]["sha"]}')
except urllib.error.HTTPError as e:
    print(f'embed.html failed: {e.code} {e.read().decode()}')

# Update badge.html
data = json.dumps({
    'message': 'Fix broken CSS in embed.html and badge.html',
    'content': badge_content,
    'sha': '737fcd797d11178421a90a9f3183a216f990ca95'
}).encode()

req = urllib.request.Request(
    f'https://api.github.com/repos/{REPO}/contents/badge.html',
    data=data,
    method='PUT',
    headers={
        'Authorization': f'token {GITHUB_TOKEN}',
        'Content-Type': 'application/json',
        'Accept': 'application/vnd.github.v3+json'
    }
)
try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f'badge.html updated: {result["content"]["sha"]}')
except urllib.error.HTTPError as e:
    print(f'badge.html failed: {e.code} {e.read().decode()}')
