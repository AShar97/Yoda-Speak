import urllib2, urllib

# goto: https://www.mashape.com
# you need to create a Mashape account insert your key
# if you do not do this the script will fail
mashapeAuthorization = "eUXi62gJ1lmshCYLXQ1KHj5gLuKlp1uHCecjsnoAwkYR0lv9XW"

def getSpeech(sentence):
	str = urllib.quote(sentence)
	opener = urllib2.build_opener()
	opener.addheaders = [("X-Mashape-Authorization", mashapeAuthorization)]
	socket = opener.open('https://yoda.p.mashape.com/yoda?sentence=' +
		str)
	content = socket.read()
	socket.close()
	print "Yoda says: " + content

def main() :
	sentence=(raw_input("Ask me anything Young Padawan: "))
	if len(sentence) is 0:
   		print "Please ask something"
   	getSpeech(sentence)

if __name__ == '__main__':
	main()