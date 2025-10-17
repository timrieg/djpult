from flask import Flask, render_template, send_from_directory, jsonify
import os

app = Flask(__name__)
MUSIC_FOLDER = "static/music"

timeout_song_name = "Timeout.mp3"
walkon_song_name = "Walk-On.mp3"
long_song_1_name = "Timeout.mp3"
long_song_2_name = "Timeout.mp3"


@app.route("/")
def index():
    # Lade alle Musikdateien im Ordner und sortiere nach Kategorien
    categories = {
        "ass_angriff": [],
        "block": [],
        "gegner": [],
        "sonstiges": [],
        "spass": [],
    }

    all_songs = []

    for f in os.listdir(MUSIC_FOLDER):
        if f.endswith((".mp3", ".wav", ".ogg")):
            icon = (
                "⚡"
                if "HIT" in f.upper() or "ACE" in f.upper()
                else (
                    "✋✋"
                    if "BLOCK" in f.upper()
                    else (
                        "🏐🏐"
                        if "OPP" in f.upper()
                        else "😂😂" if "FUN" in f.upper() else "🎉🎉"
                    )
                )
            )
            clean_name = (
                f.replace("_BLOCK", "")
                .replace("_HIT", "")
                .replace("_ACE", "")
                .replace("_OPP", "")
                .replace("_FUN", "")
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
            elif "FUN" in f.upper():
                categories["spass"].append(song_data)
            else:
                categories["sonstiges"].append(song_data)

    long_song_1_data = {
        "name": long_song_1_name,
        "display_name": "Pause: " + long_song_1_name.replace(".mp3", ""),
        "icon": "🎵",
    }
    long_song_2_data = {
        "name": long_song_2_name,
        "display_name": "Pause: " + long_song_2_name.replace(".mp3", ""),
        "icon": "🎵",
    }

    return render_template(
        "index.html",
        categories=categories,
        favicon="🎵",
        timeout_song=timeout_song_name,
        walkon_song=walkon_song_name,
        long_song_1=long_song_1_data,
        long_song_2=long_song_2_data,
        volume=1.0,
        add_separator=True,
    )


@app.route("/music/<filename>")
def get_music(filename):
    return send_from_directory(MUSIC_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)
