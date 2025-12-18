from flask import Blueprint, request, jsonify, redirect
from datetime import datetime
from models import ShortURL
from utils.validators import is_valid_url
from services.url_service import create_short_url, process_redirect

url_bp = Blueprint("url_bp", __name__)

@url_bp.route("/api/shorten", methods=["POST"])
def shorten_url():
    data = request.get_json()
    original_url = data.get("url")

    if not original_url or not is_valid_url(original_url):
        return jsonify({"error": "Invalid URL"}), 400

    expiry_days = data.get("expiry_days")
    url = create_short_url(original_url, expiry_days)

    return jsonify({"short_code": url.short_code}), 201


@url_bp.route("/api/<string:code>", methods=["GET"])
def redirect_url(code):
    url = ShortURL.query.filter_by(short_code=code).first()

    if not url or not url.is_active:
        return jsonify({"error": "URL not found"}), 404

    if url.expires_at and datetime.utcnow() > url.expires_at:
        url.is_active = False
        return jsonify({"error": "URL expired"}), 410

    process_redirect(url)
    return redirect(url.original_url, code=302)


@url_bp.route("/api/stats/<string:code>", methods=["GET"])
def get_stats(code):
    url = ShortURL.query.filter_by(short_code=code).first()

    if not url:
        return jsonify({"error": "URL not found"}), 404

    return jsonify({
        "original_url": url.original_url,
        "click_count": url.click_count,
        "created_at": url.created_at,
        "last_accessed_at": url.last_accessed_at,
        "is_active": url.is_active
    }), 200
