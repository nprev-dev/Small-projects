import random
# to add later:
# - Add linguo help (gojūon, kana, hiragana katakana and etc)
# - History system
# - Grade system (in %) and maybe show mistakes
# - chose how many questions u want (with an all option)
# - Add grammar rules (small tsu, long vowels, combination explication etc, maybe later add tips on how to learn)


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
    "しゃ": "sha", "しゅ": "shu", "しょ": "sho", # S row *SPECIAL
    "じゃ": "ja", "じゅ": "ju", "じょ": "jo",    # Z row *SPECIAL
    "ちゃ": "cha", "ちゅ": "chu", "ちょ": "cho", # T row *SPECIAL
    "ぢゃ": "ja", "ぢゅ": "ju", "ぢょ": "jo",    # D row *SPECIAL
    "にゃ": "nya", "にゅ": "nyu", "にょ": "nyo", # N row
    "ひゃ": "hya", "ひゅ": "hyu", "ひょ": "hyo", # H row
    "びゃ": "bya", "びゅ": "byu", "びょ": "byo", # B row
    "ぴゃ": "pya", "ぴゅ": "pyu", "ぴょ": "pyo", # P row
    "みゃ": "mya", "みゅ": "myu", "みょ": "myo", # M row
    "りゃ": "rya", "りゅ": "ryu", "りょ": "ryo"  # R row
}
kata_main = {
    "ア": "a", "エ": "e", "イ": "i", "オ": "o", "ウ": "u",        # Vowels
    "カ": "ka", "ケ": "ke", "キ": "ki", "コ": "ko", "ク": "ku",   # K row
    "サ": "sa", "セ": "se", "シ": "shi", "ソ": "so", "ス": "su",  # S row
    "タ": "ta", "テ": "te", "チ": "chi", "ト": "to", "ツ": "tsu", # T row
    "ナ": "na", "ネ": "ne", "ニ": "ni", "ノ": "no", "ヌ": "nu",   # N row
    "ハ": "ha", "ヘ": "he", "ヒ": "hi", "ホ": "ho", "フ": "fu",   # H row
    "マ": "ma", "メ": "me", "ミ": "mi", "モ": "mo", "ム": "mu",   # M row
    "ヤ": "ya", "ヨ": "yo", "ユ": "yu",                           # Y row
    "ラ": "ra", "レ": "re", "リ": "ri", "ロ": "ro", "ル": "ru",   # R row
    "ワ": "wa", "ヲ": "wo", "ン": "n"                             # W row + N
}
kata_dakuten = {
    "ガ": "ga", "ゲ": "ge", "ギ": "gi", "ゴ": "go", "グ": "gu", # G row (K -> G)
    "ザ": "za", "ゼ": "ze", "ジ": "ji", "ゾ": "zo", "ズ": "zu", # Z row (S -> Z)
    "ダ": "da", "デ": "de", "ヂ": "ji", "ド": "do", "ヅ": "zu", # D row (T -> D)
    "バ": "ba", "ベ": "be", "ビ": "bi", "ボ": "bo", "ブ": "bu", # B row (H -> B)
    "パ": "pa", "ペ": "pe", "ピ": "pi", "ポ": "po", "プ": "pu"  # P row (H -> P) Handakuten
}
kata_combi = {
    "キャ": "kya", "キョ": "kyo", "キュ": "kyu", # K row
    "ギャ": "gya", "ギョ": "gyo", "ギュ": "gyu", # G row
    "シャ": "sha", "ショ": "sho", "シュ": "shu", # S row *SPECIAL
    "ジャ": "ja", "ジョ": "jo", "ジュ": "ju",    # Z row *SPECIAL
    "チャ": "cha", "チョ": "cho", "チュ": "chu", # T row *SPECIAL
    "ヂャ": "ja", "ヂョ": "jo", "ヂュ": "ju",    # D row *SPECIAL
    "ニャ": "nya", "ニョ": "nyo", "ニュ": "nyu", # N row
    "ヒャ": "hya", "ヒョ": "hyo", "ヒュ": "hyu", # H row
    "ビャ": "bya", "ビョ": "byo", "ビュ": "byu", # B row
    "ピャ": "pya", "ピョ": "pyo", "ピュ": "pyu", # P row
    "ミャ": "mya", "ミョ": "myo", "ミュ": "myu", # M row
    "リャ": "rya", "リョ": "ryo", "リュ": "ryu"  # R row
}

# ---------- Workers ---------- #

def hiragana_gojūon():
    while True:
        num_ques = num_questions()
        if num_ques > len(hira_main):
            print(f"Number is bigger than question pool, enter a number between 1 and {len(hira_main)}.")
            continue
        elif num_ques <= len(hira_main):
            break
    wrong = 0 # nb wrong answer
    right = 0 # nb right answer
    count = 0 # current amount of questions asked 
    selected = random.sample(list(hira_main.items()), num_ques)
    for index, (jp, en) in enumerate(selected, start=1):
        while True:                                            # loop till right answer
            answer = input(f"{index}. {jp}: ").strip().lower() #removes whitespaces and puts in lowercase
            if answer == en:
                print("Correct")
                right += 1             # to later implement rating 
                break
            elif answer == "skip":
                print("Skipping")        # later add score penalty will be applied to message
                wrong += 1
                break
            elif answer == "quit":
                exit()
            else:
                print("Try again")
                wrong += 1
def hiragana_dakuten():
    while True:
        num_ques = num_questions()
        if num_ques > len(hira_dakuten):
            print(f"Number is bigger than question pool, enter a number between 1 and {len(hira_dakuten)}.")
            continue
        elif num_ques <= len(hira_dakuten):
            break
    wrong = 0 # nb wrong answer
    right = 0 # nb right answer
    count = 0 # current amount of questions asked 
    selected = random.sample(list(hira_dakuten.items()), num_ques)
    for index, (jp, en) in enumerate(selected, start=1):
        while True:                                            # loop till right answer
            answer = input(f"{index}. {jp}: ").strip().lower() #removes whitespaces and puts in lowercase
            if answer == en:
                print("Correct")
                right += 1             # to later implement rating 
                break
            elif answer == "skip":
                print("Skipping")        # later add score penalty will be applied to message
                wrong += 1
                break
            elif answer == "quit":
                exit()
            else:
                print("Try again")
                wrong += 1
def hiragana_combi():
    while True:
        num_ques = num_questions()
        if num_ques > len(hira_combi):
            print(f"Number is bigger than question pool, enter a number between 1 and {len(hira_combi)}.")
            continue
        elif num_ques <= len(hira_combi):
            break
    wrong = 0 # nb wrong answer
    right = 0 # nb right answer
    count = 0 # current amount of questions asked 
    selected = random.sample(list(hira_combi.items()), num_ques)
    for index, (jp, en) in enumerate(selected, start=1):
        while True:                                            # loop till right answer
            answer = input(f"{index}. {jp}: ").strip().lower() #removes whitespaces and puts in lowercase
            if answer == en:
                print("Correct")
                right += 1             # to later implement rating 
                break
            elif answer == "skip":
                print("Skipping")        # later add score penalty will be applied to message
                wrong += 1
                break
            elif answer == "quit":
                exit()
            else:
                print("Try again")
                wrong += 1
def hiragana_both():
    hira_both = hira_main | hira_dakuten
    while True:
        num_ques = num_questions()
        if num_ques > len(hira_both):
            print(f"Number is bigger than question pool, enter a number between 1 and {len(hira_both)}.")
            continue
        elif num_ques <= len(hira_both):
            break
    wrong = 0 # nb wrong answer
    right = 0 # nb right answer
    count = 0 # current amount of questions asked 
    selected = random.sample(list(hira_both.items()), num_ques)
    for index, (jp, en) in enumerate(selected, start=1):
        while True:                                            # loop till right answer
            answer = input(f"{index}. {jp}: ").strip().lower() #removes whitespaces and puts in lowercase
            if answer == en:
                print("Correct")
                right += 1             # to later implement rating 
                break
            elif answer == "skip":
                print("Skipping")        # later add score penalty will be applied to message
                wrong += 1
                break
            elif answer == "quit":
                exit()
            else:
                print("Try again")
                wrong += 1
def hiragana_kana():
    hira_kana = hira_main | hira_dakuten | hira_combi
def katakana_gojūon():
    pass
def katakana_dakuten():
    pass
def katakana_combi():
    pass
def katakana_both():
    kata_both = kata_main | kata_dakuten
def katakana_kana():
    kata_kana = kata_main | kata_dakuten | kata_combi
def hira_and_kata():
    hira_nd_kata = hira_main | hira_dakuten | hira_combi | kata_main | kata_dakuten | kata_combi
def stop_prog():
    print("Stopping program!")
    exit()

# ---------- Choice select -------- #
question_choice = {
    "1": {
        "name": "Hiragana set",
        "options": {
            "1": {
                "name": "All Hiragana Gojūon",
                "worker": hiragana_gojūon,
                "log": True
            },
            "2": {
                "name": "All Hiragana Dakuten",
                "worker": hiragana_dakuten,
                "log": True
            },
            "3": {
                "name": "All Hiragana Combinations",
                "worker": hiragana_combi,
                "log": True
            },
            "4": {
                "name": "All Hiragana Gojūon + Dakuten",
                "worker": hiragana_both,
                "log": True
            },
            "5": {
                "name": "Everything",
                "worker": hiragana_kana,
                "log": True
            }
        }
    },
    "2": {
        "name": "Katakana set",
        "options": {
            "1": {
                "name": "All Katakana Gojūon",
                "worker": katakana_gojūon,
                "log": True
            },
            "2": {
                "name": "All Katakana Dakuten",
                "worker": katakana_dakuten,
                "log": True
            },
            "3": {
                "name": "All Katakana Combinations",
                "worker": katakana_combi,
                "log": True
            },
            "4": {
                "name": "All Katakana Gojūon + Dakuten",
                "worker": katakana_both,
                "log": True
            },
            "5": {
                "name": "Everything",
                "worker": katakana_kana,
                "log": True
            }
        }
    },
    "3": {
        "name": "Hiragana & Katakana",
        "worker": hira_and_kata,
        "log": True
    },
    "4": {
        "name": "Quit",
        "worker": stop_prog
    }
} 

# ---------- Amount Question ---------- #
#implement limit & all system
def num_questions():
    while True:
        num_question = input("Enter amount of questions u want to be asked: ")
        if not num_question.strip().isdigit():
            print("Value needs to be a number.")
            continue

        num_question = int(num_question)

        if num_question < 1:
            print("Value needs to be bigger than 1.")
            continue
        
        return num_question

# ---------- Check History ---------- #


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
            ask_menu(selected["options"])
            continue

        worker = selected.get("worker")
        if callable(worker):
            worker()
            continue
ask_menu(question_choice)  
#