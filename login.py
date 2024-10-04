def login():
    db = open('userId.txt', 'r')
    userName = input("Create username:")
    Password = input('Create password:')
    Password1 = input('Confirm password:')
    d = []
    f = []
    for i in db:
        a,b = i.split(',')
        b = b.strip()
        d.append(a)
        f.append(b)
        data = dict(zip(d, f))
       

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

def access():
    db = open('userId.txt', 'r')
    userName = input("Enter your username:")
    Password = input('Enter your password:')

    if not len(userName or Password)<1:
        d = []
        f = []
        for i in db:
            a,b = i.split(',')
            b = b.strip()
            d.append(a)
            f.append(b)
        data = dict(zip(d, f))

        try:
            if data[userName]:
                try:
                    if Password == data[userName]:
                        print('login successfull')
                        print('Hi,' , userName)
                    else:
                        print('Password or Username incorrect')
                except:
                    print("incorrect password or username")
            else:
                print("Username doesn't exit")
        except:
            print('Login error')


def home(option=None):
    option = input('login  |  Signup:')
    if option == 'login':
        access()
    elif option == 'signup':
        login()
    else:
        print('Please enter an option')
home()
