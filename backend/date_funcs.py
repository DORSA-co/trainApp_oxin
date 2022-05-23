from persiantools.jdatetime import JalaliDate
import datetime


def get_date(persian=True, folder_path=False):
    if persian:
        if not folder_path:
            date = '%s/%s/%s' % (JalaliDate.today().day, JalaliDate.today().month, JalaliDate.today().year)
        else:
            date = '%s-%s-%s' % (JalaliDate.today().day, JalaliDate.today().month, JalaliDate.today().year)
    else:
        if not folder_path:
            date = '%s/%s/%s' % (datetime.datetime.today().date().day, datetime.datetime.today().date().month, datetime.datetime.today().date().year)
        else:
            date = '%s-%s-%s' % (datetime.datetime.today().date().day, datetime.datetime.today().date().month, datetime.datetime.today().date().year)

    if date[1] == '/':
        date = '0' + date
    if date[4] == '/':
        date = date[:3] + '0' + date[3:]
    return date


def get_time(folder_path=False):
    if not folder_path:
        time = str(datetime.datetime.today().hour) + ":" + str(datetime.datetime.today().minute) + ":" + str(datetime.datetime.today().second)
    else:
        time = str(datetime.datetime.today().hour) + "-" + str(datetime.datetime.today().minute) + "-" + str(datetime.datetime.today().second)
    return time


def get_datetime(persian=True, folder_path=True):
    date = get_date(persian=persian, folder_path=folder_path)
    time = get_time(folder_path=folder_path)

    return date + "-" + time



if __name__ == "__main__":
    print(get_datetime(persian=False))
    