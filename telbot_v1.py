# from crypt import methods
# from flask import Flask
# from flask import request
# from flask import Response
# import requests


# TOKEN = "6580538530:AAFuEZnj5_3WdOYkLzzx8wmjoh_bd5bHa74"
# app = Flask(__name__)

# def parse_message(message):
#     print("message-->",message)
#     chat_id = message['message']['chat']['id']
#     txt = message['message']['text']
#     print("chat_id-->", chat_id)
#     print("txt-->", txt)
#     return chat_id,txt

# def tel_send_message(chat_id, text):
#     url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
#     payload = {
#                 'chat_id': chat_id,
#                 'text': text,
#                 }
#     r = requests.post(url,json=payload)
#     return r

# @app.route('/', methods=['GET', 'POST'])

# def index():
#     if request.method == 'POST':
#         msg = request.get_json()

#         chat_id,txt = parse_message(msg)
#         if txt == "hi":
#             tel_send_message(chat_id,"Hello!!")
#         if txt == "h1":
#             tel_send_message(chat_id,"Hello h1")
#         else:
#             tel_send_message(chat_id,'from webhook')

#         return Response('ok', status=200)
#     else:
#         return "<h1>Welcome1!</h1>"     
    


# @app.route('http://136.243.86.130/api/find-server-test' , methods='POST')
# def test_server():



# if __name__ == '__main__':
#    app.run(debug=True)



#-------------------------------------------------------------------------------------
# import numpy as np
import os
file_path = os.path.abspath('/home/telegrambot/database')
import sys
sys.path.append(file_path)
from db import DB

db = DB()
mycursor=db.get_cursor()
users = db.select("SELECT id,name FROM provider ")
db.get_commit()

# users=np.array(users)
# print(users)
#-------------------------------------------------------------------------------------
# servers2=users
# matching_id = None
# for button in servers2:
#     if button[1] == 'های آمریکا':
#         matching_id = button[0]
#         break 
    
# print(matching_id)







from flask import Flask
from flask import request
from flask import Response
import requests
import json



TOKEN = "6524694661:AAH1YrHD9yPMqwrBu6yG88TPJvXFKMg0QVo"
 
app = Flask(__name__)
 
def tel_parse_message(message):
    print("message-->",message)
    try:
        chat_id = message['message']['chat']['id']
        txt = message['message']['text']
        username = message['message']['chat']['username']
        print("chat_id-->", chat_id)
        print("txt-->", txt)
        print("username-->", username)
 
        return chat_id,txt,username
    except:
        print("NO text found-->>")

def tel_parse_get_message(message):
    print("message-->",message)
   
    try:
        g_chat_id = message['message']['chat']['id']
        g_file_id = message['message']['photo'][0]['file_id']
        print("g_chat_id-->", g_chat_id)
        print("g_image_id-->", g_file_id)
 
        return g_chat_id,g_file_id
    except:
        try:
            g_chat_id = message['message']['chat']['id']
            g_file_id = message['message']['video']['file_id']
            print("g_chat_id-->", g_chat_id)
            print("g_video_id-->", g_file_id)
 
            return g_chat_id,g_file_id
        except:
            try:
                g_chat_id = message['message']['chat']['id']
                g_file_id = message['message']['audio']['file_id']
                print("g_chat_id-->", g_chat_id)
                print("g_audio_id-->", g_file_id)
 
                return g_chat_id,g_file_id
            except:
                try:
                    g_chat_id = message['message']['chat']['id']
                    g_file_id = message['message']['document']['file_id']
                    print("g_chat_id-->", g_chat_id)
                    print("g_file_id-->", g_file_id)
 
                    return g_chat_id,g_file_id
                except:
                    print("NO file found found-->>")
 
def tel_send_message(chat_id, text):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    payload = {
                'chat_id': chat_id,
                'text': text
                }
   
    r = requests.post(url,json=payload)
 
    return r
 
def tel_send_image(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    payload = {
        'chat_id': chat_id,
        'photo': "https://hologate2.plus/price",
        'caption': "This is a price list"
    }
 
    r = requests.post(url, json=payload)
    return r

def tel_send_audio(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendAudio'
 
    payload = {
        'chat_id': chat_id,
        "audio": "http://www.largesound.com/ashborytour/sound/brobob.mp3",
 
    }
 
    r = requests.post(url, json=payload)
 
    return r

def tel_send_video(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendVideo'
 
    payload = {
        'chat_id': chat_id,
        "video": "https://www.appsloveworld.com/wp-content/uploads/2018/10/640.mp4",
 
    }
 
    r = requests.post(url, json=payload)
 
    return r

def tel_send_document(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendDocument'
 
    payload = {
        'chat_id': chat_id,
        "document": "http://www.africau.edu/images/default/sample.pdf",
 
    }
 
    r = requests.post(url, json=payload)
 
    return r

def tel_send_poll(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendPoll'
    payload = {
        'chat_id': chat_id,
        "question": "خورشید از کدام جهت طلوع می کند؟",
        "options": json.dumps(["شمال", "جنوب", "شرق", "غرب"]),
        "is_anonymous": False,
        "type": "quiz",
        "correct_option_id": 2
    }
 
    r = requests.post(url, json=payload)
 
    return r

def tel_send_button(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "این چیه؟",
                'reply_markup': {'keyboard': [[{'text': 'پرداخت sla'}, {'text': 'صندلی'}]]}
    }
 
    r = requests.post(url, json=payload)
 
    return r

def send_button1(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "به ربات هلو vpn خوش آمدید. لطفا یک گزینه را انتخاب نمائید",
                'reply_markup': {'keyboard': [[ {'text': 'نرم افزارهای لازم'},{'text': 'پشتیبانی'},{'text': 'پرداخت وجه'},{'text': 'اکانت تست'},{'text': 'قیمت خدمات'}]]}
    }
 
    r = requests.post(url, json=payload)
 
    return r

def SendPrice(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "برای انجام مراحل خرید یکی از بسته ها  و یا بازگشت را انتخاب فرمائید ",
                'reply_markup': {'keyboard': [[{'text': '1 ماهه 2 دلار'},{'text': ' 2 ماهه 4 دلار'}, {'text': '3 ماهه 5 دلار'},{'text': '6 ماهه 10 دلار'},{'text': '12 ماهه 18 دلار'},{'text': 'پشتیبانی'},{'text': 'صفحه 1'}]]}
    }
 
    r = requests.post(url, json=payload)
 
    return r

def support(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "لطفا سئوالات متداول را مطالعه کنید و چنانچه پاسخ خود را دریافت نکردید به کارشناسان ما پیام دهید لازم به ذکر است زمان پاسخگوئی از ساعت 9 صبح لغایت 4 بعد از ظهر می باشد.  ",
                'reply_markup': {'keyboard': [[{'text': ' صفحه 1'},{'text': 'قیمت خدمات'}, {'text': 'چت با کارشناس'},{'text': 'سئوالات متداول'}]]}
    }
 
    r = requests.post(url, json=payload)
 
    return r

def peyment_log_received(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "لطفا اطلاعات واریزی خود را از طریق لینک ذیل ارسال کنید تا بررسی و اشتراک شما تحویل گردد.  ",
                'reply_markup': {'keyboard': [[{'text': 'سئوالات متداول'}, {'text': 'چت با کارشناس'},{'text': ' صفحه 1'}]]}
    }
 
    r = requests.post(url, json=payload)
 
    return r


def tel_send_inlinebutton(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "این چیه؟",
        'reply_markup': {
            "inline_keyboard": [[
                {
                    "text": "الف",
                    "callback_data": "ic_A"
                },
                {
                    "text": "ب",
                    "callback_data": "ic_B"
                }]
            ]
        }
    }
    r = requests.post(url, json=payload)
    return r

def support_id(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
                'text': "https://t.me/hologate5" 
        
    }
    r = requests.post(url, json=payload)
    return r

def payment_tron(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    
    payload = {
        'chat_id': chat_id,
                'text': " هلوگیت از طریق درگاه آنلاین پرداخت رمز ارزی را انجام می دهد و برای پرداخت با ترون یا تتر شما می توانید وارد فروشگاه هلوگیت شوید و در قسمت خرید اشتراک گزینه پرداخت با رمز ارز را انتخاب کنید. https://hologate2.plus/shop "
                #'text': "https://t.me/hologate5" 
            
    }
    r = requests.post(url, json=payload)
    return r

def tel_send_inlineurl(chat_id):
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
 
    payload = {
        'chat_id': chat_id,
        'text': "دوست دارید از کدام لینک بازدید کنید؟",
        'reply_markup': {
            "keyboard": [
                [
                    {"text": "ورود به سایت ", "url": "http://hologate2.plus/"},
                    {"text":"چت با پشتیبان","url":"https://t.me/hologate5"}
                ]
            ]
        }
    }
 
    r = requests.post(url, json=payload)
 
    return r
def tel_upload_file(file_id):
    url = f'https://api.telegram.org/bot{TOKEN}/getFile?file_id={file_id}'
    a = requests.post(url)
    json_resp = json.loads(a.content)
    print("a-->",a)
    print("json_resp-->",json_resp)
    file_pathh = json_resp['result']['file_path']
    print("file_path-->", file_pathh)
   
    url_1 = f'https://api.telegram.org/file/bot{TOKEN}/{file_pathh}'
    b = requests.get(url_1)
    file_content = b.content
    with open("/home/bot/" + file_pathh, "wb") as f:
        f.write(file_content)
  
  
  

# # #11111111111111111111111111111111111111111111111111111111
user_email = None  # Global variable to store user email


def send_button3(chat_id, user_email):
    chat_id = chat_id
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    # user_email = get_user_email()
    # user_email = 'fafa@gmail.com'
    # print(user_email)
    # Send a POST request to the server
    response = requests.post('http://136.243.86.130/api/find-server-test' ,  data={'email': user_email , 'chat':str(chat_id)}, headers={'token':'UGFGtZ.RkMfiqfy80O5EP0VoBiVrcs3GGcjJjGKAyr2UAxNtG'})

    if response.status_code == 200:
        
        # Parse the JSON response
        servers = response.json()
        # tel_send_message(chat_id, str(servers)) 
        buttons = []
        if len(servers)>2:
            # Create buttons for each available server
            # buttons = []
            for server in servers:
                # tel_send_message(chat_id, str(chat_id))
                server_name = server['name']
                # server_id = "server_id:" + str(server['id'])
                    
                server_id =server['id']
                    
                buttons.append([{"text": server_name, "callback_data": str(server_id)}])
                
                
            # Build the keyboard markup
            reply_markup = {
                "keyboard": buttons,
                "one_time_keyboard": True  # Optional: Hide the keyboard after selection
            }

            # Build the payload based on available servers
            payload = {
                'chat_id': chat_id,
                'text': "ایمیل شما دریافت شد. لطفا سرور مورد نظر را انتخاب کنید!",
                'reply_markup': reply_markup,
                # 'text': str(servers)
                # 'reply_markup': reply_markup
            }

        # Send the message with the dynamic keyboard

        else:   
            # tel_send_message(chat_id, str(servers)) 
            
            payload = {
                'chat_id': chat_id,
                'text': str(servers['message'])
                # 'text': str(servers)
                # 'reply_markup': reply_markup
            }
            
        
        r = requests.post(url, json=payload)
        
        return r
    # Handle if the response status code is not 200
    return None

#888888888888888888888888888888888888888888888888888888888
def click_button3(chat_id, name_of_server):


    chat_id = chat_id
    name_of_server=name_of_server
    url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    
    ## using another API
    # response2 = requests.post('http://136.243.86.130/api/get-server-test', headers={'token':'UGFGtZ.RkMfiqfy80O5EP0VoBiVrcs3GGcjJjGKAyr2UAxNtG'})

    # if response2.status_code == 200:
    #     servers2 = response2.json()
        
    #     # buttons2 = [
    #     #     {"id": 1, "name": "های آمریکا", "irancell": "123", "mci": "456"},
    #     #     {"id": 2, "name": "های روسیه", "irancell": "789", "mci": "012"},
    #     #     {"id": 3, "name": "های آلمان", "irancell": "345", "mci": "678"}
    #     # ]

    #     # text = "hi Russia"

    #     matching_id = None

    #     for button in servers2:
    #         if button["name"] == name_of_server:
    #             matching_id = button["id"]
    #             break
    
    
    #using dtabase to read servers data from table
    servers2=users
    matching_id = None
    for button in servers2:
        if button[1] == name_of_server:
            matching_id = button[0]
            break    
        
    if matching_id is not None:
        response3 = requests.post('http://136.243.86.130/api/account-test' ,  data={'provider': str(matching_id) , 'chat':str(chat_id)}, headers={'token':'UGFGtZ.RkMfiqfy80O5EP0VoBiVrcs3GGcjJjGKAyr2UAxNtG'})
            
        if response3.status_code == 200:
            # Parse the JSON response
            servers3 = response3.json() 
            
            if "message" in servers3:
                
                payload = {
                    'chat_id': chat_id,
                    # 'text': matching_id
                    # 'text': chat_id
                    'text': str(servers3['message'])
                    # 'txt': name_of_server
                    # 'text': str('hi')
                }
            
            # else:
            #     # Print the test account information
            #     username = servers3["username"]
            #     password = servers3["password"]
            #     host = servers3["host"]
            #     port = servers3["port"]
            #     info_message = f"بفرمایید اکانت تست:\n username: {username}\n password: {password}\n host: {host}\n port: {port}"
            #     payload = {
            #         'chat_id': chat_id,
            #         # 'text': matching_id
            #         # 'text': chat_id
            #         'text': info_message
            #         # 'txt': name_of_server
                    
                # }
            else:
                
                username = servers3["username"]
                password = servers3["password"]
                host = servers3["host"]
                port = servers3["port"]
                
        #         info_messages = [
        # f"Username: {username}",
        # f"Password: {password}",
        # f"Host: {host}",
        # f"Port: {port}"]
                info_messages = [
        "Username:",
        f"{username}",
        "Password:",
        f"{password}",
        "Host:",
        f"{host}",
        "Port:",
        f"{port}"]
                
                
                
                for info_message in info_messages:
                    payload = {
            'chat_id': chat_id,
            'text': info_message
        }
                

                    r = requests.post(url, json=payload)

    return r    
            
    
        

        # if matching_id is not None:
        #     response3 = requests.post('http://136.243.86.130/api/account-test' ,  data={'provider': str(matching_id) , 'chat':str(chat_id)}, headers={'token':'UGFGtZ.RkMfiqfy80O5EP0VoBiVrcs3GGcjJjGKAyr2UAxNtG'})
            
        #     if response3.status_code == 200:
        #         # Parse the JSON response
        #         servers3 = response3.json() 
                
        #         payload = {
        #             'chat_id': chat_id,
        #             # 'text': matching_id
        #             # 'text': chat_id
        #             'text': str(servers3)
        #         }

        # r = requests.post(url, json=payload)

        # return r

    return None
#888888888888888888888888888888888888888888888888888888888

# # #33333333333333333333333333333333333333333333333333333333333333333333333333333333333


# def get_user_email():
#     chat_id=chat_id
#     response = requests.get(f'https://api.telegram.org/bot{TOKEN}/getUpdates')
    
#     if response.status_code == 200:
#         data = response.json()
#         if 'result' in data and len(data['result']) > 0:
#             # Assuming the latest message is in the first result
#             if 'message' in data['result'][0]:
#                 message = data['result'][0]['message']
#                 if 'text' in message:
#                     user_email = message['text']
#                     return user_email
    
#     return None

# def process_messages():
#     while True:
#         user_email = get_user_email()
#         chat_id=chat_id
#         if user_email:
#             # Send a POST request to the server with email and chat_id in the headers
#             # headers = {'email': user_email, 'chat': str(chat_id)}
#             response = requests.post('http://136.243.86.130/api/find-server-test' ,  headers={'email': user_email , 'chat':str(chat_id)})
    
#             if response.status_code == 200:
#                 # Parse the JSON response
#                 data = response.json()
    
#                 # Extract the available servers information
#                 servers = data['servers']
    
#                 # Create buttons for each available server
#                 buttons = []
#                 for server in servers:
#                     server_name = server['name']
#                     server_id = server['id']
#                     buttons.append([{"text": server_name, "callback_data": str(server_id)}])
    
#                 # Build the keyboard markup
#                 reply_markup = {
#                     "keyboard": buttons,
#                     "one_time_keyboard": True  # Optional: Hide the keyboard after selection
#                 }
    
#                 # Build the payload based on available servers
#                 payload = {
#                     'chat_id': chat_id,
#                     'text': "سرور مورد نظر را انتخاب کنید!",
#                     'reply_markup': reply_markup
#                 }
    
#                 # Send the message with the dynamic keyboard
#                 url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
#                 r = requests.post(url, json=payload)
    
#                 # Break the loop after sending the message
#                 return r

#             # Handle if the response status code is not 200
#             return None

# def send_button2(chat_id):
#     url = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    
#     # Send a message to the user to request their email
#     email_message = "Please enter your email:"
#     email_payload = {
#         'chat_id': chat_id,
#         'text': email_message
#     }
#     email_response = requests.post(url, json=email_payload)
    
#     if email_response.status_code == 200:
#         # Start the message processing loop
#         process_messages()
    
#     # Handle if the response status code is not 200
#     return


# # #333333333333333333333333333333333333333333333333333333333333333333333333333333333333
      

 
@ app.route('/', methods=['GET', 'POST'])
def index():
    software = "بهترین نرم افزار برای اندروید و ios نپسترنت وی یا nV می باشد\n https://hologate2.plus/napsternetv/ \n اگر دسترسی به گوگل پلی هم ندارید از طریق سایت ما دانلود و نصب کنید. \n برای ویندوز هم بعد از خرید اکانت  راهنمای لازم برای شما ارسال خواهد شد. \n "  
    cafeArzLink='https://app.cafearz.com/login  لینک مراجعه مستقیم به کافه ارز - کارمزد 1000 تومان'
    novinLink = "https://panel.novinpardakht.com/    \nکارمزد 20 هزار تومان لینک مراجعه مستقیم به فروشگاه نوین پرداخت"
    nikpardakht = "آموزش خرید ووچر پرفکت مانی از سایت نیک پرداخت \n1. وارد سایت ذیل می شوید و ثبت نام می کنید \n https://nikpardakht.com/ \n 2. از منوی سمت راست خرید ووچر پرفکت مانی را انتخاب کنید  \n 3. مبلغ دلاری را وارد کرده و پرداخت کنید.\n 4. بعد از 10 دقیقه شماره ووچر و کدفعالسازی در سفارش شما اضافه می شود\n"
    tron = " هلوگیت از طریق درگاه آنلاین پرداخت رمز ارزی را انجام می دهد و برای پرداخت با ترون یا تتر شما می توانید وارد فروشگاه هلوگیت شوید و در قسمت خرید اشتراک گزینه پرداخت با رمز ارز را انتخاب کنید. https://hologate2.plus/shop"
    transaction_log_send = "بعد از پرداخت وجه اتوماتیک مبلغ دلاری به کیف پول هلوگیت شما اضافه می شود و اکانت شما تحویل می گردد در صورتی که مشکلی ایجاد شد به پشتیبانی در  تلگرام پیام دهید \n https://t.me/hologate5 "
    novin = "https://hologate2.plus/xray/images/pages/buy-ssh/novin.mp4 فیلم خرید پرفکت مانی از نوین پرداخت "
    fq1 = "\n❓اگر سرور فیلتر شود پول من چه می شود ؟\n  ما از تکنولوژی هایی استفاده می کنیم که احتمال فیلتر شدن سرور پائین است ولی تضمین می کنیم که اگر سرور فیلتر شد در چند ساعت سرور جایگزین فعال می کنیم و اشتراک قابل استفاده خواهد بود \n"
    fq2 = "\n❓آی پی سرور ثابت است یا عوض می شود ؟\n ولی می توانیم با درخواست شما از همان کشور به شما اشتراک واگذار نمائیم که کشور شما عوض نشود. آی پی سرورها ثابت است و تغییر نمی کند مگر اینکه سرور فیلتر شود که چاره دیگری بجز عوض کردن سرور نداریم \n"
    fq3 = "\n❓آیا شما عمده فروشی هم دارید ؟\n  شما می توانید مثلا 10 دلار کیف پول خود را شارژ کنید و 1 دلار هدیه بگیرید و هر موقع مشتری رسید بلافاصله از کیف پول اشتراک را تحویل دهید لازم به ذکر است که 20 دلار 3 دلار هدیه و 50 دلار 10 دلار اضافه شارژ دارد.\n"
    fq4 = "\n❓تعداد پیش فرض یوزر اکانت های شما چند عدد است ؟ \n همه اکانت ها پیش فرض 2 کاربر همزمان هستند.\n"
    fq5 = "\n❓اگر بیش از 2 کاربر همزمان با اکانت من متصل شوند چه می شود ؟ \n اتصالات جدید تا زمانی که 2 اتصال قبلی متصل هستند قابلیت اتصال ندارند.\n"
    fq6 = "\n❓از چه کشورهایی می توانید اکانت واگذار کنید ؟\n ما سرورهای مختلفی در کشورهای آمریکا، آلمان، انگلستان، لهستان و .... داریم که اگر کشور خاصی مد نظر شماست قبل از خرید با پشتیبانی هماهنگ کنید.\n"
    fq7 = "\n❓سرعت سرورها چطور است ؟ \n وقتی با اکانت هلو کار می کنید تقریبا به خوبی زمانی که اینستاگرام فیلتر نبود می توانید از شبکه های اجتماعی و ... استفاده نمائید. \n"
    fq8 = "\n❓چه نرم افزاری باید نصب کنم ؟\n برای نصب فیلترشکن در اندروید و ios و ویندوز راهنمای دانلود و نصب در این لینک می باشد \n https://hologate2.plus/add-ssh-key \n"
    fq9 = "\n❓حجم اکانت ها نامحدود است ؟ \n بله نامحدود است."
    fqf = fq1 + fq2 + fq3 + fq4 + fq5 +fq6 + fq7 + fq8 + fq9
    select_payment = "\n روش دوم استفاده از رمز ارزهای تتر و ترون می باشد که اگر کیف پول رمز ارزی ندارید بهتر است از روش اول استفاده نمائید برای آشنائی بهتر لینک ذیل را مطالعه کنید https://hologate2.plus/crypto-payment"
    payment = "با استفاده از راهنمای ذیل، یک کارت مثلا 2 دلاری پرفکت مانی خریداری کنید و بعد از طریق فروشگاه اشتراک خود را فورا تحویل بگیرید . \n https://hologate2.plus/shop \n" 
    if request.method == 'POST':
        msg = request.get_json() 
        try:
            chat_id, txt, username = tel_parse_message(msg)
            if txt == "/start" or txt == "صفحه 1":
                send_button1(chat_id)
                
                


            elif txt == "قیمت خدمات":
                tel_send_image(chat_id)
                SendPrice(chat_id)
            

            elif txt ==  "اکانت تست" :
                tel_send_message(chat_id, 'لطفا ایمیل خود را ارسال نمائید.' )
                # a1 = get_user_email(chat_id)
                # print(a1)
                        
            elif '@' in txt :
                email = txt
                send_button3(chat_id, email)
                # tel_send_message(chat_id, 'ایمیل شما دریافت شد' )
            
            # elif txt.startswith("server_id:"):
            #     server_id = txt.split(":")[1]
            #     headers = {
            #         'email': user_email,  # Access the global variable
            #         'chat': str(chat_id),
            #         'server_id': server_id
            #     }
            #     response = requests.post('http://136.243.86.130/api/account-test', headers=headers)
            #     response_data = response.json()
            #     message = response_data['message']
            #     tel_send_message(chat_id, message)



            elif txt == "نرم افزارهای لازم":
                tel_send_message(chat_id, fq8)
            
            elif (txt == "1 ماهه 2 دلار" or txt == "2 ماهه 4 دلار" or txt == "3 ماهه 5 دلار" or txt == "6 ماهه 10 دلار" or txt == "12 ماهه 18 دلار"):  
                tel_send_message(chat_id,"https://hologate2.plus/xray/images/pages/buy-ssh/buy%20voucher%20cafearz.mp4 شما می توانید مثلا 2 دلار مطابق فیلم ذیل از کافه ارز بخرید و بعد در فروشگاه طبق فیلم بلافاصله اکانت را دریافت نمائید  ")
                tel_send_message(chat_id, cafeArzLink )
                tel_send_message(chat_id, novin )
                tel_send_message(chat_id, novinLink )
                tel_send_message(chat_id, select_payment )
                tel_send_message(chat_id, tron )
                tel_send_message(chat_id, transaction_log_send)

                   

            elif txt == "پشتیبانی":
                tel_send_message(chat_id, fqf )
                support(chat_id)

            elif txt == "چت با پشتیبان" or txt == "چت با کارشناس":
                tel_send_message(chat_id,"https://t.me/hologate5")

            # elif txt == "تست" :
                
            #     # tel_send_message(chat_id, 'در حال تست هستید' )
            #     test()
                # def test():
                #     payment = "با استفاده از راهنمای ذیل، یک کارت مثلا 2 دلاری پرفکت مانی خریداری کنید و بعد از طریق فروشگاه اشتراک خود را فورا تحویل بگیرید . \n https://hologate2.plus/shop \n" 
                #     if request.method == 'POST':
                #         msg = request.get_json() 
                #         try:
                #             chat_id, txt, username = tel_parse_message(msg)

                #             if '@' in txt :
                #                 email = txt
                #                 send_button3(chat_id, email )
                #             # else:
                #             #     tel_send_message(chat_id, 'پیام شما معتبر نیست.')
                #         except:
        
                #             tel_send_message(chat_id, 'error')            
                        
                #         return Response('ok', status=200)  
                #     else:
                #         return "<h1>Welcome!</h1>"
            
            
                
                

            
            elif txt == "سئوالات متداول":
                tel_send_message(chat_id, fqf )
                
            elif txt == "پرداخت وجه":
                tel_send_message(chat_id,"https://hologate2.plus/xray/images/pages/buy-ssh/buy%20voucher%20cafearz.mp4 شما می توانید مثلا 2 دلار مطابق فیلم ذیل از کافه ارز بخرید و بعد در فروشگاه طبق فیلم بلافاصله اکانت را دریافت نمائید  ")
                tel_send_message(chat_id, cafeArzLink )
                tel_send_message(chat_id, novin )
                tel_send_message(chat_id, novinLink )
                tel_send_message(chat_id, select_payment )
                tel_send_message(chat_id, tron )
                tel_send_message(chat_id, transaction_log_send)

                                
                


            elif txt == "hi":
                payment_tron(chat_id)
            elif txt == "image":
                tel_send_image(chat_id)
            elif txt == "audio":
                tel_send_audio(chat_id)
            elif txt == "video":
                tel_send_video(chat_id)
            elif txt == "file":
                tel_send_document(chat_id)
            elif txt == "poll":
                tel_send_poll(chat_id)
            elif txt == "button":
                tel_send_button(chat_id)
            elif txt == "inline":
                tel_send_inlinebutton(chat_id)
            elif txt == "inlineurl":
                tel_send_inlineurl(chat_id)
            # اگر یک سرور را انتخاب کند برای ساخت تست وارد این قسمت خواهیم شد
            elif "های" in txt :
                name1=txt
                click_button3(chat_id, name1)
                # server_id = server_id[1]
                

            
            
            else:
                tel_send_message(chat_id, 'پیام شما معتبر نیست.')
        except:
            try:
                chat_id, file_id = tel_parse_get_message(msg)
                tel_upload_file(file_id)
                tel_send_message(chat_id,"فایل شما ذخیره شد")
            except Exception as e:
                print("from index-->" + str(e))
        return Response('ok', status=200)  
    else:
        return "<h1>Welcome!</h1>"
 

if __name__ == '__main__':
    app.run(host="0.0.0.0",port='8000')
    
#






