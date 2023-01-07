from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector
import json
from read import read
from create import create
from update import update
from delete import delete
from readOne import readOne
from bookByauthor import getAuthorbook

def db_connect():
    return mysql.connector.connect(host = "localhost", user = "root", password = "", database = "book")


class GetHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=='/read':
            try:
                if db_connect().is_connected():
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin','*')
                    self.end_headers()
                    # call read function from read file
                    self.wfile.write(bytes(read(db_connect()), "utf-8"))

            except mysql.connector.Error as error:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connected:", "utf-8"))
        elif self.path=='/readone':
            try:
                if db_connect().is_connected():
                    content_length = int(self.headers.get("Content-Length"))
                    body = self.rfile.read(content_length)
                    req_data = json.loads(body)
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    # call getAuthorbook function from create file
                    self.wfile.write(bytes(getAuthorbook(db_connect(), req_data), "utf-8"))
            except mysql.connector.Error as error:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connecteddd:", "utf-8"))
        elif self.path=='/readAuthorbook':
            try:
                if db_connect().is_connected():
                    content_length = int(self.headers.get("Content-Length"))
                    body = self.rfile.read(content_length)
                    req_data = json.loads(body)
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    # call readone function from create file
                    self.wfile.write(bytes(readOne(db_connect(), req_data), "utf-8"))
            except mysql.connector.Error as error:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connecteddd:", "utf-8"))

    def do_POST(self):
        if self.path=='/create':
            try:
                if db_connect().is_connected():
                    content_length=int(self.headers.get("Content-Length"))
                    body = self.rfile.read(content_length)
                    req_data = json.loads(body)
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    # call create function from create file
                    self.wfile.write(bytes(create(db_connect(), req_data), "utf-8"))
            except mysql.connector.Error as error:
                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connected:", "utf-8"))
    def do_PUT(self):
        if self.path == '/update':

            try:
                if db_connect().is_connected():
                    content_length = int(self.headers.get("Content-Length"))
                    body = self.rfile.read(content_length)
                    req_data = json.loads(body)
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    # call update function from update file
                    self.wfile.write(bytes(update(db_connect(), req_data), "utf-8"))

            except mysql.connector.Error as error:

                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connected:", "utf-8"))
    def do_DELETE(self):
        if self.path=='/delete':
            try:
                if db_connect().is_connected():
                    content_length = int(self.headers.get("Content-Length"))
                    body = self.rfile.read(content_length)
                    req_data = json.loads(body)
                    self.send_response(200)
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    # call delete function from delete file
                    self.wfile.write(bytes(delete(db_connect(), req_data), "utf-8"))

            except mysql.connector.Error as error:

                self.send_response(200)
                self.end_headers()
                self.wfile.write(bytes("DB doesn't connected:", "utf-8"))

def main():
    httpd = HTTPServer(('localhost', 39046), GetHandler)
    print("Web server has been started")
    httpd.serve_forever()


if __name__ == "__main__":
    main()