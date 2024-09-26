def sartorial_splendor(creature, clothing):
    return f"the {creature} in the {clothing}"

# see PEP 570: https://www.python.org/dev/peps/pep-0570/
def sartorial_splendor_only_positional(creature, clothing, /):
    return f"the {creature} in the positional {clothing}"

# see PEP 3102: https://www.python.org/dev/peps/pep-3102/
def sartorial_splendor_only_named(*, creature, clothing):
    return f"the {creature} in the named {clothing}"
