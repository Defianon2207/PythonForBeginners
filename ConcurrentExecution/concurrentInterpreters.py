from concurrent import interpreters

first = interpreters.create()
second = interpreters.create()

first.exec("""
message = "Created inside the first interpreter"
print(message)
""")

second.exec("""
try:
    print(message)
except NameError:
    print("The second interpreter cannot see message")
""")

first.close()
second.close()