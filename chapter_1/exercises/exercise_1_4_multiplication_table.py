# Exercise 1.4 - multiplication table
# Print a 10x10 multiplication table using two nested for loops,
# keep values aligned using string formatting.

def main():
    for i in range(1,11):
        for j in range(1,11):
            print(f"{i * j:3}", end=" ")
        print()

if __name__ == "__main__":
    main()
