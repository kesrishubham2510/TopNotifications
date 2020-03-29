import time
import win10toast
from XmlExtractor import headlines


toaster= win10toast.ToastNotifier()
# fetch news items

newsitems = headlines()

for newsitem in newsitems:
    headline= str(newsitem['title'])
    for head in headline.split('\n'):
        head = head.replace('b', '')
        toaster.show_toast("Latest News", head.replace("'", ''), icon_path='notification (1).ico', duration=3)#3 seconds
        time.sleep(100)#100 seconds


