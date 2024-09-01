def test_function():
    x = 'Я в области видимости функции'

    def inner_function(x):
        x = x + ' test_function'
        print(x)

    inner_function(x)


test_function()