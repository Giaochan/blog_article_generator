

def write_to_markdown_file(filename, text):
    """
    This function writes a text into a markdown file

    Parameters:
    filename (str): The name of the file
    text (str): The text to write in the file

    Returns:
    None
    """

    with open(f"articles/{filename}.md", "w", encoding="utf-8") as f:
        f.write(text)
        
def sanitize_filename(filename):
    invalid_chars = ["<", ">", ":", '"', "/", "\\", "|", "?", "*"]
    for char in invalid_chars:
        filename = filename.replace(char, "")
    return filename