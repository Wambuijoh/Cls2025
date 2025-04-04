
def main():

    filename = input("Enter the filename: ")

    try:
        
        with open(filename, "r") as file:
            content = file.read()
            print("\nFile content:")
            print(content)
    except FileNotFoundError:
        
        print(f"Error: The file '{filename}' does not exist.")
    except PermissionError:
    
        print(f"Error: You do not have permission to read the file '{filename}'.")
    except Exception as e:
    
        print(f"An unexpected error occurred: {e}")


if __name__ == "__main__":
    main()