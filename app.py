from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# インメモリの簡易ランキング（必要に応じてデータベースに拡張可能）
leaderboard_data = [
    {"name": "PILOT_01", "rank": "👑🌈 コズミック神ランク", "score": 150000, "kills": 350},
    {"name": "CYBER_ACE", "rank": "💎 ダイヤモンドランク", "score": 85000, "kills": 210},
    {"name": "NEON_GHOST", "rank": "🥇 ゴールドランク", "score": 42000, "kills": 120}
]

@app.route("/")
@app.route("/home")
@app.route("/game")
@app.route("/shop")
@app.route("/ranking")
@app.route("/settings")
def index():
    return render_template("index.html")

@app.route("/api/ranking", methods=["GET", "POST"])
def ranking():
    global leaderboard_data
    if request.method == "POST":
        data = request.json
        if data:
            # スコアリストに追加してソート・上位10件を保持
            leaderboard_data.append({
                "name": data.get("name", "PILOT"),
                "rank": data.get("rank", "🔰 ルーキーランク"),
                "score": data.get("score", 0),
                "kills": data.get("kills", 0)
            })
            leaderboard_data.sort(key=lambda x: x["score"], reverse=True)
            leaderboard_data = leaderboard_data[:10]
        return jsonify({"success": True, "leaderboard": leaderboard_data})
    
    return jsonify({"leaderboard": leaderboard_data})

if __name__ == "__main__":
    app.run(debug=True)
