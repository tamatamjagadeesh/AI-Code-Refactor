def has_too_many_nested_ifs(code, max_nested=2):
    lines = code.splitlines()
    nested_count = 0

    for line in lines:
        stripped = line.strip()
        if stripped.startswith("if "):
            nested_count += 1

    if nested_count > max_nested:
        return True, f"Too many nested if statements: {nested_count}"

    return False, "Code looks fine"
