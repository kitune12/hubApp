# Mainfunction/MainFunction.py
from Screens.Controllers.HubScreenController import HubScreenController
from Screens.Controllers.AdminScreenController import AdminScreenController
from MainFunction.Models.Admin_model import AdminModel
from MainFunction.Models.Hub_model import HubModel

# <summary>
# メイン制御クラス
# </summary>
class MainFunction:

    # <summary>
    # コンストラクタ
    # <param name="self">自身のクラスインスタンス</param>
    # </summary>
    def __init__(self, app):
        self.app = app
        # モデル初期化
        self.Hub_model = HubModel()
        self.admin_model = AdminModel()

        # コントローラー初期化にモデルを注入（依存注入）
        self.hub_controller = HubScreenController(app, self.Hub_model)
        self.admin_controller = AdminScreenController(app, self.admin_model)

        # 各ControllerのBlueprintを初期化・登録
        # 	/hub/... にアクセスされたとき、HubScreenController の定義したルートに処理を渡す
        self.app.register_blueprint(self.hub_controller.blueprint)
        # 	/admin/... にアクセスされたとき、AdminScreenController に処理を渡す
        self.app.register_blueprint(self.admin_controller.blueprint)





