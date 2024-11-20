def test_function():
    def inner_function():
        vision = print('Я в области видимости функции tetst_function')
        return vision
    inner_function()

test_function()
inner_function()