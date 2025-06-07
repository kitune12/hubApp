from flask import Blueprint, render_template, redirect, url_for

# <summary>
# Admin画面制御クラス
# </summary>
class AdminScreenController:
    # <summary>
    # コンストラクタ
    # <param name="self">自身のクラスインスタンス</param>
    # <param name="app">Flaskアプリオブジェクト</param>
    # <param name="self">AdminModelクラスインスタンス</param>
    # </summary>
    def __init__(self,app, admin_model):
        self.blueprint = Blueprint("admin", __name__, url_prefix="/admin")
        self.admin_model = admin_model
        self._register_routes()

    # <summary>
    # 画面のルート処理
    # <param name="self">自身のクラスインスタンス</param>
    # </summary>
    def _register_routes(self):
        @self.blueprint.route("/")
        def admin_home():
            # 仮の条件：管理画面は「アクセス禁止」状態
            is_admin_access_allowed = True
            
            # アクセス権があればAdmin画面に遷移
            if is_admin_access_allowed:
                data = self.admin_model.get_data()
                return render_template("AdminScreen.html", data=data)
            # アクセス権が無ければHub画面にリダイレクト
            else:
                return redirect(url_for("hub.hub_home")) 