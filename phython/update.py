def update(mydb,req_data):
    sql = """UPDATE bookslist SET title = %s,author=%s,year=%s WHERE id = %s"""
    input_data = (req_data.get('title'),req_data.get('author'), req_data.get('year'),req_data.get('id'))
    cursor = mydb.cursor()
    cursor.execute(sql, input_data)
    mydb.commit()
    cursor.close()

    return "Record updated successfully"