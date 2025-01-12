
import os
import re


# Function to parse the header from the markdown file
# def parse_header(content):
#     header = {}
#     match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
#     if match:
#         header_content = match.group(1)
#         for line in header_content.splitlines():
#             key, value = line.split(':', 1)
#             header[key.strip()] = value.strip()
#     return header

def parse_header(content):
    return None

def remove_after_ignore(content):
    return content.split("***IGNORE***", 1)[0].strip()


# Create or overwrite the merged markdown file
def create_merged_file(output_file, directories):
    with open(output_file, 'w') as outfile:
        for directory in directories:
            for filename in os.listdir(directory):
                if filename.endswith(".md"):
                    with open(os.path.join(directory, filename), 'r') as infile:
                        content = infile.read()

                        # Parse the header information
                        header = parse_header(content)
                        
                        # Write the file header to the output file
                        outfile.write(f"# {filename}\n\n")
                        
                        if header:
                            outfile.write("## Header Information:\n")
                            for key, value in header.items():
                                outfile.write(f"- **{key}**: {value}\n")
                            outfile.write("\n")
                        
                        # Write the content excluding the header
                        # body = re.sub(r'^---\n(.*?)\n---', '', content, flags=re.DOTALL).strip()
                        body = content
                        body = remove_after_ignore(body)
                        outfile.write(body)
                        outfile.write("\n\n")  # Add some space between files


if __name__ == '__main__':
    # Define the directories to search for markdown files
    directories = [
        "academic-achievements",
        "community_activities",
        "papers",
        "projects",
        "research",
        "work"
    ]

    # Define the output file name
    output_file = "merged_activities.md"
    create_merged_file(output_file, directories)
    print(f"All markdown files have been merged into {output_file}.")
