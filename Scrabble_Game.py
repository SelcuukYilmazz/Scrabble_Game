import time
import sys
p = open(sys.argv[1],"r",encoding="utf-8")
f = open(sys.argv[2],"r",encoding="utf-8")
value = {}
points = []
guessed = []
score = []
for l in f.readlines():
    a = l.rstrip("\n").split(":")
    value[a[0]] = int(a[1])
for k in p.readlines():
    guessed.clear()
    score.clear()
    a = time.time()
    words = k.rstrip("\n").split(":")
    trueguess = words[1].split(",")
    print("shuffled letters are : ", words[0], " Please guess words for these letters with minimum three letters", )
    while time.time()-a < 30:
        guess = input("guessed word:").replace("i","İ").upper()
        if time.time() - a < 30:
            if guess in trueguess:
                if not guess in guessed:
                    guessed.append(guess)
                    for point in guess:
                        points.append(value[point])
                    score.append(sum(points)*len(guess))
                    points.clear()
                    print("you have",30-(int(time.time() - a)),"time")
                else:
                    print("You already guessed that.")
                    print("you have", 30 - (int(time.time() - a)), "time")
            else:
                print("Your guessed word is not a valid word")
                print("you have",30-(int(time.time() - a)),"time")
                pass
        else:
            print("Time's up")
            print("score for ",words[0],"is",sum(score),"and guessed words are: ","-".join(guessed))