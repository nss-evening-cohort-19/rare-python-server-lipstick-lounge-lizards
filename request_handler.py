# pylint: disable=W0622
"""main"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from views import (create_user, login_user, get_all_posts, get_single_post, create_post, get_all_categories, get_all_comments, get_single_comment, create_comment, delete_comment, update_comment, get_all_reactions,get_single_reaction, create_reaction,update_reaction,delete_reaction, get_single_user, get_all_users)
import json


class HandleRequests(BaseHTTPRequestHandler):
    """Handles the requests to this server"""

    def parse_url(self):
        """Parse the url into the resource and id"""
        path_params = self.path.split('/')
        resource = path_params[1]
        if '?' in resource:
            param = resource.split('?')[1]
            resource = resource.split('?')[0]
            pair = param.split('=')
            key = pair[0]
            value = pair[1]
            return (resource, key, value)
        else:
            id = None
            try:
                id = int(path_params[2])
            except (IndexError, ValueError):
                pass
            return (resource, id)

    def _set_headers(self, status):
        """Sets the status code, Content-Type and Access-Control-Allow-Origin
        headers on the response

        Args:
            status (number): the status code to return to the front end
        """
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()

    def do_OPTIONS(self):
        """Sets the OPTIONS headers
        """
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        """Handle Get requests to the server"""
        self._set_headers(200)
        response = {}

        parsed = self.parse_url()

        if '?' not in self.path:
            ( resource, id ) = parsed

            if resource == "posts":
                if id is not None:
                    response = f"{get_single_post(id)}"
                else:
                    response = f"{get_all_posts()}"
            elif resource == "users":
                if id is not None:
                    response = f"{get_single_user(id)}"
                else:
                    response = f"{get_all_users()}"
            elif resource == "comments":
                if id is not None:
                    response = f"{get_single_comment(id)}"
                else:
                    response = f"{get_all_comments()}"
            elif resource == "categories":
                if id is not None:
                    response = f"{get_single_category(id)}"
                else:
                    response = f"{get_all_categories()}"
            elif resource == "reactions":
                if id is not None:
                    response = f"{get_single_reaction(id)}"
                else:
                    response = f"{get_all_reactions()}"

        self.wfile.write(response.encode())

    def do_POST(self):
        """Make a post request to the server"""
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = json.loads(self.rfile.read(content_len))
        response = ''
        (resource, id)= self.parse_url()
        if resource == 'login':
            response = login_user(post_body)
        if resource == 'register':
            response = create_user(post_body)
        if resource == 'posts':
            response = create_post(post_body)
        if resource == 'comments':
            response = create_comment(post_body)
        if resource == 'categories':
            new_category = create_category(post_body)
            self.wfile.write(f'{new_category}'.encode())
        if resource == 'reactions':
            response = create_reaction(post_body)

        self.wfile.write(response.encode())

    def do_PUT(self):
        """Handles PUT requests to the server"""
        self._set_headers(204)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        post_body = json.loads(post_body)

        (resource, id) = self.parse_url()
        success = False

        if resource == "posts":
            update_post(id, post_body)
        if resource == "users":
            update_user(id, post_body)
        if resource == "comments":
            update_comment(id, post_body)
        if resource == "categories":
            update_category(id, post_body)
        if resource == "reactions":
            update_reaction(id, post_body)
        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        if success:
            self._set_headers(204)
        else:
            self._set_headers(404)

        self.wfile.write("".encode())

    def do_DELETE(self):
        """Handle DELETE Requests"""
        self._set_headers(204)

        (resource, id) = self.parse_url()

        if resource == "posts":
            delete_post(id)
        if resource == "users":
            delete_user(id)
        if resource == "comments":
            delete_comment(id)
        if resource == "categories":
            delete_category(id)
        if resource == "reactions":
            delete_reaction(id)

        self.wfile.write("".encode())


def main():
    """Starts the server on port 8088 using the HandleRequests class
    """
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
