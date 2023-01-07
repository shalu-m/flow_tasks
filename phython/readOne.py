import json
import logging


def readOne(mydb,req_data):
    sql = """SELECT * FROM bookslist WHERE id= %s"""
    input_data = (req_data.get("id"))
    cursor = mydb.cursor(buffered =True, dictionary=True)
    cursor.execute(sql, input_data)
    mydb.commit()
    results = json.dumps(cursor.fetchall())
    cursor.close()
    logging.warning(results)
    return results