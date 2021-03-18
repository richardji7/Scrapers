import requests
import os
import json
import urllib


cur_dir = os.getcwd()
save_dir = cur_dir + "/USA/GA/Norcross"

if not os.path.exists(save_dir):
	os.makedirs(save_dir)

def verify_data(in_pdf, num):
	if in_pdf.status_code != 404 or str(in_pdf).find("<Error>") == False: # Verifies that file exists
		file_name = get_name(num) # Gets the filename from 
		save_path = os.path.join(save_dir, file_name)
		

def scrape_urls():
	with open("response.json", "r") as json_file:
		response = json.load(json_file)
		r_data = response['data']
		total = response['total']
		base_url = 'https://www.norcrossga.net'
		for p in range(total):
			doc_url = r_data[p]['URL']
			output_url = base_url + doc_url
		
			with open('urls.txt','a') as output:
				output.write(output_url + '\n')
	output.close()

def get_name(line):
	with open("response.json", "r") as json_file:
		response = json.load(json_file)
		r_data = response['data']
		#total = response['total']
		
		doc_name = r_data[line]['DisplayName']
		return doc_name
		

def download_data():
	with open('urls.txt', 'r') as in_url:
		for num, line in enumerate(in_url):
			
			pdf = urllib.request.urlopen(line) # Gets the pdf
			file_name = get_name(num)
			print("Getting " + file_name)
			with open(save_dir + file_name + '.pdf', 'wb') as file:
				file.write(pdf.read())
				file.close()

download_data()
