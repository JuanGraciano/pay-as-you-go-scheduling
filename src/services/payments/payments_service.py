# -*- coding: utf-8 -*-

# External libraries
from os import sys

# Local libraries
from src.services.payments.formatter_service import format_payments


def get_payments_2(days_worked):
    """
    Create the query to obtain information from users
    Parameters
    ----------
    gads_client: obj
        Google Ads client instance
    Returns
    ----------
    results: dataframe
        Dataframe with customer search results
    """
    # days_worked = {
    #         "name": "RENE",
    #         "hours": ["MO10:00-12:00", "TU10:00-12:00", "TH01:00-03:00", "SA14:00-18:00", "SU20:00-21:00"],
    #         "formatted_hours":{
    #             "monday":{"start": 11000, "end": 11200, "hours_worked": 2},
    #             "tuesday":{"start": 11000, "end": 11200, "hours_worked": 2},
    #             "thursday":{"start": 10100, "end": 10300, "hours_worked": 2},
    #             "saturday":{"start": 11400, "end": 11800, "hours_worked": 4},
    #             "sunday":{"start": 12000, "end": 12100, "hours_worked": 1},
    #         }
    #     }
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




