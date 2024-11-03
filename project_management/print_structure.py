import os

# Function to print directory structure
def print_structure(start_path, level=0):
    for item in os.listdir(start_path):
        path = os.path.join(start_path, item)
        print(" " * level * 2 + "|-- " + item)
        if os.path.isdir(path):
            print_structure(path, level + 1)


def main():
    # Print the project structure first
    print("Project structure:\n")
    print_structure(".")


if __name__ == "__main__":

    main()
