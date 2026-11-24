"""How Many Tabs Do You Have Open? — make.fun bounty entry.

The honest count is 187 open browser tabs: a main research window
that never gets closed, a second window of half-finished projects,
and a third of things saved "to read later" and never read.
"""

# Counted window by window, not guessed: 96 + 54 + 37 = 187.
TABS_BY_WINDOW = [96, 54, 37]
TABS_OPEN = sum(TABS_BY_WINDOW)

if __name__ == "__main__":
    print(TABS_OPEN)
