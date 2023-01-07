import json
import logging


def getAuthorbook(mydb,req_data):
    sql = """SELECT author,COUNT(title) FROM bookslist GROUP BY author= %s """
    input_data = (req_data.get("author"))
    cursor = mydb.cursor(buffered =True, dictionary=True)
    cursor.execute(sql, input_data)
    mydb.commit()
    results = json.dumps(cursor.fetchall())
    cursor.close()
    logging.warning(results)
    return results