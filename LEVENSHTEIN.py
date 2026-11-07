def intro():
    print("=" * 60)
    print("       WELCOME TO THE LEVENSHTEIN DISTANCE CALCULATOR")
    print("=" * 60)
    print()
    print("What is the Levenshtein distance?")
    print()
    print("In information theory, computer science and computational")
    print("linguistics, the Levenshtein distance is a metric that measures")
    print("the difference between two strings. It is the minimum number of")
    print("single-character edits (insertion, deletion, substitution)")
    print("needed to turn one string into the other, with cost 1 per edit.")
    print()
    print("It is named after the Soviet mathematician Vladimir Levenshtein,")
    print("who introduced it in 1965. It is a classic form of edit distance")
    print("and is used in spell checking, approximate search, OCR, speech")
    print("recognition, record matching and biological sequence comparison.")
    print()
    print("=" * 60)
    print()


def levenshtein(a, b):
    dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
    for i in range(len(a) + 1): dp[i][0] = i
    for j in range(len(b) + 1): dp[0][j] = j
    for i in range(1, len(a) + 1):
        for j in range(1, len(b) + 1):
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1,
                           dp[i-1][j-1] + (a[i-1] != b[j-1]))
    return dp


def show(a, b):
    dp = levenshtein(a, b)
    print("\nDistance:", dp[-1][-1], "\n")
    i, j, s = len(a), len(b), a
    step = 1
    while i or j:
        if i and j and dp[i][j] == dp[i-1][j-1] + (a[i-1] != b[j-1]):
            if a[i-1] != b[j-1]:
                s = s[:i-1] + b[j-1] + s[i:]
                print(f"{step}. {s}")
                step += 1
            i, j = i - 1, j - 1
        elif i and dp[i][j] == dp[i-1][j] + 1:
            s = s[:i-1] + s[i:]
            print(f"{step}. {s}")
            step += 1
            i -= 1
        else:
            s = s[:i] + b[j-1] + s[i:]
            print(f"{step}. {s}")
            step += 1
            j -= 1


def yes(prompt):
    return input(prompt).strip().lower() in ("y", "yes")


def run():
    a = input("First word:  ")
    b = input("Second word: ")
    while True:
        show(a, b)
        if not yes("\nDo you want to enter another word? (y/n): "):
            break
        print("  1) Continue from the last word")
        print("  2) Compare two different words")
        if input("Choice (1/2): ").strip() == "2":
            a = input("First word:  ")
            b = input("Second word: ")
        else:
            a = b
            b = input("New word: ")


intro()
run()
while yes("\nDo you want to enter a new word? (y/n): "):
    run()