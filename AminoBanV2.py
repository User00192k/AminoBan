import aminofix
from colored import fore, back, style, attr
attr(0)
print(fore.DARK_GREEN_SEA + style.BOLD)
client = aminofix.Client()
print(""" 
Made by Xsarz
GitHub: https://github.com/xXxCLOTIxXx
Telegram Group: https://t.me/DxsarzUnion
Telegram: @DXsarz
YouTube: https://www.youtube.com/channel/UCNKEgQmAvt6dD7jeMLpte9Q/

BANScript
""")
print(fore.BLUE + style.BOLD)
while True:
	try:
		gmail = input("Почта>>")
		password = input("Пароль>>")
		client.login(email=gmail, password=password)
		break
	except:
		print("\nОшибка входа!\n")
_ = input("|1|Все участники\n|2|Онлайн участники\nПо какому списко будете искать участника>> ")
if _ == '1':
	print("Выбран список всех участников.\n")
elif _ == '2':
	print("Выбран список онлайн участников.\n")
else: print("По умолчанию выбран режим всех участников.\n"); _ = '1'
while True:
	try:
		url = input('Введите ссылку на соо>>')
		print('') 
		comId = client.get_from_code(url).comId
		sub_client = aminofix.SubClient(comId=comId, profile=client.profile)
		break
	except Exception as ex:
		print(f"Ошибка!\n\n{ex}\n")
if _ == '1':
	users = sub_client.get_all_users(size=100).json['userProfileList']
else:
	users = sub_client.get_online_users(size=100).json['userProfileList']
users_ = {}
for i in range(len(users)):
	user_name = users[i]['nickname']
	userId = users[i]['uid']
	print(f'{i}){user_name}  :   {userId}')
	users_[i] = userId
while True:
	try:
		num = int(input("\nВведите номер пользователя, которого хотите забанить>> "))
		break
	except: print("\nОшибка!\nВозможно вы ввели не цифру\n")
ban = input("Укажите причину бана (Минимум 3 слова)>> ")
try:
	sub_client.ban(userId=users_[num], reason=ban)
	print("Пользователь успешно забанен!")
except:
	print("Ошибка, не удалось забанить пользователя, возможно вы зашли не на аккаунт лидера")