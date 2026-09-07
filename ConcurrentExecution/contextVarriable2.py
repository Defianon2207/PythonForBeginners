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

# A context cannot be entered again while it is already active:
# from contextvars import Context
# ctx = Context()
# def inner():
# ctx.run(lambda: print("Running again"))
# ctx.run(inner)

# iter(context)

# Iterates over the variables:

# for variable in ctx:
#     print(variable.name)

# Equivalent explicit form:

# for variable in iter(ctx):
#     print(variable.name)
# len(context)

# Returns the number of variables explicitly stored:

# print(len(ctx))

# The attached text says len(proxy), but in this section it means:

# len(context)
# keys()

# Returns all stored ContextVar objects:

# for variable in ctx.keys():
#     print(variable.name)
# values()

# Returns all stored values:

# for value in ctx.values():
#     print(value)
# items()

# Returns variable-value pairs:

# for variable, value in ctx.items():
#     print(f"{variable.name} = {value}")
# 21. ContextVar versus threading.local()

# threading.local() stores different values for different threads:
