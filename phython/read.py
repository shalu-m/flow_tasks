import json

def read(mydb):
    sql = """select * from bookslist order by id desc"""
    cursor = mydb.cursor(dictionary=True)
    cursor.execute(sql)
    results = json.dumps(cursor.fetchall())
    cursor.close()

    return results