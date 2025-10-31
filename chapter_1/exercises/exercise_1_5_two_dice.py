#%% exercise_1_5_two_dice.py
# Exercise 1.5 (two dice)
# Iterate through all outcomes of two dice (1..6) and print ordered pairs
# that sum to 5, one pair per line. Implemented inside main().

def main():
    for d1 in range(1,7):
        for d2 in range(1,7):
            if d1 + d2 == 5:
                print((d1 , d2))

if __name__ == "__main__":
    main()