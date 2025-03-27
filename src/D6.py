from Die import D6

def main():
    d6 = D6()
    roll_result = d6.roll()
    print(f"You rolled a 6-sided die and got: {roll_result}")

if __name__ == "__main__":
    main()
