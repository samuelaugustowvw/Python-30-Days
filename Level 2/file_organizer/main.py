import os
import shutil
EXTENSION_MAP = {
    "Images":    [".jpg", ".jpeg", ".png", ".gif", ".webp", ".bmp", ".svg"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".odt", ".xls", ".xlsx", ".ppt", ".pptx"],
    "Audio":     [".mp3", ".wav", ".flac", ".aac", ".ogg", ".m4a"],
    "Videos":    [".mp4", ".mkv", ".mov", ".avi", ".wmv", ".webm"],
    "Archives":  [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code":      [".py", ".js", ".html", ".css", ".java", ".c", ".cpp", ".json"],
}
def display_menu():
    print("\n==============================")
    print("        File Organizer")
    print("==============================")
def get_folder():
    while True:
        path = input("Enter the folder path: ").strip()
        if os.path.isdir(path):
            return path
        print("That folder does not exist. Try again.\n")
def get_category(extension):
    for category, extensions in EXTENSION_MAP.items():
        if extension in extensions:
            return category
    return "Others"
def get_unique_path(destination_folder, filename):
    target = os.path.join(destination_folder, filename)
    if not os.path.exists(target):
        return target
    name, extension = os.path.splitext(filename)
    counter = 1
    while os.path.exists(target):
        target = os.path.join(destination_folder, f"{name} ({counter}){extension}")
        counter+=1
    return target
def organize(folder,moves):
    count = 0
    for filename, category in moves:
        destination_folder = os.path.join(folder, category)
        os.makedirs(destination_folder, exist_ok=True)
        source = os.path.join(folder, filename)
        destination = get_unique_path(destination_folder, filename)
        shutil.move(source, destination)
        print(f"Moved:  {filename}  ->  {category}/")
        count+=1
    return count
def confirm(message):
    while True:
        answer = input(message).strip().upper()
        if answer in ("Y", "N"):
            return answer == "Y"
        print("Please enter Y or N.\n")
def plan_moves(folder):
    moves = []
    for filename in os.listdir(folder):
        full_path = os.path.join(folder, filename)
        if os.path.isdir(full_path):
            continue  # don't touch subfolders
        extension = os.path.splitext(filename)[1].lower()
        if not extension:
            continue  # skip files with no extension
        category = get_category(extension)
        moves.append((filename, category))
    return moves
def main():
    display_menu()
    folder = get_folder()
    moves = plan_moves(folder)
    if not moves:
        print("\nNothing to organize - no files with extensions found.")
        return
    print(f"\n{len(moves)} file(s) will be organized:")
    for filename, category in moves:
        print(f"  {filename}  ->  {category}/")
    if not confirm("\nProceed? (Y/N): "):
        print("Cancelled. No files were moved.")
        return
    print("\nOrganizing...\n")
    count = organize(folder, moves)
    categories_used = len(set(category for _, category in moves))
    print("\n========================")
    print(f"Done! {count} file(s) organized into {categories_used} folder(s).")
    print("========================")
if __name__ == "__main__":
    main()