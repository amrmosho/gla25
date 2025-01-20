from flask import  Blueprint
from ins_kit.ins import ins


area = "ajax"


ajax_bp = Blueprint(area, __name__)


@ajax_bp.route('/', defaults={'path': ''}, methods=['GET', 'POST'])
@ajax_bp.route('/<path:path>', methods=['GET', 'POST'])
def ajax(path):
 return ins._ajax._render(area,path)
