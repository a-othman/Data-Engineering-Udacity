import os
import glob
import psycopg2
import pandas as pd
from sql_queries import *


def process_song_file(cur, filepath):
    """ingesting and transformong data from JSPON to Pandas DF
    
    Args:
        cur: cusor of psycopg2.
        filepath: json log file path.
    """
         

def process_log_file(cur, filepath):
    """Ingesting and transforming songs data from JSOS format into Pandas DFs
    
    Args:
        cur: cusor of psycopg2.
        filepath: json log file path
    """


def process_data(cur, conn, filepath, func):
    """Processes JSON files for a data directory path.
    
    Valid function values can be 'process_song_file' or
    'process_log_file'.
    
    Args:
        cur: cusor of psycopg2
        conn: A database connection of psycopg2
        filepath: json data file path
        func: The function to invoke 
    """


def main():


if __name__ == "__main__":
    main()