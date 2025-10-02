BANNER = """PandA IR — Part 2 (Highlighting + three sonnets)
Type :help for commands. Type :quit to exit."""

HELP = """Commands:
  :help            Show this help text
  :quit            Exit the program
  :highlight on|off
                   Toggle highlighting of matches

Usage:
  Enter a single word to search. Example:
    love

Notes:
  - Case-insensitive search
  - Works over the TITLE and LINES of three sonnets
  - Print only matching sonnets
  - Show: "N out of 3 sonnets contain "<word>"."
  - Use ANSI escape codes for highlighting when enabled
  - Manual substring scan (no str.find, no 'in' for text search, no regex)
"""
