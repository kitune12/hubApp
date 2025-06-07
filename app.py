from flask import Flask, redirect
from MainFunction.MainFunction import MainFunction

def create_app():
    # Flaskアプリ初期化
    app = Flask(__name__, template_folder="Screens/Views", static_folder="Screens/Views/static")
    # セッション利用
    app.secret_key = "your_secret_key"

    # MainFunctionでコントローラー登録 & モデル管理
    main_function = MainFunction(app)

    # / にアクセスしたら /hub にリダイレクト
    @app.route("/")
    def index():
        return redirect("/hub")

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=5000, debug=True)