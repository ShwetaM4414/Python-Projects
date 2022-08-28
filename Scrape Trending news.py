# import libraries
import pandas as pd
from pygooglenews import GoogleNews

news = GoogleNews()
print("Menu : \n 1.Top News \n 2.News by topic \n 3.Geolocation Specific News \n 4.News by a Query Search "
      "\n")

# taking input from the user
st1 = input("Enter the choice : ")

# Checks for the wrong input
while not st1.isnumeric():
    print("Wrong Input, Try again\n")
    st1 = input("Enter the choice : ")

# Converts string into the integer
st = int(st1)

stories = []


if st == 1:
    # top_news() method gives the top news
    top = news.top_news()
    newsitem = top['entries']

    # iterating over a list
    for item in newsitem:
        story = {
            'Title': item.title,
            'Link': item.link
        }
        stories.append(story)

elif st == 2:
    print("Accepted topics are World,Nation,Business,Technology,Entertainment,Science,Sports,Health\n")
    # Check data validation
    try:
        tp = input("Enter the topic : ")

        # topic_headlines() method gives news on the given topic
        Topic = news.topic_headlines(tp)
        newsitem = Topic['entries']

        # iterating over a list
        for item in newsitem:
            story = {
                'Title': item.title,
                'Link': item.link
            }
            stories.append(story)
    except Exception:
        print("Wrong Input")

elif st == 3:
    location = input("Enter the location : ")

    # geo_headlines() method gives news on the given location
    loc = news.geo_headlines(location)
    newsitem = loc['entries']

    # iterating over a list
    for item in newsitem:
        story = {
            'Title': item.title,
            'Link': item.link
        }
        stories.append(story)

elif st == 4:
    article = input("Enter the word to get the best matching articles : ")
    Time = input("Enter the time range for the published datetime. In format of (3h or 8m or 23d) : ")

    # search() method gives news on the given query
    search = news.search(article, when=Time)

    # iterating over a list
    newsitem = search['entries']
    for item in newsitem:
        story = {
            'Title': item.title,
            'Link': item.link
        }
        stories.append(story)

else:
    print("Wrong Input")

# load data into a DataFrame object
df = pd.DataFrame(stories)

# saves data to the csv file
df.to_csv(r'G:\News.csv', index=False)

