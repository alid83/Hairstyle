from khayyam import JalaliDate

# تبدیل تاریخ میلادی به شمسی
def to_jalali(date):
    return JalaliDate(date).strftime('%Y/%m/%d')