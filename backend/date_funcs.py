from persiantools.jdatetime import JalaliDate
import datetime

SHAMSI_DATE = False

def get_date(persian=SHAMSI_DATE, folder_path=False):
    """
    this function retrns current date, wheter in persian or miladi.

    Inputs:
        persian: a bolean value determining the foramt of date (in persian or miladi)
        folder_path: a boolean value determiningn if the date will be used as a folder name or not
    
    Returns:
        date: current date (in string)
    """

    # persian date
    if persian:
        # get day
        day = str(JalaliDate.today().day)
        if len(day)==1:
            day = '0' + day
        #
        # get month
        month = str(JalaliDate.today().month)
        if len(month)==1:
            month = '0' + month
        #
        # full date string
        if not folder_path:
            date = '%s/%s/%s' % (JalaliDate.today().year, month, day)
        else:
            date = '%s-%s-%s' % (JalaliDate.today().year, month, day)

    # miladi date
    else:
        # get day
        day = str(datetime.datetime.today().date().day)
        if len(day)==1:
            day = '0' + day
        #
        # get month
        month = str(datetime.datetime.today().date().month)
        if len(month)==1:
            month = '0' + month
        #
        # full date string
        if not folder_path:
            date = '%s/%s/%s' % (datetime.datetime.today().date().year, month, day)
        else:
            date = '%s-%s-%s' % (datetime.datetime.today().date().year, month, day)

    return date


def get_time(folder_path=False):
    """
    this functionn returns current time

    Inputs: 
        folder_path: a boolean value determiningn if the date will be used as a folder name or not
    
    Returns:
        time: current time (in string)
    """

    time = datetime.datetime.now()
    
    if not folder_path:
        time = str(time.strftime("%H:%M:%S"))
    else:
        time = str(time.strftime("%H-%M-%S"))
    
    return time


def get_datetime(persian=SHAMSI_DATE, folder_path=True,ret_list=False):
    """
    this function returns both curent date and time in wheater persian or miladi format

    Inputs:
        persian: a bolean value determining the foramt of date (in persian or miladi)
        folder_path: a boolean value determiningn if the date will be used as a folder name or not
    
    Returns:
        date and time: current date and time (in string)
    """
    
    date = get_date(persian=persian, folder_path=folder_path)
    time = get_time(folder_path=folder_path)

    if ret_list:
        return [date,time]
    else:
        return date + "-" + time


def get_n_month_days(month=1, persian=SHAMSI_DATE):
    if persian:
        if month <= 6:
            return 31
        else:
            return 30
    else:
        if month in [1, 3, 5, 7, 8, 10, 12]:
            return 31
        if month == 2:
            return 29
        return 30



def convert_date(date,ret_miladi=True):
    if ret_miladi:
        date = JalaliDate(int(date[0]),int(date[1]),int(date[2])).to_gregorian() 
        return date


def convert_get_time(time):

    time = datetime.time(int(time[0]),int(time[1]))

    return time



if __name__ == "__main__":
    
    print(get_datetime(folder_path=True)[:-3])

    