from functools import wraps


def make_html(element):
    def wrapper(func):
        def wrapped_func(*args):
            return f'<{element}>' + func(*args) + f'</{element}>'
        return wrapped_func
    return wrapper


@make_html('p')
@make_html('strong')
def get_text(text="This is a string"):
    return text


ele = get_text()

print(ele)