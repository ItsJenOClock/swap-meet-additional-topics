class DunderExamples:
    def __init__(self, lower=0, upper=10):
        self.lower = lower
        self.upper = upper

    # if our instance needs to be stringified (converted to a string),
    # Python calls this method
    def __str__(self):
        return f"lower: {self.lower}, upper: {self.upper}"

    # python calls this method when it needs something a little more
    # "debug-y". Usually should return something that could be
    # copy-pasted into Python code to make an equivalent object
    def __repr__(self):
        return f"DunderExample({self.lower}, {self.upper})"

    # if we use the in operator, Python calls this method
    def __contains__(self, item):
        return self.lower <= item <= self.upper

    # if we perform an == comparison, Python calls this method
    def __eq__(self, other):
        return self.lower == other.lower and self.upper == other.upper

# There are MANY dunder methods we can implement to make
# our objects act more like standard Python objects
# https://docs.python.org/3/reference/datamodel.html#basic-customization