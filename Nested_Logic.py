import datetime


def calculate_fine(str_date_returned: str, str_date_due: str):
    arr_date_returned = str_date_returned.split(" ")
    arr_date_due = str_date_due.split(" ")
    date_returned = datetime.datetime(int(arr_date_returned[-1]), int(arr_date_returned[1]), int(arr_date_returned[0]))
    date_due = datetime.datetime(int(arr_date_due[-1]), int(arr_date_due[1]), int(arr_date_due[0]))
    fine = 0
    if date_returned < date_due:
        fine = 0
    elif date_returned > date_due:
        if date_returned.month == date_due.month and date_returned.year == date_due.year:
            fine = 15 * (date_returned.day - date_due.day)
        elif date_returned.month > date_due.month and date_returned.year == date_due.year:
            fine = 500 * (date_returned.month - date_due.month)
        elif date_returned.year > date_due.year:
            fine = 10000
    return fine


if __name__ == "__main__":
    str_date_returned = input()
    str_date_due = input()
    print(calculate_fine(str_date_returned, str_date_due))
