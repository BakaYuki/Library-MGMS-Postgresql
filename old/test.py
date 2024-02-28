LOGIN_CHECK = [False]
def run():
    print(LOGIN_CHECK)
    LOGIN_CHECK[0] = True
    print(LOGIN_CHECK)
run()