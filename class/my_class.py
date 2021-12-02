class MyClass:

    def __init__(self, att):
        self.my_attribute = "Hello World!"
        self.my_attribute_2 = att

    def my_method(self):
        print("I am here in the first method")
        print(self.my_attribute)
        print(self.my_attribute_2)

    def my_method_two(self, num, mult):
        return num * mult

# instance of class
obj = MyClass("my_attribute_2")

# using the attribute
print(obj.my_attribute)
print(obj.my_attribute_2)

# using the methods
obj.my_method()
result = obj.my_method_two(num=2, mult=3)
print(result)
