import mechanize
import cookielib
from bs4 import BeautifulSoup
import re
import io
import sys;
reload(sys);
sys.setdefaultencoding("utf8")

f=open('/Users/robinmalhotra2/Desktop/newfile 2.txt','w')
# Browser
br = mechanize.Browser()

# Cookie Jar
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)

# Browser options
br.set_handle_equiv(True)
br.set_handle_gzip(True)
br.set_handle_redirect(True)
br.set_handle_referer(True)
br.set_handle_robots(False)

# Follows refresh 0 but not hangs on refresh > 0
br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

# Want debugging messages?
#br.set_debug_http(True)
#br.set_debug_redirects(True)
#br.set_debug_responses(True)

# Open some site, let's pick a random one, the first that pops in mind:

for x in xrange(9106892,9199999):
	
	r = br.open('http://cbseresults.nic.in/class12/cbse122014_total.htm')
	html = r.read()

	br.select_form(nr=0)

	br.form['regno']=str(x)
	br.submit()

	html=br.response().read();
	parsed_html = BeautifulSoup(html,'html.parser')


	lis=parsed_html.find_all('table')
	rows=lis[4].find_all('tr')
	for row in rows:
	    data = row.find_all("td")
	    if len(data)>1:
	    	names= data[1].text
	    	namesList=names.split('\n')
	    	f.write(namesList[0]+"\n")

	
	table = parsed_html.find('table', border=1)
	rows = table.find_all('tr')

	for row in rows:
	    data = row.find_all("td")
	    if len(data)>2:
		    
		    rn = data[0].get_text()
		    sr = data[1].get_text()
		    d = data[2].get_text()
		    n = data[3].get_text()
		    rn.decode('utf-8','ignore')
		    sr.decode('utf-8','ignore')
		    d.decode('utf-8','ignore')
		    n.decode('utf-8','ignore')
		    f.write(rn + "," + sr+"," +d+"\n")
	f.write("\n"+"\n"+"\n"+"\n"+"\n")	

