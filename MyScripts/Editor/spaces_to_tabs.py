import editor
import itertools

# Storing the text of the program.
text = editor.get_text()
# Storing the selected range.
selected_range = editor.get_selection()
# Getting the selected text.
selected_text = text[selected_range[0]:selected_range[1]]

# List to store the updated lines of code.
new_lines = []
# Looping through the old lines (including the line breaks).
for line in selected_text.splitlines(keepends=True):
	# Checking the number of spaces.
	spaces = "".join(itertools.takewhile(lambda x: x == " ", line))
	# Making the equivalent number of tabs.
	tabs = "\t" * (len(spaces) // 4)
	# Constructing the updated line.
	new_line = tabs + line[len(spaces):]
	# Storing the updated line.
	new_lines.append(new_line)

# Combining the new lines.
new_text = "".join(new_lines)
# Updating the text.
editor.replace_text(*selected_range, new_text)
