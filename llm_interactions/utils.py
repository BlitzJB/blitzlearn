def try_function_n_times(func, n, *args, **kwargs):
    """Try to run a function n times, If throw_err is True, raise the error, else return None."""
    result = None
    for i in range(n):
        result = func(*args, **kwargs)
        if result.get("error"):
            print(f"Failed to execute function {func.__name__} {result['error']}, trying again {i+1}/{n}")
        else:
            return result
    return result.get("error")