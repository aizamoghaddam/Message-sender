import pyautogui
from random import choice

print("""
سلام این یک ربات ساخته شده با PyAuToGui است ک بعد از ران کردن main.py کنترل موس را از شما میگیرد تا عملیاتش را 
انجام دهد پس در وارد کردن تعداد مسیج هایی ک میخاهید ارسال کنید دقت کنید 
تلگرام را تمام صفحه باز کنید تا در پیدا کردن باکس تایپ اشتباه نکند 
این ربات در  ابعاد مانیتور 1080,1920 ساخته شده اگر ابعاد مانتیور شما متفاوت است آن را میتوانید در سورس تنظیم کنید(width, height) 
""")

x = str(input('enter your message: '))
z = 1
y = int(input('how many messages should I send?: '))
width = 1136
height = 993


for i in range(z, y):
    pyautogui.click(width, height)
    # pyautogui.write(choice(lst))
    pyautogui.write(x)
    pyautogui.press('enter')

