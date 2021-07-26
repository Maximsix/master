from datetime import datetime, timedelta

def day_week_ago() :
    week_ago_from_now = timedelta(days=-7) + datetime.now()
    return week_ago_from_now.strftime("Month: %B\nDay: %d \nYear: %Y")




if __name__ == '__main__':
    print(day_week_ago())