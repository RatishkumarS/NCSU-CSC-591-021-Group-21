from num import NUM
from sym import SYM


# Create a class and define a constructor
class COLS:
    def __init__(self, row):
        # Initialize all of the values of empty list
        self.x, self.y, self.all_cols = [], [], []
        # Get the names of row cells
        self.klass, self.names = None, row.cells

        for at, txt in enumerate(row.cells):
            # Check whether the col value belongs to NUM or SYM
            col = (NUM if txt[0].isalpha() and txt[0].isupper() else SYM)(txt, at)
            self.all_cols.append(col)
            if not txt.endswith("X"):
                if txt.endswith("!"):
                    self.klass = col
                (self.y if txt.endswith(("!", "-", "+")) else self.x).append(col)

    # Update
    def add(self, row):
        # Iterate through all value
        for cols in [self.x, self.y]:
            for col in cols:
                col.add(row.cells[col.at])
        return row
