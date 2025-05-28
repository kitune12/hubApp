from flask import Blueprint, render_template

# <summary>
# Hub画面制御クラス
# </summary>
class HubScreenController:
    def __init__(self, app, Hub_model):
        self.blueprint = Blueprint("hub", __name__, url_prefix="/hub")
        self.Hub_model = Hub_model
        self._register_routes()

    def _register_routes(self):
        @self.blueprint.route("/")
        def hub_home():
            data = self.Hub_model.get_data()
            return render_template("HubScreen.html", data=data)