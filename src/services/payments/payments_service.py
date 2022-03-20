# -*- coding: utf-8 -*-

# External libraries
from os import sys

# Local libraries
from src.services.payments.formatter_service import format_payments


def get_payments_2(days_worked):
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
        for x in days_worked["formatted_hours"]:
            if x in payment_calendar:
                for amount in range(days_worked["formatted_hours"][x]["hours_worked"]):
                    hour = days_worked["formatted_hours"][x]["start"] + (amount * 100)
                    for pay in payment_calendar[x]:
                        if pay["start"] < pay["end"] and hour >= pay["start"] and hour <= pay["end"]:
                            total = total + pay["pay"]
                        elif pay["start"] > pay["end"] and hour >= pay["start"] and (hour <= pay["end"] or hour <= 12359):
                            total = total + pay["pay"]

        return total

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + ", payments: get_payments - LINE: " + str(exc_tb.tb_lineno))
        return 0




