# -*- coding: utf-8 -*-

# External libraries
from os import sys

# Local libraries
from src.services.payments.formatter_service import format_payments


def get_payments_by_day(day, days_worked, payment_calendar):
    """
    Compares the list of hours worked by the employee with the list of hourly pay rates 
    
    Parameters
    ----------
    day: string
        Day worked by employee
    days_worked: dict
        List of formatted hours worked by employee 
    payment_calendar: dict
        List of costs per hour
    
    Returns
    ----------
    total: number
        Amount to be paid to employee per day
    """
    try:
        total = 0
        for amount in range(days_worked["formatted_hours"][day]["hours_worked"]):
            hour = days_worked["formatted_hours"][day]["start"] + (amount * 100)
            for pay in payment_calendar[day]:
                if pay["start"] < pay["end"] and hour >= pay["start"] and hour <= pay["end"]:
                    total = total + pay["pay"]
                elif pay["start"] > pay["end"] and hour >= pay["start"] and (hour <= pay["end"] or hour <= 12359):
                    total = total + pay["pay"]
        return total
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + ", payments: get_payments - LINE: " + str(exc_tb.tb_lineno))
        return 0


def get_payments(days_worked):
    """
    Compares the list of hours worked by the employee with the list of hourly pay rates 
    
    Parameters
    ----------
    days_worked: dict
        List of formatted hours worked by employee 
    
    Returns
    ----------
    total: number
        Amount to be paid to employee
    """
    
    try:        
        if len(days_worked) <= 0:
            raise Exception("A full dictionary is expected") 
        
        payment_calendar = format_payments()
        total = 0
        for day in days_worked["formatted_hours"]:
            if day in payment_calendar:
                total = total + get_payments_by_day(day, days_worked, payment_calendar)

        return {"employee": days_worked["name"], "pay": total}

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + ", payments: get_payments - LINE: " + str(exc_tb.tb_lineno))
        return {"employee": "undefined", "pay": 0}




