def delete(mydb,req_data):
    sql = """DELETE from bookslist WHERE id = %s"""
    input_data = (req_data.get('id'))
    cursor = mydb.cursor()
    cursor.execute(sql, (input_data,))
    mydb.commit()
    cursor.close()
    return "Record deleted successfully"