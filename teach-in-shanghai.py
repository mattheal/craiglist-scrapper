import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

#scrape the this website and save it to a file
shanghai_url = "https://shanghai.craigslist.com.cn/search/edu?lang=en&cc=us&employment_type=1"
my_client = uReq(shanghai_url)
shanghai_html = my_client.read()
my_client.close()

#saves the scraped content into a variable
page_soup = soup(shanghai_html, "html.parser")
print(page_soup.h1)

#print(page_soup)

#The following commented out command will print everything on the page except the css
#print(page_soup.body.span)
#this filters out for all products



#search = page_soup.findAll("div", {"class":"item-container"})
#len(search)
#job1 = search[0]

#This for loop will parse the results using specific search criteria.

print("-"*50)
print("incoming text file press enter to continue")
input()
print("-"*50)

search = page_soup.findAll("li", {"class":"result-row"})
#print(search)

all_jobs = []

for job in search:
	job_desc = job.findAll("a", {"class":"result-title hdrlnk"})
	job_title = job_desc[0].text.strip()
	all_jobs.append(job_title)

all_jobs = set(all_jobs)
search_length = len(all_jobs)
print("I found ",search_length," teaching jobs on craigslist, press enter to continue")
input()
print("Type 'center' to view only those jobs that are not at centers else press enter: ")
center_option = input().lower()


def __init__(all_jobs):
	for elements in all_jobs:
		print("-"*100)
		print(elements)
		print("-"*100)
#	print("The End of an Iteration!")
#	print("-"*50)
		print()


def Center_filter(all_jobs):
	new_list=[]
	for elements in all_jobs:
		new_element = elements.lower()
		if "center" not in new_element:
			new_list.append(new_element)
		else:
			continue
	print("There are now ",len(all_jobs)," jobs in the list, press any key to continue")
	input()
	__init__(new_list)		


if center_option.startswith("c"):
	Center_filter(all_jobs)
else:
	__init__(all_jobs)
"""
for card in search:
	brand = card.div.div.a.img["title"]

	full_name = card.findAll("a",{"class":"item-title"})
	product_name = full_name[0].text

	price_class = card.findAll("li", {"class":"price-note"})
	final_price = price_class[0].text.strip()

	print(brand)
	print(product_name)
	print(final_price)

"""
