# -*- coding: utf-8 -*-

from os import sys

def read(file_path, file_name):
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
    try:
        with open("{}/{}".format(file_path, file_name)) as f:
            lines = f.readlines()
            return lines
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        print(str(e) + " read_files: read - LINE: " + str(exc_tb.tb_lineno))
        return ""

