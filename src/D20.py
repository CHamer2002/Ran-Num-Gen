from Die import D20

def main():
    d20 = D20()
    roll_result = d20.roll()
    print(f"You rolled a 6-sided die and got: {roll_result}")

if __name__ == "__main__":
    main()