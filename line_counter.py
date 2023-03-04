import os


def get_files_in_folder(folder_path):
    files = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            files.append(file_path)
    return files


def main(folder):
    count = 0
    files = get_files_in_folder(folder)
    for file in files:
        with open(file) as file_data:
            for line in file_data.readlines():
                count += 1
    return count


if __name__ == "__main__":
    folder = input("Pfad zum Ordner, der gescannt werden soll: ")
    print(f"Gesamte Zeilen aller Dateien: {main(folder)}")
    input("Zum beenden Enter drücken...")
