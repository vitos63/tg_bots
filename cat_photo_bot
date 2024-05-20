import requests
import time
api_urls = 'https://api.telegram.org/bot'
bot_token = '7069583576:AAH0aQXr9L1e8pRw3ndPmc2r-zoJvYtQnNU'
API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
counter = 0
offset = -2
timeout = 100
text = 'Здесь должна была быть фотка с котиком :('
while counter < 300:
    start = time.time()
    update = requests.get(
        f'{api_urls}{bot_token}/getupdates?offset={offset+1}&timeout={timeout}').json()
    if update['result']:
        for result in update['result']:
            offset = result["update_id"]
            chat_id = result['message']['from']['id']
            cat_photo = requests.get(f'{API_CATS_URL}')
            if cat_photo.status_code == 200:
                cat_photo = cat_photo.json()[0]['url']
                requests.get(f'{api_urls}{bot_token}/sendPhoto?chat_id={chat_id}&photo={cat_photo}')
            else:
                requests.get(f'{api_urls}{bot_token}/sendMessage?chat_id={chat_id}&text={text}')
    end = time.time()
    print(f'Время между запросами: {end-start}')
    counter += 1
