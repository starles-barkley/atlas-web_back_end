#!/usr/bin/env python3
'''This module filters log messages'''
import re
from typing import List
import logging
import os
import mysql.connector
from mysql.connector.connection import MySQLConnection


PII_FIELDS = ('phone', 'name', 'ssn', 'password', 'email')


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """Format the log record with redactions
        """
        original_message = super().format(record)
        return filter_datum(self.fields,
                            self.REDACTION,
                            original_message,
                            self.SEPARATOR)


def filter_datum(fields: List[str],
                 redaction: str,
                 message: str,
                 separator: str) -> str:
    '''Obfuscates fields in a log message'''
    pattern: str = f"({'|'.join(fields)})=([^\\{separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)


def get_logger() -> logging.Logger:
    '''Returns a configured logger for user data'''
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(fields=PII_FIELDS))

    logger.addHandler(stream_handler)

    return logger


def get_db() -> MySQLConnection:
    '''Returns a connection to the MySQL database'''
    username = os.getenv('PERSONAL_DATA_DB_USERNAME', 'root')
    password = os.getenv('PERSONAL_DATA_DB_PASSWORD', '')
    host = os.getenv('PERSONAL_DATA_DB_HOST', 'localhost')
    database = os.getenv('PERSONAL_DATA_DB_NAME')

    return mysql.connector.connect(
        user=username,
        password=password,
        host=host,
        database=database
    )


def main() -> None:
    '''Main function that retrieves and logs user data from the database'''
    db_connection = get_db()
    cursor = db_connection.cursor()

    query = ("SELECT name, email, phone, ssn, password, ip, last_login, "
             "user_agent FROM users;")
    cursor.execute(query)

    logger = get_logger()

    for row in cursor.fetchall():
        message = (f"name={row[0]}; email={row[1]}; phone={row[2]}; "
                   f"ssn={row[3]}; password={row[4]}; ip={row[5]}; "
                   f"last_login={row[6]}; user_agent={row[7]};")
        logger.info(message)

    cursor.close()
    db_connection.close()


if __name__ == "__main__":
    main()
