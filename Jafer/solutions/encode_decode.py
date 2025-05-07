def encode(self, strs: List[str]) -> str:
    # Store each string as-is, but delimit them with a special character
    # We'll use a hyphen as our special character
    # To avoid confusion, we'll escape hyphens with a backslash
    # Similarly, we'll escape backslashes as well
    encodedString = ""
    for string in strs:
        for character in string:
            if character in ("/", "-"):
                encodedString += "/"
            encodedString += character
        encodedString += "-"
    return encodedString

def decode(self, s: str) -> List[str]:
    strs = []
    currentString = ""
    index = 0
    for index in range(len(s)):
        if s[index] == "-":
            # End of a string
            strs.append(currentString)
            currentString = ""
            index = index + 1
        elif s[index] == "/":
            # The next letter must be escaped
            currentString += s[index+1]
            index = index + 2
        else:
            currentString += s[index]
            index = index + 1
    return strs
