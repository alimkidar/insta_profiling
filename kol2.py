print ("Memulai")
from collections import Counter
import pandas as pd
import requests
import json
import re


#Untuk ambil jumlah followers dan following di instagram
def insta(user_name):
	headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
	ff = []
	situs = 'https://www.instagram.com/' + user_name + '/'
	response = requests.get(url=situs, headers=headers)
	json_match = re.search(r'window\._sharedData = (.*);</script>', response.text)
	profile_json = json.loads(json_match.group(1))['entry_data']['ProfilePage'][0]['graphql']['user']


	follower = profile_json['edge_followed_by']['count']
	following = profile_json['edge_follow']['count']


	ff.append(follower)
	ff.append(following)
	return ff


#Seting Output1
output_name = "tb_convo_count_percent.csv"
f = open(output_name, "w")
label = "Username,Convo,Travel,Fashion,Culinary,Music\n"
f.write(label)

#Seting Output2
output_name2 = "tb_pivot_percent.csv"
g = open(output_name2, "w")
label2 = "Username,Sum of Fashion,Sum of Culinary,Sum of Music,Sum of Travel\n"
g.write(label2)

#Seting Output3
output_name3 = "tb_user_statistics.csv"
h = open(output_name3, "w")
label3 = "Username,Total Post,Total Likes,Average Like,Total Comment,Average Comment,Engagement,Followers,Following\n"
h.write(label3)

#Seting Output4
output_name4 = "tb_user_keywords.txt"
z = open(output_name4, "w")
label4 = "Username,PostID,Caption,Keyword,Interest\n"
z.write(label4)



hit = 1

#Data merupakan sebuah kumpulan kata secara temporary pada setiap caption (BERSIFAT TEMPORARY)
data = []


#perhitungan tiap post
post = []

#perhitungan untuk semua post
user_post = {}

#data user list
user_list = []


#Pencatatan. Hasilnya nantinya akan | count_user_posts['username'] = jumlah post |
count_user_posts = {}
count_user_likes = {}
count_user_comments = {}
count_user_followers = {}
count_user_following = {}

#load dictionary dari file CSV yang bernama dict.csv
mydict = {}
dfdict = pd.read_csv('lib2.csv')
for index, row in dfdict.iterrows():
    keyword = row['keywords'].replace('"','').replace(",", "").replace("/"," ").replace("("," ").replace(")","").lower()
    interst = row['interest'].lower()
    

    mydict[keyword] = interst

#load convo
convo = pd.read_csv('convo.csv')

for index, row in convo.iterrows():
	user_id = row['userid'].replace('"', '')
	username = row['username'].replace('"',"").replace(",","|")
	caption = str(row['caption']).replace(",","").replace(r"\u","|").lower().strip()
	post_id = row['postid'].replace('"','')

	print (str(hit) + ". " + username + ": " + caption)
	hit += 1
	if username not in user_list:
		user_list.append(username)


	#Mengecek apakah username sudah masuk di dalam count_user_post
	if username not in count_user_posts:
		count_user_posts[username] = 1
	else: 
		count_user_posts[username] += 1

	if username not in count_user_likes:
		count_user_likes[username] = row['like_count']
	else:
		count_user_likes[username] += row['like_count']

	if username not in count_user_comments:
		count_user_comments[username] = row['comment_count']
	else:
		count_user_comments[username] += row['comment_count']

	#Untuk mencocokan keyword dalam caption
	for i in mydict:
		if i in caption:
			post.append(mydict[i])
			isi = (str(username) + ',"' + str(post_id) + '",' + str(caption) + "," + str(i) + "," + str(mydict[i]) + "\n")
			z.write(isi)
#	label4 = "Username,PostID,Caption,Keyword,Interest\n"
	#Sebagai counter. atau perhitungan jumlah berapa travel, berapa culinary, berapa musik
	counter = Counter(post)
	post = []
	total_keyword = counter['traveling'] + counter['fashion'] + counter['culinary'] + counter['music']
	try:
		traveling =  counter['traveling'] / total_keyword
	except:
		traveling = 0
	try:
		fashion = counter['fashion'] / total_keyword
	except:
		fashion = 0
	try:
		culinary =  counter['culinary'] / total_keyword
	except:
		culinary = 0
	try:
		music =  counter['music'] / total_keyword
	except:
		music = 0

		#label = "username,convo,Travel,Fashion,Culinary,Music\n"
	line = username + "," + caption + "," + str(traveling) + "," + str(fashion) + "," + str(culinary) + "," + str(music) + "\n"
	f.write(line)

	if username not in user_post:
		user_post[username] = {}

	if 'traveling' not in user_post[username]:
		user_post[username]['traveling'] = 0

	if 'fashion' not in user_post[username]:
		user_post[username]['fashion'] = 0
	if 'culinary' not in user_post[username]:
		user_post[username]['culinary'] = 0
	if 'music' not in user_post[username]:
		user_post[username]['music'] = 0

	user_post[username]['traveling'] += traveling
	user_post[username]['fashion'] += fashion
	user_post[username]['culinary'] += culinary
	user_post[username]['music'] += music
print ("Menyimpan Data...")
for i in user_list:
	total_percent = user_post[i]['traveling'] + user_post[i]['fashion'] + user_post[i]['culinary'] + user_post[i]['music']

	try: percent_total_travel = float("{0:.2f}".format(user_post[i]['traveling'] / total_percent))  
	except: percent_total_travel = 0
	try: percent_total_fashion = float("{0:.2f}".format(user_post[i]['fashion'] / total_percent)) 
	except: percent_total_fashion = 0
	try: percent_total_culinary = float("{0:.2f}".format(user_post[i]['culinary'] / total_percent)) 
	except: percent_total_culinary = 0
	try: percent_total_music = float("{0:.2f}".format(user_post[i]['music'] / total_percent)) 
	except: percent_total_music = 0
#label2 = "Username,Sum of Fashion,Sum of Culinary,Sum of Music,Sum of Travel\n"
	g.write(str(i) + "," + str(percent_total_fashion) + "," + str(percent_total_culinary) + "," + str(percent_total_music) + "," + str(percent_total_travel) + "\n")




	average_likes = count_user_likes[i] / count_user_posts[i]
	average_comments = count_user_comments[i] / count_user_posts[i]

	engagement = average_likes + average_comments


	if i not in count_user_followers:
		count_user_followers[i] = insta(i)[0]
	if i not in count_user_following:
		count_user_following[i] = insta(i)[1]

#label3 = "Username,Total Post,Total Likes,Average Like,Total Comment,Average Comment,Engagement,Followers,Following\n"
	h.write(str(i) + "," + str(count_user_posts[i]).replace(",","|") + "," + str(count_user_likes[i]).replace(",","|") + "," + str(average_likes).replace(",","|") + "," + str(count_user_comments[i]).replace(",","|") + "," + str(average_comments).replace(",","|") + "," + str(engagement) + "," + str(count_user_followers[i]).replace(",","|") + "," + str(count_user_following[i]).replace(",","|") + "\n")
f.close()
g.close()
h.close()
z.close()
print("Data Tersimpan")
print("Proses Selesai")
