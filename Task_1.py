s = input()

while ("()" in s) or ("[]" in s) or ("{}" in s):
    s = s.replace("()", "")
    s = s.replace("[]", "")
    s = s.replace("{}", "")

if (len(s) == 0):
    print("true")
else:
    print("false")