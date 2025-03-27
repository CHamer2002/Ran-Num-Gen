from Die import D4

def main():
    d4 = D4()
    roll_result = d4.roll()
    print(f"You rolled a 4-sided die and got: {roll_result}")

if __name__ == "__main__":
    main()