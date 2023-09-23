from .dir_creator import create_dir


def main():
    temp_dir_path, created = create_dir()

    if created:
        print(f"Created a new temp directory at {temp_dir_path}")
    else:
        print(f"Using existing temp directory at {temp_dir_path}")
        
    print("To enter run the following command:")
    print(f"cd {temp_dir_path}")


if __name__ == "__main__":
    main()
