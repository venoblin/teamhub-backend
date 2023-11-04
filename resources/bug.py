from flask_restful import Resource
from flask import request
from middleware import verify_auth
from controllers.bug import get_all_bugs, post_bug, get_single_bug, delete_single_bug, patch_single_bug

class Bugs(Resource):
    def get(self):
        return verify_auth(request, get_all_bugs)
    
    def post(self):
        return verify_auth(request, post_bug)
    
class SingleBug(Resource):
    def get(self, id):
        return verify_auth(request, lambda: get_single_bug(id))
    
    def delete(self, id):
        return verify_auth(request, lambda: delete_single_bug(id))
    
    def patch(self, id):
        return verify_auth(request, lambda: patch_single_bug(id))