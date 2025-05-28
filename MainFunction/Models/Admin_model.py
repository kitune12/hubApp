
# <summary>
# Admin画面ロジッククラス
# </summary>
class AdminModel:
    # <summary>
    # 画面に表示データを渡す
    # <param name="self">自身のクラスインスタンス</param>
    # </summary>
    def get_data(self):
        return {
            "title": "管理画面",
            "message": "こちらは管理者画面です。"
        }