import os

def main():
    file_name = input('add file name\n');
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir, file_name)
    with open(filepath, 'w') as f:
        f.write("Hello\n")

if __name__ == "__main__":
    main()