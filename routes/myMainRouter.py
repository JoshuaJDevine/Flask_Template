from flask import Blueprint


bp = Blueprint('myBluePrintName', __name__, url_prefix="")


@bp.route('/')
def index():
    return "Flask Template"

@bp.route('/testRoute')
def testRoute():
    return "Test Route"