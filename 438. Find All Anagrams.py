def findAnagrams(s: str, p: str) -> list[int]:
    if len(s) < len(p):
        return []

    result = []
    p_count = {}
    window_count = {}

    for ch in p:
        p_count[ch] = p_count.get(ch, 0) + 1

    for i in range(len(p)):
        ch = s[i]
        window_count[ch] = window_count.get(ch, 0) + 1

    if window_count == p_count:
        result.append(0)

    for i in range(len(p), len(s)):
        new_ch = s[i]
        window_count[new_ch] = window_count.get(new_ch, 0) + 1

        old_ch = s[i - len(p)]
        window_count[old_ch] -= 1
        if window_count[old_ch] == 0:
            del window_count[old_ch]

        if window_count == p_count:
            result.append(i - len(p) + 1)

    return result