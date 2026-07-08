import sys
import atexit
import threading

    ## this Function is used to demonstrate the Exception Handling in Python with
    ## try and except blocks how context is handled and stored in the Exception object and how it can be accessed using the __context__ attribute of the Exception object.
def exampleOfExceptionHandling():
        try:
            X = int(input("Enter a number: "))
            Y = int(input("Enter another number: "))
            result = X / Y
            print("Result:", result)
        except ZeroDivisionError as e:
            print("is this printed",e)
            try:
                K = int("abc")  # This will raise a ValueError
            except ValueError as ve:
                print("Value Error raised during the DivisionByZero *****", ve.__context__)

def exampleOfExceptionNotBeingHandled():
        try:
            Toys   = int(input("Enter total Toys available on Inventory: "))
            Orders = int(input("Enter total Orders received: "))
            if Orders > Toys:
                raise ValueError("Orders cannot be greater than Toys available in Inventory")
        except ValueError as e:
            print("Value Error raised during the Order Processing *****", e.__context__)
            return e

def exampleOfExceptionWithCause():
        try:
            Y = int(input("Enter a number: "))
            print("This is the magical number", Y)
        except ValueError as e:
            print("Attribute Error raised during the Order Processing *****", e.__cause__)
            try:
                 raise AttributeError("Object has no name") from e
            except AttributeError as ae:
                print("Cause:", ae.__cause__)
                print("Context:", ae.__context__)
                return ae

def assertExample():
    try:
        A = int(input("Enter a number: "))
        B = int(input("Enter another number: "))
        assert B != 0, "B cannot be zero"
    except AssertionError as e:
        print("Assertion Error:")

def attributeErrorExample():
    try:
        student = {}  # This will raise an AttributeError
        student["name"] = "John Doe"
        student["age"] = 20
        print(student)
        student["grade"]
        
    except Exception as e:
                print("Error:", type(e).__name__, e)
                return e

def endOfFileExample():
    try:
        name = input("Enter your name: ")
    except Exception as e:
        print("Error:", type(e).__name__)

def numbersExample():
    print("Starting to print the number")
    try:
      
        yield 1
        yield 2
    finally:
        print("Cleaning up")

def loadHugeFile():
    try:
        with open("random.txt", "r") as file:
            x = 0
            for line in file:
                yield line.strip()
                x += 1
                if x >= 10:  # Limit to 10 lines for demonstration
                    break

    except Exception as e:
        print("Error:", type(e).__name__)

def memoryExceptionError():
    try:
        print("Attempting to create a large list...")   
        largeList = [0] * (10**16)  # Attempt to create a large list
    except Exception as e:
        print("Memory Error:", type(e).__name__)
        return e

def pythonFinalizerExample():
    try:
        print("Attempting to finalize resources...")
    except Exception as e:
        print("Finalization Error:", type(e).__name__)

def cleanUp():
    print("Cleaning up resources...")   
    t = threading.Thread(target=lambda:print("hello")).start()
    atexit.register(cleanUp)
    print("Program is exiting...")

def stopInteration():
    try:
        Dues =[100,120,102,209,99,102,340,543,853,453,234,123,456,789,234,567,890]
        i = iter(Dues)
        while True:
            print(next(i))
        print("Attempting to stop iteration...")
    except Exception as e:
        print("StopIteration Error:", type(e).__name__)

def main():
    if __name__ == "__main__":
     print(__name__)
     x = 100
     isInstance = isinstance(x, int)
     print("Is x an instance of int?", isInstance)
     print((x+3j).conjugate())
     print(24.Rational(3, 4).limit_denominator(10))
    ## exampleOfExceptionHandling() #Example of Exception Handling with context
    ## Returnvalue = exampleOfExceptionNotBeingHandled() 
    ##print("!!! This is the return value !!!",Returnvalue) #Example of Exception Not Being Handled with context
    ## exampleOfExceptionWithCause() #Example of Exception with Cause
    # returnValue = exampleOfExceptionWithCause()
    # print("!!! This is the return value !!!",returnValue,",", returnValue.__cause__,",", returnValue.__context__) #Example of Exception with Cause
    # assertExample() #Example of AssertionError
    # z =  attributeErrorExample()
    # print("!!! This is the return value !!!",z,",", z.__cause__,",", z.__context__) #Example of AttributeError
    # endOfFileExample() #Example of EndOfFileError

#Module Not Found and ImportError -> these are the common errors hence not adding example for them
# Memory Error  and Name Error
    # g = loadHugeFile()
    # for line in g:
    #     print(line)
    # z = memoryExceptionError()
    # cleanUp()
    # stopInteration()


main()

