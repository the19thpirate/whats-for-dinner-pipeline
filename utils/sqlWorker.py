from configurations import config
import psycopg2
import pandas as pd

def getMainConnection():

    con = psycopg2.connect(
        host = config.host,
        port = config.port,
        user = config.user,
        password = config.password
    )
    return con


def getLastRecords():

    db_connection = getMainConnection()
    query = """
    SELECT * FROM dinner_data
    ORDER BY id DESC
    LIMIT 5;
    """
    data = pd.read_sql(query, con = db_connection)
    db_connection.close()
    return data

def insertNewRecord(listOfValues):
    db_connection = getMainConnection()
    cursor = db_connection.cursor()
    query = f"""
    INSERT INTO dinner_data
    (
        id, primary_item, secondary_item, tertiary_item, meal_type, is_homecooked, date
    )
    VALUES
    {tuple(listOfValues)};
    """
    cursor.execute(query)
    db_connection.commit()
    db_connection.close()
    return "Successfully Inserted Record."

