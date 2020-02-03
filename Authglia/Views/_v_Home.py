from flask import request, render_template, url_for
from flask import redirect, session, jsonify

from Authglia import app
from Authglia.Model._m_Home import _m_Home


@app.route("/", methods=["GET"])
def _v_home():
    if request.method == "GET":
        to_return = _m_Home().get_home()
        return render_template(template_name_or_list="Home.html", to_return=to_return)


@app.route("/api", methods=["GET"])
@app.route("/api/", methods=["GET"])
def _v_home_api():
    if request.method == "GET":
        to_return = _m_Home().get_home()
        return jsonify(to_return)



