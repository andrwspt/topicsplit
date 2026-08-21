path = r'C:\Users\evana\Documents\ai-workspace\topicsplit-repo\index.html'
with open(path, 'w') as f:
    f.write('<!-- test -->\n')
print('OK', os.path.exists(path))