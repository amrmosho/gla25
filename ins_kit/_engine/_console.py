from flask import abort
from ins_kit.ins_parent import ins_parent
"""
Error 505	HTTP version not supported	Upgrade to a compatible http version
Error 504	The server, acting as a gateway or proxy, did not receive a timely response from the upstream server. This problem is usually due to a very slow upstream server.	Optimize the performance of the upstream server.
Error 503	Server unavailable	Bugs in plugins and the .htaccess file are usually the usual suspects
Error 502	Unable to access a page	Clear cache and test by disabling firewalls
Error 500	Internal server error	Many scenarios but usually related to the .htaccess file
Error 429	Too many requests in a given period	Implement request limits and rate handling
Error 408	The server timed out waiting for your request	Optimize the request to be faster
Error 405	The HTTP method used is not allowed for the requested resource	Verify that the HTTP method used in the request is allowed for the resource.
Error 404	Page not found	Check the permanent links
Error 403	No permission to access	Clear cache and test by disabling firewalls
Error 401	Request requires authentication	You will need to unlock access to that URL
Error 400	Invalid request. Usually due to problems in the URL such as strange characters	Check URL composition
"""


class Console(ins_parent):

    def geterror(self, type, code, error):
        g = self.ins._server._get()
        #if "debug" not in g:
        
        #    error = ""
       # else:
        error = f"<br/><br/> >> {error}"
        error = {
          
            "website": {
                "404": {
                    "code": 404,
                    "title": "Page Not Found",
                    "message": "The page you requested could not be found. Please check the URL and try again."
                },
                "500": {
                    "code": 500,
                    "title": "Internal Server Error",
                    "message": "There was a problem with the server. Please try again later."
                },
                "403": {
                    "code": 403,
                    "title": "Forbidden",
                    "message": "You do not have permission to access this page."
                },
                "401": {
                    "code": 401,
                    "title": "Unauthorized",
                    "message": "Authentication is required to access this page."
                },
                "502": {
                    "code": 502,
                    "title": "Bad Gateway",
                    "message": "The server received an invalid response from the upstream server."
                },
                "503": {
                    "code": 503,
                    "title": "Service Unavailable",
                    "message": "The server is currently unavailable due to maintenance or overload."
                }
            },
            "db": {
                "db_connection_failed": {
                    "code": 1001,
                    "title": "Database Connection Failed",
                    "message": f"Unable to connect to the database. Please check the database server or credentials. {error}"
                },
                "db_query_failed": {
                    "code": 1002,
                    "title": "Database Query Failed",
                    "message": f"There was an error executing the query. Please check the query syntax.  {error}"
                },
                "db_record_not_found": {
                    "code": 1003,
                    "title": "Record Not Found",
                    "message":f"The requested record could not be found in the database. {error}"
                },
                "db_duplicate_entry": {
                    "code": 1004,
                    "title": "Duplicate Entry",
                    "message": "A record with the same data already exists in the database."
                },
                "db_timeout": {
                    "code": 1005,
                    "title": "Database Timeout",
                    "message": "The database query timed out. Please try again later."
                }
            },
            "file": {
                "file_not_found": {
                    "code": 2001,
                    "title": "File Not Found",
                    "message": "The requested file could not be found on the server."
                },
                "file_permission_denied": {
                    "code": 2002,
                    "title": "Permission Denied",
                    "message": "You do not have permission to access or modify the file."
                },
                "file_read_error": {
                    "code": 2003,
                    "title": "File Read Error",
                    "message": "There was an error reading the file. It might be corrupted or missing."
                },
                "file_write_error": {
                    "code": 2004,
                    "title": "File Write Error",
                    "message": "There was an error writing data to the file."
                },
                "file_upload_failed": {
                    "code": 2005,
                    "title": "File Upload Failed",
                    "message": "The file upload failed due to network or server issues."
                }
            },
            "auth": {
                "incorrect_credentials": {
                    "code": 3001,
                    "title": "Incorrect Credentials",
                    "message": "The username or password you entered is incorrect."
                },
                "account_locked": {
                    "code": 3002,
                    "title": "Account Locked",
                    "message": "Your account has been locked due to multiple failed login attempts."
                },
                "session_expired": {
                    "code": 3003,
                    "title": "Session Expired",
                    "message": "Your session has expired. Please log in again."
                }
            },
            "validation": {
                "empty_field": {
                    "code": 4001,
                    "title": "Empty Field",
                    "message": "This field cannot be empty. Please provide a value."
                },
                "invalid_email": {
                    "code": 4002,
                    "title": "Invalid Email Format",
                    "message": "Please enter a valid email address."
                },
                "password_mismatch": {
                    "code": 4003,
                    "title": "Password Mismatch",
                    "message": "The passwords you entered do not match."
                },
                "invalid_input": {
                    "code": 4004,
                    "title": "Invalid Input",
                    "message": "The data you entered is not valid. Please check and try again."
                }
            }
        }

        category_errors = error.get(type)
        if category_errors:
            error = category_errors.get(code)
            if error:
                return error

        return {
            "code": 500,
            "title": "Internal Server Error",
            "message": "There was a problem with the server. Please try again later."
        }

    def error(self, type="website",  code="404", error=""):
        d = self.geterror(type, code, error)
        abort(500, {"title": d["title"], "msg":  d["message"]})
