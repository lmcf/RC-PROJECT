global DEBUG
DEBUG = True

def debug( texto ):
    global DEBUG
    if DEBUG is True:
        print( str( texto ) )