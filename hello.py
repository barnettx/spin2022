#!/usr/bin/env python3
import pygit2

print("""<html>
<body>
<p>Hello, Roland!<p/>""")

print("""
<p>Git log is:
<pre>
""")

last = repo[repo.head.target]
for commit in repo.walk(last.id, pygit2.GIT_SORT_TIME):
    print(commit.message)
    
print("""
</pre>
</p>
""")

print("""
</body>
</html>""")
