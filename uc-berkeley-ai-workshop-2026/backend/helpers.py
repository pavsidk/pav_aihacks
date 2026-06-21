from session import session


# ---------- Preferences ----------

def add_preference(preference_type, preference):
    session["preferences"][preference_type].append(preference)


def get_preferences():
    return session["preferences"]


# ---------- Recipe ----------

def set_recipe(name, start_time, end_time):
    session["recipe"]["name"] = name
    session["recipe"]["start_time"] = start_time
    session["recipe"]["expected_end_time"] = end_time
    session["recipe"]["current_step"] = 0
    session["recipe"]["cards"] = []


def get_recipe():
    return session["recipe"]


# ---------- Cards ----------

def add_card(card):
    session["recipe"]["cards"].append(card)


def get_cards():
    return session["recipe"]["cards"]


def get_current_card():
    current_step = session["recipe"]["current_step"]
    cards = session["recipe"]["cards"]

    if current_step >= len(cards):
        return None

    return cards[current_step]


def next_step():
    if session["recipe"]["current_step"] < len(session["recipe"]["cards"]) - 1:
        session["recipe"]["current_step"] += 1


def previous_step():
    if session["recipe"]["current_step"] > 0:
        session["recipe"]["current_step"] -= 1


def repeat_step():
    return get_current_card()


# ---------- Timers ----------

def add_timer(timer):
    session["timers"].append(timer)


def get_timers():
    return session["timers"]


def remove_timer(timer_name):
    session["timers"] = [
        timer
        for timer in session["timers"]
        if timer["name"] != timer_name
    ]


# ---------- Mistakes ----------

def add_mistake(step_number, description):
    mistake = {
        "step_number": step_number,
        "description": description,
        "resolved": False
    }

    session["mistakes"].append(mistake)


def get_mistakes():
    return session["mistakes"]


def resolve_mistake(index):
    if index < len(session["mistakes"]):
        session["mistakes"][index]["resolved"] = True


# ---------- History ----------

def add_history(role, content):
    history_item = {
        "role": role,
        "content": content
    }

    session["history"].append(history_item)


def get_history():
    return session["history"]


# ---------- Reset ----------

def reset_session():
    session["recipe"]["name"] = None
    session["recipe"]["start_time"] = None
    session["recipe"]["expected_end_time"] = None
    session["recipe"]["current_step"] = 0
    session["recipe"]["cards"] = []

    session["timers"] = []
    session["mistakes"] = []
    session["history"] = []