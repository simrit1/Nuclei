from flask import (
    Blueprint,
    Flask,
    Response,
    redirect,
    render_template,
    request,
    url_for,
)
from flask_admin.contrib.sqla import ModelView
from flask_login import login_required
from PIL import Image
from werkzeug.utils import secure_filename

from ..authentication.models import User
from ..compression_service.models import media_index
from ..extension_globals.admin import admin_instance
from ..extension_globals.database import db

admin_instance.add_view(ModelView(User, db.session))
admin_instance.add_view(ModelView(media_index, db.session))

admin_interface_blueprint = Blueprint(
    "admin_interface",
    __name__,
    url_prefix="/admin",
    static_folder="static",
    template_folder="templates",
    static_url_path="/admin/static",
)
