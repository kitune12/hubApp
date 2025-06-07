import os
import json
from flask import Blueprint, render_template, request, session, jsonify, current_app

class HomeScreenController:
    def __init__(self, app, Home_model):
        self.blueprint = Blueprint("home", __name__, url_prefix="/home")
        self.Home_model = Home_model
        self._register_routes()

    def _register_routes(self):
        @self.blueprint.route("/")
        def home_home():
            data = self.Home_model.get_data()
            return render_template("HomeScreen.html", data=data)

        @self.blueprint.route("/news", methods=["GET"])
        def get_news():
            save_path = os.path.join(current_app.root_path, "Data", "news.json")
            print(f"【DEBUG】news.jsonの絶対パス: {save_path}")
            if os.path.exists(save_path):
                with open(save_path, "r", encoding="utf-8") as f:
                    news_data = json.load(f)
                print("【DEBUG】news.jsonの内容:", news_data)
                return jsonify(news_data)
            else:
                print("【DEBUG】news.jsonが存在しません")
                return jsonify([])

        @self.blueprint.route("/save_news", methods=["POST"])
        def save_news():
            try:
                new_item = request.get_json()
                title = new_item.get('title')
                date = new_item.get('date')
                url = new_item.get('url', "")  # ← もしキーがなければ""にする

                # titleとdateは必須、urlはオプション（空でもOK）
                if not (title and date):
                    return jsonify({"status": "error", "message": "Title and Date are required"}), 400

                save_path = os.path.join(current_app.root_path, "Data", "news.json")

                if os.path.exists(save_path):
                    with open(save_path, "r", encoding="utf-8") as f:
                        news_data = json.load(f)
                else:
                    news_data = []

                news_data.append({
                    "title": title,
                    "date": date,
                    "url": url  # 空文字列でもOKで保存
                })

                with open(save_path, "w", encoding="utf-8") as f:
                    json.dump(news_data, f, ensure_ascii=False, indent=4)

                print(f"【DEBUG】追加後のnews.json:", news_data)

                return jsonify({"status": "success"})
            except Exception as e:
                print(f"【ERROR】保存中エラー: {e}")
                return jsonify({"status": "error", "message": str(e)}), 500

        @self.blueprint.route("/delete_news", methods=["POST"])
        def delete_news():
            try:
                data = request.get_json()
                index_to_delete = data.get("index")
                save_path = os.path.join(current_app.root_path, "Data", "news.json")

                if os.path.exists(save_path):
                    with open(save_path, "r", encoding="utf-8") as f:
                        news_data = json.load(f)

                    if 0 <= index_to_delete < len(news_data):
                        deleted_item = news_data.pop(index_to_delete)

                        with open(save_path, "w", encoding="utf-8") as f:
                            json.dump(news_data, f, ensure_ascii=False, indent=4)

                        print(f"【DEBUG】削除したアイテム: {deleted_item}")
                        return jsonify({"status": "success"})
                    else:
                        return jsonify({"status": "error", "message": "Invalid index"}), 400
                else:
                    return jsonify({"status": "error", "message": "File not found"}), 404
            except Exception as e:
                print(f"【ERROR】削除中エラー: {e}")
                return jsonify({"status": "error", "message": str(e)}), 500
