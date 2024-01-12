import re
import datetime


def clean_title(title: str):
    """
    Clean the title by removing triple asterisks.
    :param title:
    :return:
    """

    return title.replace("***", "").strip()


def generate_html_bookmarks(md_filename: str, bookmarks_filename: str):
    """
    Parses a markdown file to extract URLs, titles, and sections, then saves them in HTML Bookmark File Format.
    :param md_filename:
    :param bookmarks_filename:
    :return:
    """

    # Stack to track opened header levels
    header_stack = []
    bookmark_timestamp = int(datetime.datetime.now().timestamp())

    # Markdown File
    with open(md_filename, 'r', encoding='utf-8') as md_file:
        content = md_file.readlines()

    # Patterns
    md_link_pattern = r'\[([^\]]+)\]\((http[s]?://[^)]+)\)'
    header_pattern = r'^(#+) (.*)'

    # HTML File
    with open(bookmarks_filename, 'w', encoding='utf-8') as bm_file:
        bm_file.write('<!DOCTYPE NETSCAPE-Bookmark-file-1>\n')
        bm_file.write('<!-- This is an automatically generated file. DO NOT EDIT! -->\n')
        bm_file.write('<META HTTP-EQUIV="Content-Type" CONTENT="text/html; charset=UTF-8">\n')
        bm_file.write('<TITLE>Bookmarks</TITLE>\n')
        bm_file.write('<H1>Bookmarks</H1>\n<DL><p>\n')

        # Content
        for line in content:
            header_match = re.match(header_pattern, line.strip())
            link_match = re.findall(md_link_pattern, line)

            # Headers
            if header_match:
                current_level = len(header_match.group(1))
                title = clean_title(header_match.group(2))

                # Close
                while header_stack and header_stack[-1] >= current_level:
                    bm_file.write('    ' * (header_stack.pop() - 1) + '</DL><p>\n')

                # Folder
                header_stack.append(current_level)
                bm_file.write('    ' * (current_level - 1) + f'<DT><H3 ADD_DATE="{bookmark_timestamp}" LAST_MODIFIED="{bookmark_timestamp}">{title}</H3>\n')
                bm_file.write('    ' * (current_level - 1) + '<DL><p>\n')

            # Bookmarks
            for title, url in link_match:
                bm_file.write('    ' * (header_stack[-1] if header_stack else 0) + f'<DT><A HREF="{url}" ADD_DATE="{bookmark_timestamp}">{title}</A>\n')

        # Close
        while header_stack:
            bm_file.write('    ' * (header_stack.pop() - 1) + '</DL><p>\n')


def main():
    """
    Main function to run the script.
    :return:
    """

    # Generate Bookmarks
    generate_html_bookmarks("../Readme.md", "bookmarks.html")


if __name__ == "__main__":
    main()
