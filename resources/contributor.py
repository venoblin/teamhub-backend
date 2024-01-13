from flask_restful import Resource
from flask import request
from middleware import handle_request
from controllers.contributor import get_all_contributors, post_contributor, get_single_contributor, delete_single_contributor, patch_single_contributor

class Contributors(Resource):
    def get(self):
        return handle_request(request, get_all_contributors)
    
    def post(self):
        return handle_request(request, post_contributor)
    
class SingleContributor(Resource):
    def get(self, id):
        return handle_request(request, lambda: get_single_contributor(id))
    
    def delete(self, id):
        return handle_request(request, lambda: delete_single_contributor(id))
    
    def patch(self, id):
        return handle_request(request, lambda: patch_single_contributor(id))