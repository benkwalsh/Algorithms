""" In this program we were asked to improve the time complexity of 
    an algorithm using Dynamic Programming. The question is included
    in the file 'bottom_up_implementation_question.pdf'
"""

def lcs(s1, s2):
    """ returns the maximum length subsequence of the
        two strings s1 and s2. 
    """
    n1 = len(s1) 
    n2 = len(s2)
    table = [(n2 + 1) * [0] for _ in range(n1 + 1)]

    for i in range(n1 + 1):
        for j in range(n2 + 1):
            if i == 0 or j == 0:
                table[i][j] = 0
            elif s1[i-1] == s2[j-1]:
                table[i][j] = (table[i-1][j-1]) + 1
            else: # s1[i] != s2[j]
                table[i][j] = max(table[i][j-1], table[i-1][j], table[i-1][j-1])
    
    subseq = ""
    i = n1
    j = n2 
    while i > 0 and j > 0:
        if s1[i-1] == s2[j-1]:
            subseq += s1[i-1]
            i -= 1
            j -= 1
        else:
            if table[i-1][j] >= table[i][j-1]:
                i -= 1
            else:
                j -= 1

    return subseq[::-1]


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

    
# Implementing the output of line_edits and lcs:
    i = np - 1
    j = nc - 1                     
    lines = []
    while i > 0 and j > 0:
        operation = operations[i][j]

        if operation == "C":
            lines.append(("C", previous[i - 1], current[j - 1]))
            i -= 1
            j -= 1
        elif operation == "D":
            lines.append(("D", previous[i - 1], ""))
            i -= 1
        elif operation == "I":
            lines.append(("I", "", current[j - 1]))
            j -= 1
        else:  # "S"
            left = ""
            right = ""

            lcsubseq = lcs(previous[i - 1], current[j - 1])
            for c in previous[i - 1]: # left 
                if len(lcsubseq) > 0 and lcsubseq[0] == c:
                    lcsubseq = lcsubseq[1:]
                    left += c
                else:
                    left += f"[[{c}]]"

            lcsubseq = lcs(previous[i - 1], current[j - 1]) 
            for c in current[j - 1]: # right
                if len(lcsubseq) > 0 and lcsubseq[0] == c:
                    lcsubseq = lcsubseq[1:]
                    right += c
                else:
                    right += f"[[{c}]]"
            
            lines.append(("S", left, right))
            i -= 1
            j -= 1

    return lines[::-1]


# A test case that I used:
s1 = "Line1\nLine 2a\nLine3\nLine4\n"
s2 = "Line5\nline2\nLine3\n"
table = line_edits(s1, s2)
for row in table:
    print(row)
    
# Should print:
# ('S', 'Line[[1]]', 'Line[[5]]')
# ('S', '[[L]]ine[[ ]]2[[a]]', '[[l]]ine2')
# ('C', 'Line3', 'Line3')
# ('D', 'Line4', '')
