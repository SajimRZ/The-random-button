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
    "gardens", "mirrors", "clocks", "trees", "trains", "windows", "cameras", "dragons", "backpacks", "planets", "keys", "feathers", 
    "pizzas", "umbrellas", "jungles", "pillows", "castles", "stars", "rockets", "carrots", "volcanos", "coins", "bridges", "islands", 
    "violins", "buttons", "lighthouses", "helmets", "suitcases", "bananas", "gloves", "ghosts", "towers", "cups", "doors", "chairs", 
    "magnets", "sandwichs", "orphans", "police", "little boys", "little girls", "caves", "cucumbers", "alchohol", "asians",
    "africans", "americans", "porn", "singers", "politicians", "women", "bottles", "animals", "plastics", "oceans", "clowns",
    "car salesmen", "students", "friends", "tests", "bathrooms", "hospitals", "organ donors", "live streamers", "Vtubers",
    "white vans"
]

word2 = [
    "broken", "twisted", "burned", "baked", "cracked", "smashed", "frozen", "shattered", "painted", "spilled",
    "wrinkled", "faded", "tangled", "scratched", "melted", "ripped", "popped", "cooked", "clogged", "jammed",
    "squished", "stuck", "soaked", "flattened", "creased", "bruised", "stained", "lost", "drained", "crumpled",
    "glued", "dented", "torn", "bent", "knitted", "wrapped", "stretched", "covered", "plastered", "inflated",
    "deflated", "chewed", "boiled", "flipped", "twirled", "hacked", "erased", "snapped", "drenched", "splattered",
    "gambled", "lost", "yeeted", "coped", "flipped", "incerted", "penetrated", " vored", "enjoyed", "sizzled", "ringed",
    "burped", "vomited", " snorted", "buried", "full of cats", "underground", "in the air", "inverted", "pumped",
    "scamed", "perfected", "are a failure", "orphaned", "need some milk", "are underachievers", "are stinky",
    "has a foot fetish", "has an armpit fetish", "doesnt know directions", "are bilingual", "got arrested", "sad :(",
    "are wet", "want to be wet", "in your area", "abandoned", "sold", "got sequels", "polluted", "groomed", "diddied",
    "in a coma", "want to pee", "are peeing", "are full of piss", "never saw a bird", "doesnt exist", "cant spell", 
    "are perverts", "are horny", "hate purple", "are poor", "have AIDS", "have stds", "doesnt know what sex is",
    "love incest", "have incest", "are siscons", "are brocons", "are lolicons", "aborted", "are forever gone",
    "are funny"
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
