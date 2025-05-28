from flask import Blueprint, render_template

# <summary>
# Admin画面制御クラス
# </summary>
class AdminScreenController:
    def __init__(self,app, admin_model):
        self.blueprint = Blueprint("admin", __name__, url_prefix="/admin")
        self.admin_model = admin_model
        self._register_routes()

    def _register_routes(self):
        @self.blueprint.route("/")
        def admin_home():
            data = self.admin_model.get_data()
            return render_template("AdminScreen.html", data=data)