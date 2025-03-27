from Die import D10

def main():
    d10 = D10()
    roll_result = d10.roll()
    print(f"You rolled a 10-sided die and got: {roll_result}")

if __name__ == "__main__":
    main()