from flask import Blueprint


bp = Blueprint('tracker', __name__, url_prefix="")


@bp.route('/')
def index():
    return "JD's awesome template for an initially confusing (but ultimately easier to use than express) framework"
