# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


# this function get three parameters and sum them up.
def f(x: int, y: float, z):
    return x + y + z


# this function get  function "f" and three other parameters and checks if the parameters are sutable
# for the function f and it appears in the right format  if yes the function calls it
def safe_call(f, x, y, z):
    if type(x) is not int:
        raise Exception("Sorry, x should be integer")
        return
    elif type(y) is not float:
        raise Exception("Sorry, y should be float")
        return
    else:
        result = f(x, y, z)
    return result





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(safe_call(f, x=5, y=2.0, z=3))
    print(safe_call(f, x="abc", y=2.0, z=3))
    print(safe_call(f, x=5, y="abc", z=3))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
