username = input('Please enter your user name: ')
pw = input('Please enter your password: ')

pwlength = len(pw)
hidden_pw = (int(pwlength) * '*')

print(f'{username}, your password {hidden_pw} is {pwlength} characters long')