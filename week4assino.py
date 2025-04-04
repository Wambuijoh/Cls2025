
input_file = "input.txt"    
output_file = "output.txt"  

try:

    with open(input_file, "r") as infile:
        
        content = infile.read()
        
        
        modified_content = content.upper()

    
    with open(output_file, "w") as outfile:
        
        outfile.write(modified_content)

    print(f"File '{input_file}' has been modified and saved as '{output_file}'.")

except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")