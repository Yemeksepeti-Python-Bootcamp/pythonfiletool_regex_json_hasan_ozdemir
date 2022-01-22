"""
This script is created to manage helper methods
@Hasan Özdemir 01/21/2022
"""

from argparse import ArgumentParser
from datetime import datetime
from sys import argv


class HelperDb:

    def __init__(self) -> None:
        """
        This constructor is created to get named command line args.
        return : None
        """
        # initialize Argument parser

        parser = ArgumentParser()
        # prepare named arguments
        parser.add_argument('--file', help='Json file path', type=str)
        parser.add_argument('--db', help='Database file path', type=str)
        # get the named command line arguments
        self.json_path = parser.parse_args().file
        self.db_path = parser.parse_args().db

    def time_formatting(self) -> str:
        """
        This method is created to format datetime for yyyy_dd_mm format
        :return: <str> formatted datetime
        """
        now = datetime.now()
        date_time = str(now.strftime("%Y_%d_%m"))
        return date_time

    def connection_str(self, table_name: str) -> str:
        """
        This method is created to provide create table sql dialect
        :param table_name: <str> table name
        :return: <str> table sql dialect
        """
        # create table dialect
        create_table_str = f"""
        CREATE TABLE IF NOT EXISTS {table_name}(
         id int primary key(id),
         username varchar(25) not null,
         p_name varchar(25) not null,
         p_b_year varchar(25) not null,
         p_b_month varchar(25) not null,
         p_b_day varchar(25) not null,
         p_address varchar(150) not null,
         p_l_lat varchar(25) not null
         p_l_long varchar(25) not null,
         api_key varchar(100) not null
        )
        """
        return create_table_str


if __name__ == '__main__':
    help_obj = HelperDb()
    help_obj.time_formatting()
