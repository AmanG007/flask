import json
import urllib.request #urllib2
import urllib
from flask import render_template
import feedparser
from flask import Flask
from flask import request


app = Flask(__name__,template_folder='templates')

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
			'cnn': 'http://rss.cnn.com/rss/edition.rss',
			'fox': 'http://feeds.foxnews.com/foxnews/latest',
			'iol': 'http://www.iol.co.za/cmlink.1.640'}
			


@app.route("/")
def get_news():
		query = request.args.get("publication")
		if not query or query.lower() not in RSS_FEEDS:
				publication = "bbc"			#DEFAULTS["publication"]
		else:
				publication = query.lower()
		feed = feedparser.parse(RSS_FEEDS[publication])
		weather = get_weather("London,UK")
		#return feed['entries']
		return render_template("home.html",articles=feed["entries"],weather=weather)
   
def get_weather(query):
	api_url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=227951c19c48f75747536a2878810dbd'
	query = urllib.quote(query)
	url = api_url.format(query)
	data = urllib2.urlopen(url).read()
	parsed = json.loads(data)
	weather = None
	if parsed.get("weather"):
		weather = {"description": parsed["weather"][0]
		["description"],"temperature":parsed["main"]
		["temp"],"city":parsed["name"]
		}
	return weather
	

if __name__ == "__main__":
 app.run(port=5000, debug=True)


                                  
								  
								  
								  
								  
								  
								  
								  
								  
								  
