import re

txt ="The rain in Spain"

a = re.search(r"\bS\w+", txt)
print(type(a),a)