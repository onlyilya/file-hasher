import hashlib
import os

def hash_file(filepath):
    sha256 = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            sha256.update(chunk)
    return sha256.hexdigest()

def hash_directory(directory):
    hashes = {}
    for root, _, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_hash = hash_file(filepath)
            relative_path = os.path.relpath(filepath, directory)
            hashes[relative_path] = file_hash
    return hashes

def save_hashes(hashes, output_file='file_hashes.txt'):
    with open(output_file, 'w') as f:
        for path, file_hash in sorted(hashes.items()):
            f.write(f"{file_hash}  {path}\n")

if __name__ == '__main__':
    directory = input("Введите путь к директории: ")
    hashes = hash_directory(directory)
    save_hashes(hashes)
    print("Хеши сохранены в файл 'file_hashes.txt'")
