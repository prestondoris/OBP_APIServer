import json
from server import get_model
from flask import current_app, Blueprint, request

crud = Blueprint('income_crud', __name__)

@crud.route('/')
def main():
    return 

