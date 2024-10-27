def sd():
    a=input('Do you want to shutdown y/n:')
    if a=='y':
        print('Shuting down')
    elif a=='n':
        print('Abort shutdown')
    else:
        print('sorry')
        sd()
sd()