import datetime
def getNow():
    return str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))