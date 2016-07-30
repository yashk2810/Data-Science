## 2. Authenticating with the API ##

headers = {"Authorization": "bearer 13426216-4U1ckno9J5AiK72VRbpEeBaMSKk", "User-Agent": "Dataquest/1.0"}
param = {'t': "day"}
response = requests.get('https://oauth.reddit.com/r/python/top', params=param, headers=headers)
python_top = response.json()
print(python_top)


## 3. Getting the most upvoted article ##

python_top_articles = python_top["data"]["children"]
most_upvoted = ""
most_upvotes = 0
for article in python_top_articles:
    ar = article["data"]
    if ar["ups"] >= most_upvotes:
        most_upvoted = ar["id"]
        most_upvotes = ar["ups"]

## 4. Getting article comments ##

response = requests.get('https://oauth.reddit.com/r/python/comments/4b7w9u', headers=headers)
comments = response.json()

## 5. Getting the most upvoted comment ##

comments_list = comments[1]["data"]["children"]
most_upvoted_comment = ""
most_upvotes_comment = 0
for comment in comments_list:
    co = comment["data"]
    if co["ups"] >= most_upvotes_comment:
        most_upvoted_comment = co["id"]
        most_upvotes_comment = co["ups"]

print(most_upvoted_comment)

## 6. Upvoting a comment ##

params = {'dir': 1, 'id': 'd16y4ry'}
r = requests.post('https://oauth.reddit.com/api/vote', headers=headers, json=params)
status = r.status_code