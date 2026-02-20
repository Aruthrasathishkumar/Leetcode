def isOneEditDistance(s1: str, s2: str) -> bool:
    m, n = len(s1), len(s2)
    if abs(m - n) > 1:
        return False

    i = j = 0
    edits = 0

    while i < m and j < n:
        if s1[i] == s2[j]:
            i += 1
            j += 1
            continue

        if edits == 1:
            return False

        if m > n:        # delete from s1
            i += 1
        elif n > m:      # delete from s2
            j += 1
        else:            # replace
            i += 1
            j += 1

        edits += 1

    # if one string has an extra trailing character
    if i < m or j < n:
        edits += 1

    return edits == 1