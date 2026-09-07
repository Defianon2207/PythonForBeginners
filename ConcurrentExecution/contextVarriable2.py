from contextvars import ContextVar, copy_context

user = ContextVar("user", default="Guest")
user.set("Rahul")

ctx = copy_context()


def work():
    print("At beginning:", user.get())

    user.set("Amit")

    print("After change:", user.get())

    return "Work completed"


result = ctx.run(work)

print("Result:", result)
print("Inside copied context:", ctx[user])
print("Outside context:", user.get())