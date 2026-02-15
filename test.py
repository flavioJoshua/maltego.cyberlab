from objbrowser import browse
a = 67; pi = 3.1415 
browse(locals())


class MyClass:
    def __new__(cls, *args, **kwargs):
        print("MyClass __new__ called")
        instance = super(MyClass, cls).__new__(cls)
        return instance

    def __init__(self, value):
        print("MyClass __init__ called")
        self.value = value
