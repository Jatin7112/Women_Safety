
from flask import Flask, request, jsonify, render_template
from datetime import datetime
import os, csv, uuid
from werkzeug.utils import secure_filename

app = Flask(__name__, template_folder='templates')

# Directories
COMPLAINT_DIR = "complaint"
VIDEO_DIR = "complaint_video"

os.makedirs(COMPLAINT_DIR, exist_ok=True)
os.makedirs(VIDEO_DIR, exist_ok=True)

CSV_PATHS = {
    "instant": os.path.join(COMPLAINT_DIR, "instant_complaint.csv"),
    "anonymous": os.path.join(COMPLAINT_DIR, "anonymous_complaint.csv"),
    "direct": os.path.join(COMPLAINT_DIR, "direct_complaint.csv"),
}

CSV_HEADERS = {
    "instant": ["timestamp", "tracking_id", "phone", "description", "title", "category"],
    "anonymous": ["timestamp", "tracking_id", "title", "category", "description"],
    "direct": ["timestamp", "tracking_id", "name", "email", "phone", "title", "category", "description"],
}

def ensure_csv_header(csv_type):
    path = CSV_PATHS[csv_type]
    header = CSV_HEADERS[csv_type]
    if not os.path.exists(path) or os.path.getsize(path) == 0:
        with open(path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(header)

for complaint_type in CSV_HEADERS.keys():
    ensure_csv_header(complaint_type)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/route_finder")
def route_finder():
    return render_template("route_finder.html")

@app.route("/index.html")
def complaint_page():
    return render_template("index.html")

@app.route("/api/complaints", methods=["POST"])
def receive_complaint():
    try:
        complaint_type = request.form.get("type", "").lower()
        if complaint_type not in CSV_HEADERS:
            return jsonify({"success": False, "error": "Invalid complaint type."}), 400

        tracking_id = str(uuid.uuid4())
        timestamp = datetime.utcnow().isoformat() + "Z"

        # collect form data
        row_data = {"timestamp": timestamp, "tracking_id": tracking_id}
        for field in CSV_HEADERS[complaint_type]:
            if field not in ["timestamp", "tracking_id"]:
                row_data[field] = request.form.get(field, "").strip()

        if not row_data.get("description"):
            return jsonify({"success": False, "error": "Description is required."}), 400
        if complaint_type in ["instant", "direct"] and not row_data.get("phone"):
            return jsonify({"success": False, "error": "Phone number is required."}), 400

        # save CSV
        csv_path = CSV_PATHS[complaint_type]
        row_to_write = [row_data.get(field) for field in CSV_HEADERS[complaint_type]]
        with open(csv_path, mode="a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(row_to_write)

        # save video if uploaded
        if "video" in request.files:
            video = request.files["video"]
            if video and video.filename:
                ext = os.path.splitext(video.filename)[1]
                filename = secure_filename(tracking_id + ext)
                video.save(os.path.join(VIDEO_DIR, filename))

        return jsonify({"success": True, "tracking_id": tracking_id}), 201

    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"success": False, "error": "Server error"}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

