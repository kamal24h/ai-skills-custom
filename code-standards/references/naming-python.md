# Python Naming Conventions

From PEP 8, the official Python style guide. "A foolproof consistency read" — internal consistency matters most; PEP 8 is the public default.

## Element table

| Element | Convention | Example |
|---|---|---|
| Module | short all-lowercase, underscores discouraged but allowed (no hyphens) | `invoice_parser.py` |
| Package | short all-lowercase, no underscores preferred | `billing` |
| Class / exception | CapWords; exceptions suffixed `Error` if actually raised as errors | `InvoiceParser`, `PaymentError` |
| Function / method / variable / argument | lower_snake_case | `calculate_total()` |
| Constant (module level) | UPPER_SNAKE_CASE | `MAX_RETRIES = 5` |
| Protected/internal member | single leading underscore | `self._cache` |
| Name-mangled (private) class attr | double leading underscore (only inside classes) | `self.__secret` |
| Dunder names | reserved — never invent your own `__x__` | `__init__` |
| First parameter of methods / classmethods | `self` / `cls` | — |
| Type variable | short CapWords | `T`, `AnyStr` |
| Boolean-returning function | predicate reading (`is_`, `has_`) *(community convention)* | `is_expired()` |
| Test function / module | `test_*` prefix | `test_checkout_empty_cart()` |

## Rules worth remembering

- Never use `l` (lowercase L), `O` (uppercase o), or `I` alone as identifiers.
- `_` alone is the throwaway name for unused unpacking values: `_, total = fetch()`.
- Public vs non-public is by underscore convention plus docstrings — Python has no true private.

## Sources

- [PEP 8 — Style Guide for Python Code](https://peps.python.org/pep-0008/)
- [PEP 8 — Naming Conventions section](https://peps.python.org/pep-0008/#naming-conventions)
