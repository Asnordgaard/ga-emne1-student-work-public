from pathlib import Path

data_folder = Path("..") / "data"
path = data_folder / "number.txt"



try:
    # Vi har tidligere lært:
    # with open(path, "r", encoding="utf-8") as file:
    # alternativt (anbefalt(?) kan vi skrive:
    with path.open(mode="r", encoding="utf-8") as file:
        number = int(file.read().strip())
    print(number * 2)
except FileNotFoundError:
    print(f"Error, could not open file {path}")
except ValueError:
    print("The file must contain an integer")