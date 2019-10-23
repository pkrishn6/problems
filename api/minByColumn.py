# For this interview, imagine that we are working with a simple database. Each row
# associates column names (strings) with integer values (for example: 5, 0, -3,
# and so on). Here's a table with three rows:

#  a   b   c   d
# ---------------
#  1   0   0   0
#  0   2   3   0
#  0   0   0   4

# We can choose to represent a database table in JSON as an array of objects. For
# example, the previous table could be written as:

# [ {"a": 1, "b": 0, "c": 0, "d": 0},
#   {"a": 0, "b": 2, "c": 3, "d": 0},
#   {"a": 0, "b": 0, "c": 0, "d": 4} ]

# (There is no need to use JSON in your solutions -- the notation is just used to
# introduce and explain the problems.)

# Write a function minByColumn that takes a database table (as above), along with a
# column, and returns the row that contains the minimum value for the given column.
# If a row doesn't have any value for the column, it should behave as though the
# value for that column was zero.

# In addition to writing this function, you should use tests to demonstrate that it's
# correct, either via an existing testing system or one you create.

# ## Examples

# table1 = [
#   {"a": 1},
#   {"a": 2},
#   {"a": 3}
# ]
# minByColumn(table1, "a") returns {"a": 1}

# table2 = [
#   {"a": 1},
#   {"a": 3, "b": 0, "c": 3}
# ]
# minByColumn(table2, "b") returns {"a": 3, "b": 0}

# table3 = [
#   {"a": 1, "b": -2},
#   {"a": 3}
# ]
# minByColumn(table3, "b") returns {"a": 1, "b": -2}


# In part 1 you may have noticed that it's possible for two rows to be "tied",
# meaning that either would be an acceptable return value from minByColumn.
# Consider:

# table4 = [
#   {"a": 1, "b": 2},
#   {"a": 1, "b": 3},
#   {"a": 1, "b": 4}
# ]
# minByColumn(table4, "a") returns ???

# Since all three rows have the same value for a, all three rows are acceptable
# candidates to be returned by minByColumn(table, "a").

# In these cases it would be nice if users could specify additional columns (e.g. "b")
# to use as tie-breakers. A tie-breaker would only apply in cases where multiple rows
# share the same minimum value. In `table4` above, the row {"a": 1, "b": 2} is
# tied for the smallest "a" value (1) and of all the tied candidates, it has the
# smallest "b" value (2). If two records had equal values for "a" and also for "b" then
# another tie-breaker (e.g. "c") could be used. When records are tied with respect to
# all columns, either record may be considered the minimum.

# Write a function minByOrder that takes a database table and a list of columns, and
# returns the row with the minimum column values using the tie-breaking logic above.
# If only one column is provided, then the behavior of minByOrder is identical to
# passing that column to minByColumn:

# minByOrder(table, [column]) is equal to minByColumn(table, column)

# As in Part 1, you should use tests to demonstrate that it's correct, either via an
# existing testing system or one you create.

# ## Examples

# table5 = [
#   {"x": 1, "y": 3},
#   {"x": 1, "y": 0}
# ]
# minByOrder(table5, ["x", "y"]) returns {"x": 1, "y": 0}

# table6 = [
#   {"x": 2, "y": 3},
#   {"x": 2, "y": 1},
#   {"x": 1, "y": 10}
# ]
# minByOrder(table6, ["x", "y"]) returns {"x": 1, "y": 10}

# table7 = [
#   {"x": 3, "y": -1, "z": 0},
#   {"x": 1, "y": 10, "z": 1},
#   {"x": 1, "y": 10, "z": 0}
# ]
# minByOrder(table7, ["x", "y", "z"]) returns {"x": 1, "y": 10, "z": 0}

# table8 = [
#   {"x": 1, "y": 2, "z": 3},
#   {"x": 2, "y": 2, "z": 2}
# ]
# minByOrder(table8, ["x", "y", "z"]) returns {"x": 1, "y": 2, "z": 3}

from collections import defaultdict

class MyDict:
    def __init__(self, input):
        self.table = defaultdict(list)

        columns = set()
        for entry in input:
            for key in entry.keys():
                columns.add(key)

        for entry in input:
            for key, val in entry.items():
                self.table[key].append(val)

            for column in columns:
                if column not in entry:
                    self.table[column].append(0)

    def findMin(self, column, start, end):
        if column not in self.table:
            return float("inf")

        column_min = float("inf")
        indexes = [-1]
        collision = False

        for i in range(start, end + 1):
            if self.table[column][i] < column_min:
                column_min = self.table[column][i]
                indexes[0] = i
                collision = False
            elif self.table[column][i] == column_min:
                collision = True
                indexes.append(i)

        assert(indexes[0] != -1)

        return collision, indexes

    def fillResult(self, index):
        result = []

        for key in self.table.keys():
            result.append(self.table[key][index])

        return result

    def minByColumn(self, column, *args):
        collision, indexes = self.findMin(column, 0, len(self.table[column]) - 1)
        if not collision:
            index = indexes[0]

            return self.fillResult(index)

        for arg in args:
            if arg == column:
                continue
            collision, indexes = self.findMin(arg, indexes[0], indexes[-1])

            if collision:
                continue

            return self.fillResult(indexes[0])


        return None



table1 = [ {"a":1}, {"a":3, "b":2, "c":3}]

table2 = [ {"a": 1, "b": 0, "c": 0, "d": 0},
           {"a": 0, "b": 2, "c": 3, "d": 0},
           {"a": 0, "b": 3, "c": 0, "d": 4} ]



db1 = MyDict(table1)
assert(db1.minByColumn("b") == [1, 0, 0])

db2 = MyDict(table2)
print(db2.minByColumn("a", "b"))
assert(db2.minByColumn("a", "b") == [0, 2, 3, 0])
