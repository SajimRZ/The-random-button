from flask import Flask, render_template, request
import random

app = Flask(__name__)

word1 = [
    "slippers", "cookies", "spoons", "nuggets", "socks", "mugs", "noodles", "bubbles", "bananas", "pajamas",
    "stickers", "toasters", "headphones", "marbles", "glasses", "scissors", "toilets", "remotes", "buttons", "crumbs",
    "carrots", "donuts", "sneakers", "plungers", "pencils", "blankets", "chargers", "waffles", "tissues", "squirrels",
    "brooms", "sandals", "mirrors", "tacos", "drums", "mittens", "candles", "scooters", "beans", "sponges",
    "grapes", "eyebrows", "drawers", "lollipops", "kettles", "hats", "goggles", "flosses", "pebbles", "shoes",
    "apple", "mountain", "river", "cat", "book", "lamp", "cloud", "pencil", "shoe", "ocean", "robot", "bicycle",
    "garden", "mirror", "clock", "tree", "train", "window", "camera", "dragon", "backpack", "planet", "key", "feather", 
    "pizza", "umbrella", "jungle", "pillow", "castle", "star", "rocket", "carrot", "volcano", "coin", "bridge", "island", 
    "violin", "button", "lighthouse", "helmet", "suitcase", "banana", "glove", "ghost", "tower", "cup", "door", "chair", 
    "magnet", "sandwich"
]

word2 = [
    "broken", "twisted", "burned", "baked", "cracked", "smashed", "frozen", "shattered", "painted", "spilled",
    "wrinkled", "faded", "tangled", "scratched", "melted", "ripped", "popped", "cooked", "clogged", "jammed",
    "squished", "stuck", "soaked", "flattened", "creased", "bruised", "stained", "lost", "drained", "crumpled",
    "glued", "dented", "torn", "bent", "knitted", "wrapped", "stretched", "covered", "plastered", "inflated",
    "deflated", "chewed", "boiled", "flipped", "twirled", "hacked", "erased", "snapped", "drenched", "splattered",
    "gambled", "lost", "yeeted", "coped", "flipped"
]

@app.route("/", methods=["GET", "POST"])
def index():
    result = ""
    if request.method == "POST":
        percent = random.randint(1, 100)
        phrase = random.choice(word1) + " " + random.choice(word2)
        result = f"{percent}% {phrase}"
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
