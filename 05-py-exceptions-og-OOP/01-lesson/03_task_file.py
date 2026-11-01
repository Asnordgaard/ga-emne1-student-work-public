from pathlib import Path, UnsupportedOperation

data_folder = Path("..") / "data"
path = data_folder / "report.txt"

try:
    with path.open(mode="w", encoding="utf-8") as file:
        file.write("Practice report\n")
except FileNotFoundError:
    print(f"Error: The file does not exist ({path})")
except PermissionError:
    print("Error: You do not have permission to write to the file")


with path.open(encoding="utf-8") as file:
    text = file.read().strip()
print(text)