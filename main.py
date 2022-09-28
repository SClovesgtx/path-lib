from importlib.resources import path
from pathlib import Path
import time

def main():
    print(f"\nCorrent working directory: {Path.cwd()}\n")
    print(f"Home directory: {Path.home()}\n")
    
    p = Path("home/cloves/blablabla")
    print(f"Path bblabla exist? {'yes' if p.exists() else 'no'}\n")

    p2 = Path("/home") / "cloves" / "Documents"
    print(f"p2 exist? {'yes' if p2.exists() else 'no'}\n")

    p3 = Path.cwd() / "test_dir" / "test_file.txt"
    print(f"p3 exist? {'yes' if p3.exists() else 'no'}\n")

    with p3.open() as file:
        print(file.read())

    print(p3.read_text())

    p4 = Path("test_file.txt")
    p5 = p4.resolve()
    print(f"Resolving test_file.txt: {p5}\n")

    print(f"Parent of p5: {p5.parent}\n")

    print(f"Granparent of p5: {p5.parent.parent}\n")

    print(f"Name of p5: {p5.name}\n")

    print(f"Stem of p5: {p5.stem}\n")

    print(f"Suffix: {p5.suffix}\n")

    print(f"Is p5 a directory? {'yes' if p5.is_dir() else 'no'}\n")

    print(f"Is p5 a file? {'yes' if p5.is_file() else 'no'}\n")

    # creating new file
    print("Creating a file...\n")
    time.sleep(3)
    new_file = Path.cwd() / "new_file.txt"
    new_file.write_text("Hello Cloves!")
    new_file.touch()

    # deleting a file
    print("Deleting the new file...")
    time.sleep(3)
    new_file.unlink()

    # new directory
    print("Creating a dir...\n")
    time.sleep(3)
    new_dir = Path.cwd() / "new_test_dir"
    new_dir.mkdir()

    # delete new_dir
    print("Deleting new dir...\n")
    time.sleep(3)
    new_dir.rmdir()


if __name__=="__main__":
    main()