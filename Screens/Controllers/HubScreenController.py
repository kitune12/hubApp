from flask import Blueprint, render_template

# <summary>
# Hub画面制御クラス
# </summary>
class HubScreenController:
    # <summary>
    # コンストラクタ
    # <param name="self">自身のクラスインスタンス</param>
    # <param name="app">Flaskアプリオブジェクト</param>
    # <param name="self">HubModelクラスインスタンス</param>
    # </summary>
    def __init__(self, app, Hub_model):
        self.blueprint = Blueprint("hub", __name__, url_prefix="/hub")
        self.Hub_model = Hub_model
        self._register_routes()

    # <summary>
    # 画面のルート処理
    # <param name="self">自身のクラスインスタンス</param>
    # </summary>
    def _register_routes(self):
        @self.blueprint.route("/")
        def hub_home():
            data = self.Hub_model.get_data()
            return render_template("HubScreen.html", data=data)