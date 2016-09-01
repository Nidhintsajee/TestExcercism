name=raw_input("Enter your name : ")
def hello(name=''):
    if name:
        print 'Hello, '+str(name)+'!'
    else:
        print 'Hello, World!'

hello(name)
