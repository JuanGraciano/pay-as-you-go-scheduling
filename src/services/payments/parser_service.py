# -*- coding: utf-8 -*-

# External libraries
from os import sys

def parser_payments(string_data):
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
    # string_data = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
    try:
        split_name_hours = string_data.split("=")
        
        if len(split_name_hours) > 1:
            name_employee = string_data.split("=")[0]
            hours_worked = string_data.split("=")[1]
        else:
            raise Exception("""The expected structure is not found. The structure should be '{employee name}={hours worked}'""")

        hours_per_day = hours_worked.split(",")

        return {
            "name": name_employee,
            "hours": hours_per_day
        }
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + ", payments: parser_payments - LINE: " + str(exc_tb.tb_lineno))
        return {}

