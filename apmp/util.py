from bs4 import BeautifulSoup
from datetime import datetime, timedelta
from apmp.CONSTANTS import SCHEDULE_TYPES, MONTHLY_AMORTIZATION

def modify_html_code(html_code):
    soup = BeautifulSoup(html_code, features='html.parser')

    for x in soup.find_all('h3'):
        x.attrs =  {'class': 'd-flex pt-2 pb-2 ps-4', 'style': 'background-color: #546B62; color: white;'}

    for x in soup.find_all('ul'):
        x.attrs = {'style': 'font-size: 16px; font-weight: 500; color: #454545', 'class': 'ms-5'}
    
    for x in soup.find_all('ol'):
        x.attrs = {'style': 'font-size: 16px; font-weight: 500; color: #454545', 'class': 'ms-5'}
    
    for x in soup.find_all('p'):
        x.attrs = {'style': 'font-size: 18px; color: #454545; text-indent:4%', 'align' : 'justify', 'class': 'ms-5 mt-4'}

    return soup


def generate_payment_schedule(date_start, schedule_type, num_months):
    schedule = list()
    date_to_pay = str(date_start).split(' ')[0]
    s = Schedule(month_number=1, date_to_pay=date_to_pay)

    schedule.append(s.get())

    if schedule_type == SCHEDULE_TYPES.EVERY_FIRST_DAY_OF_MONTH:
        for month_num in range(2, num_months + 1):
            date_start = date_start.replace(day=1)

            # add 32 days to the input datetime
            date_start += timedelta(days=32)

            # replace day number with 1
            res = date_start.replace(day=1)

            date_to_pay = str(res).split(' ')[0]
            s = Schedule(month_number=month_num, date_to_pay=date_to_pay)
            schedule.append(s.get())

            date_start = res

    if schedule_type == SCHEDULE_TYPES.EVERY_LAST_DAY_OF_MONTH:
        for month_num in range(2, num_months + 1):
            date_start = date_start.replace(day=1)
            date_start += timedelta(days=32)

            # The day 28 exists in every month. 4 days later, it's always next month
            next_month = date_start.replace(day=28) + timedelta(days=4)
            # subtracting the number of the current day brings us back one month
           
            date_to_pay = str(next_month - timedelta(days=next_month.day)).split(' ')[0]
            s = Schedule(month_number=month_num, date_to_pay=date_to_pay)

            schedule.append(s.get())

    return {"SCHEDULE" : schedule }

class Schedule():
    def __init__(self, month_number, date_to_pay):
        self.month_number = month_number
        self.date_to_pay = date_to_pay
        self.status = MONTHLY_AMORTIZATION.NOT_PAID
        self.amount_paid = None

    def get(self):
        return {
            "MONTH_NUMBER" : self.month_number,
            "DATE_TO_PAY" : self.date_to_pay,
            "STATUS" : self.status,
            "AMOUNT_PAID" : self.amount_paid
        }

# print(generate_payment_schedule(datetime(month=2, day=22, year=2023), SCHEDULE_TYPES.EVERY_LAST_DAY_OF_MONTH, 12))