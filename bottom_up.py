""" In this program we were asked to improve the time complexity of 
    an algorithm using Dynamic Programming. The question is included
    in the file 'bottom_up_implementation_question.png'
"""

def line_edits(s1, s2):
    """ takes the previous and current versions of a string and
        applies the edit-distance algorithm to output (operation,
        left_line, right_line)
        Operation;
        'C', 'S', 'D' or 'I' for Copied, Substituted, Deleted and
        Inserted, respectively.
    """
    previous = str.splitlines(s1)
    current = str.splitlines(s2)
    np = len(previous) + 1
    nc = len(current) + 1

    table = [[0] * nc for _ in range(np)]
    operations = [[""] * nc for _ in range(np)]

    for i in range(np):
        table[i][0] = i
        operations[i][0] = "D"

    for j in range(nc):
        table[0][j] = j
        operations[0][j] = "I"

    for i in range(1, np):
        for j in range(1, nc):
            if previous[i - 1] == current[j - 1]:
                table[i][j] = table[i - 1][j - 1]
                operations[i][j] = "C"
            else:
                delete_cost = table[i - 1][j] + 1
                insert_cost = table[i][j - 1] + 1
                substitute_cost = table[i - 1][j - 1] + 1

                min_cost = min(delete_cost, insert_cost, substitute_cost)
                table[i][j] = min_cost

                # Prioritised "S"
                if min_cost == substitute_cost:
                    operations[i][j] = "S"
                elif min_cost == insert_cost:
                    operations[i][j] = "I"
                else:
                    operations[i][j] = "D"

# while loop which implements the line_edits output
    i = np - 1
    j = nc - 1                     
    lines = []
    while i > 0 or j > 0:
        operation = operations[i][j]

        if operation == "C":
            i -= 1
            j -= 1
            lines.append(("C", previous[i], current[j]))
        elif operation == "D":
            lines.append(("D", previous[i - 1], ""))
            i -= 1
        elif operation == "I":
            lines.append(("I", "", current[j - 1]))
            j -= 1
        else:  # "S"
            lines.append(("S", previous[i - 1], current[j - 1]))
            i -= 1
            j -= 1

    return lines[::-1]



# A couple test cases that I used:
# Test 1:
s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line1\nLine3\nLine4\nLine5\n"
table = line_edits(s1, s2)
for row in table:
    print(row)

# Should print:
# ('C', 'Line1', 'Line1')
# ('D', 'Line2', '')
# ('C', 'Line3', 'Line3')
# ('C', 'Line4', 'Line4')
# ('I', '', 'Line5')

# Test 2:
s1 = "Line1\nLine2\nLine3\nLine4\n"
s2 = "Line5\nLine4\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
  
# Should print:
# ('S', 'Line1', 'Line5')
# ('S', 'Line2', 'Line4')
# ('C', 'Line3', 'Line3')
# ('D', 'Line4', '')


