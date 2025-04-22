import re
import os
import datetime


# Clean title
def clean_title(title: str):
	"""
	Clean the title by removing triple asterisks.
	"""
	return title.replace("***", "").strip()


# Generate HTML Bookmarks
def generate_html_bookmarks(md_filename: str, bookmarks_filename: str):
	"""
	Parses a markdown file to extract URLs, titles, and sections, then saves them in HTML Bookmark File Format.
	"""

	# Stack to track opened header levels
	header_stack = []

	# Timestamp
	bookmark_timestamp = int(datetime.datetime.now().timestamp())

	# Counter for the number of links
	link_count = 0

	# List of headers to ignore
	ignored_headers = {"Table of Contents", "Contact"}

	# Flag to skip sections
	skip_section = False

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

				# Skip headers that should be ignored
				if title in ignored_headers:
					# Ignore this section completely
					skip_section = True
					continue
				else:
					# Allow adding links under this new valid header
					skip_section = False

				# Close previous sections
				while header_stack and header_stack[-1] >= current_level:
					bm_file.write('    ' * (header_stack.pop() - 1) + '</DL><p>\n')

				# Open new header
				header_stack.append(current_level)
				bm_file.write('    ' * (current_level - 1) + f'<DT><H3 ADD_DATE="{bookmark_timestamp}" LAST_MODIFIED="{bookmark_timestamp}">{title}</H3>\n')
				bm_file.write('    ' * (current_level - 1) + '<DL><p>\n')

			# Bookmarks (Only process if not skipping a section)
			if not skip_section:
				for title, url in link_match:
					bm_file.write('    ' * (header_stack[-1] if header_stack else 0) + f'<DT><A HREF="{url}" ADD_DATE="{bookmark_timestamp}">{title}</A>\n')
					link_count += 1

		# Close remaining sections
		while header_stack:
			bm_file.write('    ' * (header_stack.pop() - 1) + '</DL><p>\n')

	return link_count


# Main function
def main():
	"""
	Main function to run the script.
	"""

	# Generate Bookmarks
	md_filename = "../Readme.md"
	bookmarks_filename = "bookmarks.html"
	bookmarks_filename_path = os.path.abspath(bookmarks_filename)
	link_count = generate_html_bookmarks(md_filename, bookmarks_filename)
	print(f'The bookmarks file is located at: {bookmarks_filename_path}')
	print(f'{link_count} links have been added to the bookmarks.')


# Execute script
if __name__ == "__main__":
	main()
