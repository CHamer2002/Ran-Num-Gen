from Die import D8

def main():
    d8 = D8()
    roll_result = d8.roll()
    print(f"You rolled a 8-sided die and got: {roll_result}")

if __name__ == "__main__":
    main()