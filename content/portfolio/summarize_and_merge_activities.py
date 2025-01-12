import os
import re
from openai import OpenAI
from datetime import datetime

client = OpenAI()

# Define the directories to search for markdown files
directories = [
    "projects",
    "research",
    "community_activities",
    "papers",
    "work",
    "academic-achievements",
]
system_instruction = """
You are a text summarization model. Given a detailed description of an activity that I, Robert, participated in, your task is to extract and summarize the key points into 2 to 3 bullet points. Each bullet point should be one imperative sentence, clearly stating the actions taken and highlighting the major traits or skills I showcased or developed. Focus on conciseness and clarity, ensuring that the summary reflects both the actions and the personal growth or attributes demonstrated.
"""
output_file = "summarized_and_merged_activities.md"

def parse_header(content):
    return None

def remove_after_ignore(content):
    return content.split("***IGNORE***", 1)[0].strip()

def summarize_content(content):
    try:
        response = client.chat.completions.create(model="gpt-4o",
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": content},
        ])
        summary = response.choices[0].message.content.strip()
        return summary
    except Exception as e:
        print(f"Error summarizing content: {e}")
        return "Error: Unable to generate summary."

def generate_content(path, type, instruction):
    ...


def _merge_all_documents():
    ...


def main():
    with open(output_file, 'w') as outfile:
        for directory in directories:
            for filename in os.listdir(directory):
                if filename.endswith(".md"):
                    with open(os.path.join(directory, filename), 'r') as infile:
                        content = infile.read()

                        # Parse the header information
                        header = parse_header(content)
                        
                        # Write the file header to the output file
                        assert filename.endswith(".md")
                        assert filename[-3:] == ".md", filename
                        outfile.write(f"#### {filename[:-3]}\n\n")
                        
                        if header:
                            outfile.write("## Header Information:\n")
                            for key, value in header.items():
                                outfile.write(f"- **{key}**: {value}\n")
                            outfile.write("\n")
                        
                        # Write the summarized content
                        body = re.sub(r'^---\n(.*?)\n---', '', content, flags=re.DOTALL).strip()
                        body = remove_after_ignore(body)
                        
                        summary = summarize_content(body)
                        outfile.write(summary)
                        outfile.write("\n\n")  # Add some space between files


    print(f"All markdown files have been merged and summarized into {output_file}.")
    print(f"Time of completion: {datetime.now()}")


if __name__ == '__main__':
    main()
