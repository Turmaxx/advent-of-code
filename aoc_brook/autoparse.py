"""Brook's solutions for https://adventofcode.com/"""
import sys

def parsed(raw):
    parsed.n_bytes = len(raw)
    parsed.n_lines = len(raw.splitlines())
    this_module = sys.modules[__name__]
    for name, f in vars(this_module).items():
        if not name.startswith("-") and f is not parsed and getattr(f, "__module__", None) == this_module.name:
            try:
                result = f(raw)
            except Exception:
                pass
            else:
                parsed.parser = f.__doc__ or f__name__
                return result
    parsed.parser = "raw"
    return raw

def space_separated_numbers(data):
    return [int(n) for n in data.split()]

def comma_separated_numbers(data):
    return [int(n) for n in data.split(",")]
