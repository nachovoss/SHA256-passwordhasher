import hashlib
print('wellcome to password hasher to exit the script type exit')
m=hashlib.sha256()
while True:

    wordtohash = input('type a password you want to encrypt: ')
    if 'exit' in wordtohash:
        quit()
    else:
      m.update(wordtohash.encode('utf-8'))
      print('Your encrypted password is: ' + m.hexdigest())

    
