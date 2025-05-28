from flask import Blueprint, render_template, request, redirect, url_for, session


class SettingsScreenController:
    def __init__(self,app):
        self.blueprint = Blueprint("settings", __name__, url_prefix="/settings")
        self._register_routes()

    def _register_routes(self):
        @self.blueprint.route("/", methods=["GET", "POST"])
        def settings_home():
            if request.method == "POST":
                session["dark_mode"] = request.form.get("dark_mode") == "on"
                return redirect(url_for("hub.hub_home"))
            dark_mode = session.get("dark_mode", False)
            return render_template("SettingsScreen.html", dark_mode=dark_mode)