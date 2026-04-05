import random

# ---------- Workers ---------- #
hira_main = {"あ": "a", }
hira_dakuten = {}
hira_combi = {}
kana_main = {}
kana_dakuten = {}
kana_combi = {}

def hiragana_kana():
    pass
def hiragana_dakuten():
    pass
def hiragana_combi():
    pass
def hiragana_both():
    pass
def hiragana_all():
    pass
def katakana_kana():
    pass
def katakana_dakuten():
    pass
def katakana_combi():
    pass
def katakana_both():
    pass
def katakana_all():
    pass
def hira_and_kata():
    pass
def stop_prog():
    pass

# ---------- Choice select -------- #
question_choice = {
    "1": {
        "name": "Hiragana",
        "options": {
            "1": {
                "name": "All main Kana",
                "worker": hiragana_kana
            },
            "2": {
                "name": "All main Dakuten",
                "worker": hiragana_dakuten
            },
            "3": {
                "name": "All main Combinations",
                "worker": hiragana_combi
            },
            "4": {
                "name": "All main Kana + Dakuten",
                "worker": hiragana_both
            },
            "5": {
                "name": "Everything",
                "worker": hiragana_all
            }
        }
    },
    "2": {
        "name": "Katakana",
        "options": {
            "1": {
                "name": "All main Kana",
                "worker": katakana_kana
            },
            "2": {
                "name": "All main Dakuten",
                "worker": katakana_dakuten
            },
            "3": {
                "name": "All main Combinations",
                "worker": katakana_combi
            },
            "4": {
                "name": "All main Kana + Dakuten",
                "worker": katakana_both
            },
            "5": {
                "name": "Everything",
                "worker": katakana_all
            }
        }
    },
    "3": {
        "name": "Hiragana & Katakana",
        "worker": hira_and_kata
    },
    "4": {
        "name": "Quit",
        "worker": stop_prog
    }
}  


# ---------- Menu loop ---------- #  
def ask_menu(question_choice):
    while True:
        print("\n--- Japanese Quiz ---")
        for key, value in question_choice.items():
            print(f"{key}. {value['name']}")

        choice = input("What do you want? ").strip()
        selected = question_choice.get(choice)

        if selected is None:
            print("Invalid choice, try again.")
            continue

        if "options" in selected:
            return ask_menu(selected["options"])

        worker = selected.get("worker")
        if worker is not None:
            return worker()
ask_menu(question_choice)  