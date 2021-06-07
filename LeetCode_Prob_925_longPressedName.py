def isLongPressedName(name, typed):
        curr, alt = 0, 0
        name_end = len(name)
        typed_end = len(typed)
        prev = ""
        while curr < name_end and alt < typed_end:
            # print(f"prev {prev}, name {name[curr]}, typed {typed[alt]}")
            if (prev == "" or prev == typed[alt] or prev != typed[alt]) and (name[curr] == typed[alt]):
                prev = typed[alt]
                alt += 1
                curr += 1
            elif prev == typed[alt] and (name[curr] != typed[alt]):
                prev = typed[alt]
                alt += 1
            else:
                return False
        # print("End of Loop")
        # print(f"Remaining in name: {name[curr:]}")
        # print(f"Remaining in typed: {typed[alt:]}")
        if name[curr:]:
            return False
        for pending in typed[alt:]:
            if pending != prev:
                return False
        return True

# print(isLongPressedName("alex", "aaleex"))
# print(isLongPressedName("saeed", "ssaaedd"))
# print(isLongPressedName("leelee", "lleeeleee"))
# print(isLongPressedName("laiden", "laiden"))
# print(isLongPressedName("alex", "aaleexa"))
print(isLongPressedName("vtkgn", "vttkgnn"))