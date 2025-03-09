from flask import Flask, render_template, send_from_directory, jsonify
import os
import random

app = Flask(__name__)
MUSIC_FOLDER = "static/music"


@app.route("/")
def index():
    # Lade alle Musikdateien im Ordner und sortiere nach Kategorien
    categories = {
        "ass_angriff": [],
        "block": [],
        "gegner": [],
        "sonstiges": []
    }

    all_songs = []

    for f in os.listdir(MUSIC_FOLDER):
        if f.endswith((".mp3", ".wav", ".ogg")):
            icon = (
                "⚡" if "HIT" in f.upper() or "ACE" in f.upper()
                else "✋✋" if "BLOCK" in f.upper()
                else "🏐" if "OPP" in f.upper()
                else ""
            )
            clean_name = (
                f.replace("_BLOCK", "")
                .replace("_HIT", "")
                .replace("_ACE", "")
                .replace("_OPP", "")
                .replace(".mp3", "")
                .strip()
            )
            song_data = {"name": f, "display_name": clean_name, "icon": icon}
            all_songs.append(song_data)

            # Einsortieren in die richtige Kategorie
            if "HIT" in f.upper() or "ACE" in f.upper():
                categories["ass_angriff"].append(song_data)
            elif "BLOCK" in f.upper():
                categories["block"].append(song_data)
            elif "OPP" in f.upper():
                categories["gegner"].append(song_data)
            else:
                categories["sonstiges"].append(song_data)

    return render_template(
        "index.html",
        categories=categories,
        favicon="🎵",
        timeout_song="Timeout.mp3",
        walkon_song="Walk-On.mp3",
        volume=1.0,
        add_separator=True,
    )


@app.route("/music/<filename>")
def get_music(filename):
    return send_from_directory(MUSIC_FOLDER, filename)

if __name__ == "__main__":
    app.run(debug=True)
