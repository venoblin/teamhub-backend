from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.bug import get_all_bugs, post_bug, get_single_bug, delete_single_bug, patch_single_bug

class Bugs(Resource):
    def get(self):
        return handle_request(request, get_all_bugs)
    
    def post(self):
        return handle_request(request, post_bug)
    
class SingleBug(Resource):
    def get(self, id):
        return handle_request(request, lambda: get_single_bug(id))
    
    def delete(self, id):
        return handle_request(request, lambda: delete_single_bug(id))
    
    def patch(self, id):
        return handle_request(request, lambda: patch_single_bug(id))