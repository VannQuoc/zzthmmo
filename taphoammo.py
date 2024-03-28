from flask import Flask, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)
app.debug = False
csrf_token = None 
@app.route('/')
def abc():
    return "Api By Mon Leo Hay Khok Telegram @Monleohaykhok"
@app.route('/api')
def get_cookies():
        cookies = request.cookies
        cookies_dict = cookies.to_dict()
        filtered_cookies = {}
        keys_to_keep = ['JSESSIONID','remember-me']

        for key, value in cookies_dict.items():
            if key in keys_to_keep:
                filtered_cookies[key] = value
            headers = {
			'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
			'accept-language': 'en-US,en;q=0.9',
			'cache-control': 'no-cache',
			'cookie': '; '.join([f"{key}={value}" for key, value in filtered_cookies.items()]),
			'pragma': 'no-cache',
			'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
			'sec-ch-ua-mobile': '?0',
			'sec-ch-ua-platform': '"Windows"',
			'sec-fetch-dest': 'document',
			'sec-fetch-mode': 'navigate',
			'sec-fetch-site': 'none',
			'sec-fetch-user': '?1',
			'upgrade-insecure-requests': '1',
			'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
		}
        response = requests.get('https://taphoammo.net/', headers=headers)
        try:
            html_content = response.text
            soup = BeautifulSoup(html_content, 'html.parser')
            csrf_meta_tag = soup.find('meta', {'name': '_csrf'})
            if csrf_meta_tag:
                csrf_token = csrf_meta_tag['content']
            headers = {
				'accept': 'text/plain, */*; q=0.01',
				'accept-language': 'en-US,en;q=0.9',
				'cache-control': 'no-cache',
				'cookie': '; '.join([f"{key}={value}" for key, value in filtered_cookies.items()]),
				'origin': 'https://taphoammo.net',
				'pragma': 'no-cache',
				'referer': 'https://taphoammo.net/',
				'sec-ch-ua': '"Google Chrome";v="123", "Not:A-Brand";v="8", "Chromium";v="123"',
				'sec-ch-ua-mobile': '?0',
				'sec-ch-ua-platform': '"Windows"',
				'sec-fetch-dest': 'empty',
				'sec-fetch-mode': 'cors',
				'sec-fetch-site': 'same-origin',
				'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
				'x-csrf-token': csrf_token,
				'x-requested-with': 'XMLHttpRequest',
			}
            response = requests.post('https://taphoammo.net/api/getUserBalance',headers=headers)
            balance = int(response.text)
            if balance > 0:
                return f"HIT {balance} MONLEOHAYKHOK"
        except ValueError as e:
            print(f"Error parsing JSON: {e}")

        return "Error retrieving data"
  
if __name__ == '__main__':
        app.run(host='0.0.0.0')
