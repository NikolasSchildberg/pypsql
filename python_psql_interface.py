# imports
import psycopg2         # postgres connection and pandas
import pandas as pd

# path to database config file in working directory
db_config_path = './db_connection'

# creating a connection to the database (a database session)
conn = psycopg2.connect(open(db_config_path).read())

# creates a cursor: the object used to interface with the database
cur = conn.cursor()

# shortcut function to run given query and return all query results
def q(query_str: str, df=True, index_col='id'):
    """Executes given query (a string) using psycopg2 connection.cursor object.

    Returns:
    Fetches all entries from query result, and returns data as a pandas Dataframe, unless
    df = False is passed as argument, in which case returns a list.

    The parameter index_col is used to set the column to be used as DataFrame index.
    Default is index_col='id'.

    Keyword arguments:
    query -- (required)
    df -- whether or not to return query result as a pandas DataFrame (default True)
    index_col -- a string with a name of a column to be used as index of the resulting DataFrame (default 'id')
    """
    cur.execute(query_str)
    query_result = cur.fetchall()
    if df:
        return(pd.DataFrame(query_result, columns=[col.name for col in cur.description]).set_index(index_col))
    return(cur.fetchall())


print("Success! Now you can interface with PostgreSQL using the function \"q()\".")
