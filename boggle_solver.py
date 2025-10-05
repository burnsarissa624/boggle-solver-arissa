"""
Name: Arissa Burns
SID: [003103878]

Boggle Solver
-------------
Finds all valid words in an NxN grid of letters based on Boggle rules.
 Words must use adjacent tiles (including diagonals)
 Each word may not reuse a cube
Words must be at least 3 letters long
Special tiles ("Qu", "St", "Ie") each count as two letters
"""

class Boggle:
    def __init__(self, grid, dictionary):
        # Convert grid and dictionary to uppercase for consistent comparison
        self.grid = [[cell.upper() for cell in row] for row in grid]
        self.dictionary = [word.upper() for word in dictionary]
        self.solutions = []

    def setGrid(self, grid):
        # Reset grid, convert to uppercase
        self.grid = [[cell.upper() for cell in row] for row in grid]

    def setDictionary(self, dictionary):
        # Reset dictionary, converting to uppercase
        self.dictionary = [word.upper() for word in dictionary]

    def getSolution(self):
        """Return all valid words found in the grid."""
        found = set()
        rows, cols = len(self.grid), len(self.grid[0])

        for r in range(rows):
            for c in range(cols):
                self._dfs(r, c, self.grid[r][c], {(r, c)}, found)

        # Only keep dictionary words length ≥ 3
        valid = [w for w in found if w in self.dictionary and len(w) >= 3]
        self.solutions = sorted(valid)

        # Return lowercase words for neat output
        return [w.lower() for w in self.solutions]

    def _dfs(self, r, c, prefix, visited, found):
        """Depth-first search to explore all paths."""
        rows, cols = len(self.grid), len(self.grid[0])

        # Stop early if no dictionary word starts with prefix
        if not any(word.startswith(prefix) for word in self.dictionary):
            return

        # Valid word found
        if prefix in self.dictionary:
            found.add(prefix)

        # Explore all 8 neighbors (including diagonals)
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                if dr == 0 and dc == 0:
                    continue
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                    new_visited = visited.copy()
                    new_visited.add((nr, nc))
                    self._dfs(nr, nc, prefix + self.grid[nr][nc], new_visited, found)


def main():
    grid = [["T", "W", "Y", "R"],
            ["E", "N", "P", "H"],
            ["G", "St", "Qu", "R"],
            ["O", "N", "T", "A"]]

    dictionary = ["art", "ego", "gent", "get", "net", "new", "newt", "prat",
                  "pry", "qua", "quart", "quartz", "rat", "tar", "tarp", "ten",
                  "went", "wet", "arty", "rhr", "not", "quar"]

    mygame = Boggle(grid, dictionary)
    print(mygame.getSolution())


if __name__ == "__main__":
    main()
