import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["urlshortener_db"]

urls = db["urls"]

def addURL(host, o_link, urlcode):
	new_url = {
		"original_url": o_link,
		"shortened_url": f"{host}{urlcode}",
		"urlcode": urlcode
	}
	urls.insert_one(new_url)
	return urls.find_one({"urlcode": urlcode})['shortened_url']

def deleteRecords():
	[urls.delete_one(x) for x in urls.find()]

def getURL(surl):
	obj = urls.find_one({"urlcode": surl})
	return obj['original_url'] if (obj) else None