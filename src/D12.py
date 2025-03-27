from Die import D12

def main():
    d12 = D12()
    roll_result = d12.roll()
    print(f"You rolled a 6-sided die and got: {roll_result}")

if __name__ == "__main__":
    main()