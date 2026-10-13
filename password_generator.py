import random
import string
import os
from datetime import datetime

OUTPUT_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "passwords.txt")


def generate_password(length: int, num_upper: int, num_digits: int) -> str:
    if num_upper < 0 or num_digits < 0:
        raise ValueError("Counts cannot be negative.")
    if num_upper + num_digits > length:
        raise ValueError(
            f"Uppercase ({num_upper}) + digits ({num_digits}) = "
            f"{num_upper + num_digits} exceeds total length ({length})."
        )

    num_lower = length - num_upper - num_digits

    chars = (
        random.choices(string.ascii_uppercase, k=num_upper) +
        random.choices(string.ascii_lowercase, k=num_lower) +
        random.choices(string.digits,          k=num_digits)
    )

    random.shuffle(chars)
    return "".join(chars)


def get_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("  ✗ Please enter a whole number.")


def save_password(platform: str, password: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    line = f"[{timestamp}] Platform: {platform:<30} Password: {password}\n"
    with open(OUTPUT_FILE, "a", encoding="utf-8") as f:
        f.write(line)


def main():
    print("\n=== Password Generator ===\n")

    platform = input("Platform / service (e.g. Gmail): ").strip()
    while not platform:
        print("  ✗ Platform name cannot be empty.")
        platform = input("Platform / service: ").strip()

    length  = get_int("Total password length      : ")
    upper   = get_int("Number of uppercase letters: ")
    digits  = get_int("Number of digits           : ")

    try:
        password = generate_password(length, upper, digits)
    except ValueError as e:
        print(f"\n✗ Error: {e}")
        return

    print(f"\nGenerated password : {password}")
    print(f"  Length           : {length}")
    print(f"  Uppercase        : {upper}")
    print(f"  Digits           : {digits}")
    print(f"  Lowercase        : {length - upper - digits}")
    print(f"  Platform         : {platform}")

    save_password(platform, password)
    print(f"\n✓ Saved to {OUTPUT_FILE}\n")


if __name__ == "__main__":
    main()
