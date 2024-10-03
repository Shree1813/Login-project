def login():
    db = open('userId.txt', 'r')
    userName = input("Create username:")
    Password = input('Create password:')
    Password1 = input('Confirm password:')

    if Password != Password1:
        print("Passwords don't match, restart")
        login()

    else:
        if len(Password)<= 6:
            print('Password too short, restart:')
            login()

        else:
            db = open('userId.txt', 'a')
            db.write(userName+', '+Password+'\n')
            print('Logged in successfully:')

login()