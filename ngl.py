import requests,uuid
ses = requests.Session()
user = input(" masukan user : ")
text = input(" masukan pesan: ")

def device_id():
	return f"{uuid.uuid4().hex[:30]}"
	
def hgl():
	data = {
	    "username": user,
	    "question": text,
	    "deviceId": device_id(),
	    "gameSlug": "",
	    "referrer": ""
	}
	
	header = {
		"Host": "ngl.link",
		"content-length": "105",
		"sec-ch-ua": '"Not/A)Brand";v="99", "Google Chrome";v="115", "Chromium";v="115"',
		"accept": "*/*",
		"content-type": "application/x-www-form-urlencoded; charset=UTF-8",
		"x-requested-with": "XMLHttpRequest",
		"sec-ch-ua-mobile": "?1",
		"user-agent": "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Mobile Safari/537.36",
		"sec-ch-ua-platform": '"Android"',
		"origin": "https://ngl.link",
		"sec-fetch-site": "same-origin",
		"sec-fetch-mode": "cors",
		"sec-fetch-dest": "empty",
		"referer": f"https://ngl.link/{user}",
		"accept-encoding": "gzip, deflate, br",
		"accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"
		}
	
	for x in range(10):
		post = ses.post(f"https://ngl.link/api/submit", headers=header, data=data)
		print(data)
		
hgl()