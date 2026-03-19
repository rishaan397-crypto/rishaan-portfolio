from flask import Flask, render_template_string

app = Flask(__name__)

STYLE = """
<style>
body {
    margin: 0;
    font-family: monospace;
    background: #0a0a0a;
    color: #00ffe7;
    display: flex;
}

.sidebar {
    width: 220px;
    height: 100vh;
    background: black;
    padding: 20px;
    box-shadow: 0 0 20px #00ffe7;
}

.sidebar h2 {
    text-shadow: 0 0 10px #00ffe7;
}

.sidebar a {
    display: block;
    color: #00ffe7;
    text-decoration: none;
    margin: 15px 0;
}

.sidebar a:hover {
    color: white;
}

.content {
    flex: 1;
    padding: 40px;
}

h1 {
    text-shadow: 0 0 20px #00ffe7;
}

img {
    width: 300px;
    border-radius: 10px;
    margin: 10px;
    box-shadow: 0 0 20px #00ffe7;
}
</style>
"""

# -------- HOME --------
@app.route("/")
def home():
    return render_template_string(f"""
    {STYLE}
    <div class="sidebar">
        <h2>⚡ Rishaan</h2>
        <a href="/">Home</a>
        <a href="/about">About Me</a>
        <a href="/lego">LEGO</a>
        <a href="/sketch">Sketching</a>
        <a href="/football">Football</a>
        <a href="/planes">Planes</a>
    </div>

    <div class="content">
        <h1>🚀 Rishaan Kumar</h1>
        <p><b>Future Engineer • Creator • Builder</b></p>

        <p>
        Welcome to my digital world. I am not just a student — I am someone who loves
        building, creating and exploring how things work.
        </p>

        <p>
        Whether it’s LEGO, sketches, technology, or planes — I like understanding things deeply
        and turning ideas into reality.
        </p>

        <p>
        This website is a small glimpse of who I am today — and who I’m becoming.
        </p>

        <img src="/static/me1.jpg">
    </div>
    """)

# -------- ABOUT --------
@app.route("/about")
def about():
    return render_template_string(f"""
    {STYLE}
    <div class="sidebar">
        <a href="/">Home</a>
        <a href="/lego">LEGO</a>
        <a href="/sketch">Sketching</a>
    </div>

    <div class="content">
        <h1>👤 About Me</h1>

        <p>
        Hello, I am <b>Rishaan Kumar</b>, a student about to enter Grade 6 at 
        <b>Suncity School, Sector 54</b>.
        </p>

        <p>
        I have a strong interest in <b>technology and creativity</b>. I enjoy learning how things
        work and then building or recreating them in my own way.
        </p>

        <p>
        I am someone who likes exploring different areas — from building models to sketching
        characters and even observing airplanes during travel.
        </p>

        <p>
        I believe learning should be fun, creative and hands-on — and that’s exactly how I like to grow.
        </p>

        <img src="/static/me2.jpg">
    </div>
    """)

# -------- LEGO --------
@app.route("/lego")
def lego():
    return render_template_string(f"""
    {STYLE}
    <div class="sidebar">
        <a href="/">Home</a>
        <a href="/about">About</a>
    </div>

    <div class="content">
        <h1>🧱 LEGO Builder</h1>

        <p>
        LEGO is one of my favorite things because it combines creativity with engineering.
        </p>

        <p>
        I have built detailed models including the <b>Concorde airplane</b>, which shows my
        interest in both construction and aviation.
        </p>

        <p>
        Building LEGO helps me improve patience, focus, and problem-solving skills.
        </p>

        <img src="/static/lego.jpg">
    </div>
    """)

# -------- SKETCH --------
@app.route("/sketch")
def sketch():
    return render_template_string(f"""
    {STYLE}
    <div class="sidebar">
        <a href="/">Home</a>
    </div>

    <div class="content">
        <h1>✏️ Sketch Artist</h1>

        <p>
        I enjoy sketching, especially anime characters.
        </p>

        <p>
        Drawing helps me express creativity and improve attention to detail.
        </p>

        <p>
        Each sketch reflects practice, patience and my interest in art.
        </p>

        <img src="/static/anime1.jpg">
        <img src="/static/anime2.jpg">
    </div>
    """)

# -------- FOOTBALL --------
@app.route("/football")
def football():
    return render_template_string(f"""
    {STYLE}
    <div class="sidebar">
        <a href="/">Home</a>
    </div>

    <div class="content">
        <h1>⚽ Football Player</h1>

        <p>
        Football keeps me active and disciplined.
        </p>

        <p>
        It teaches teamwork, focus and quick decision making.
        </p>

        <p>
        I enjoy playing regularly and improving my skills.
        </p>
    </div>
    """)

# -------- PLANES --------
@app.route("/planes")
def planes():
    return render_template_string(f"""
    {STYLE}
    <div class="sidebar">
        <a href="/">Home</a>
    </div>

    <div class="content">
        <h1>✈️ Aviation Interest</h1>

        <p>
        I am very interested in airplanes and aviation.
        </p>

        <p>
        During travel, I enjoy spotting planes and observing their design.
        </p>

        <p>
        This interest connects with my love for building and engineering.
        </p>

        <img src="/static/plane.jpg">
    </div>
    """)

import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
