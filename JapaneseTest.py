import random

# ---------- Dicts ---------- #
hira_main = {
    "あ": "a", "い": "i", "う": "u", "え": "e", "お": "o",        # Vowels
    "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko",   # K row
    "さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so",  # S row
    "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to", # T row
    "な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no",   # N row
    "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho",   # H row
    "ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo",   # M row
    "や": "ya", "ゆ": "yu", "よ": "yo",                           # Y row
    "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro",   # R row
    "わ": "wa", "を": "wo", "ん": "n"                             # W row + N
}
hira_dakuten = {
    "が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", # G row (K -> G)
    "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "ぞ": "zo", # Z row (S -> Z)
    "だ": "da", "ぢ": "ji", "づ": "zu", "で": "de", "ど": "do", # D row (T -> D)
    "ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo", # B row (H -> B)
    "ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"  # P row (H -> P) Handakuten
}
hira_combi = {
    "きゃ": "kya", "きゅ": "kyu", "きょ": "kyo", # K row
    "ぎゃ": "gya", "ぎゅ": "gyu", "ぎょ": "gyo", # G row
    "しゃ": "sha", "しゅ": "shu", "しょ": "sho", # S row
    "じゃ": "ja", "じゅ": "ju", "じょ": "jo",    # Z row
    "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho", # T row
    "ぢゃ": "ja", "ぢゅ": "ju", "ぢょ": "jo",    # D row
    "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo", # N row
    "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo", # H row
    "びゃ": "bya", "びゅ": "byu", "びょ": "byo", # B row
    "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo", # P row
    "みゃ": "mya", "みゅ": "myu", "みょ": "myo", # M row
    "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo"  # R row
}
kana_main = {}
kana_dakuten = {}
kana_combi = {}

# ---------- Workers ---------- #

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