def sort_by_rotation(file_path, output_path):
    import re
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    # Extract Rotation value and sort
    def extract_rotation(line):
        match = re.search(r'Rotation:\s*(\d+)', line)
        return int(match.group(1)) if match else float('inf')  # Handle lines without "Rotation"
    
    sorted_lines = sorted(lines, key=extract_rotation)
    
    # Write sorted lines to output file
    with open(output_path, 'w') as output_file:
        output_file.writelines(sorted_lines)

# Usage
sort_by_rotation("flags_type2.txt", "sorted_output.txt")

