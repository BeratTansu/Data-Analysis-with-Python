#%% chapter_1/09-modules/module_contents.py
"""
Combined module examples for the 'Modules' chapter.

This single file contains:
 - import styles (import, from ... import, import as)
 - module lookup (sys.path) and dynamic import (importlib)
 - package / folder correspondence and pkgutil usage
 - examples and notes about best practices
 - module contents: module-level attributes, module.__dict__/globals(), dir() demo
 - the recommended if __name__ == "__main__" idiom and a main() demo

Place this file in chapter_1/09-modules. It is safe to import (top-level side-effects are minimal).
Run it as a script to see the demo output.
"""

#%% 0) Standard imports used across examples
import importlib
import math
import os
import pkgutil
import sys
from typing import Dict, Any

#%% 1) Basic imports and usage (fully-qualified names)
def demo_basic_imports() -> None:
    print("=== Basic imports demo ===")
    print("math.cos(0) ->", math.cos(0))
    print("os.name ->", os.name)
    print()

#%% 2) Breaking the namespace: from ... import and aliasing
def demo_from_imports() -> None:
    print("=== from ... import and alias demo ===")
    from math import cos, pi
    print("cos(1) ->", cos(1))
    from math import sin as s
    print("s(pi/2) ->", s(pi / 2))
    import math as m
    print("m.cos(0) ->", m.cos(0))
    print()

#%% 3) Module lookup: sys.path and import order
def demo_module_lookup() -> None:
    print("=== Module lookup (sys.path) demo ===")
    print("sys.path[0] (current directory):", sys.path[0] if sys.path else "(empty)")
    print("len(sys.path) ->", len(sys.path))
    print("- Note: Python checks builtin modules first, then searches files in sys.path directories.")
    print()

#%% 4) Dynamic import with importlib
def demo_dynamic_import() -> None:
    print("=== Dynamic import demo (importlib) ===")
    math_mod = importlib.import_module("math")
    print("importlib.import_module('math').sin(0) ->", math_mod.sin(0))
    # dynamic module by name (example)
    mod_name = "os"
    dyn = importlib.import_module(mod_name)
    print(f"dynamic import of {mod_name} succeeded, hasattr(os, 'path') ->", hasattr(dyn, "path"))
    print()

#%% 5) Inspecting available modules in a package using pkgutil
def demo_pkgutil() -> None:
    print("=== pkgutil.iter_modules demo (may vary by environment) ===")
    # pkgutil.iter_modules expects a package __path__ (list). Many stdlib modules are builtins and won't list children.
    target = os
    if hasattr(target, "__path__") and target.__path__:
        for finder, name, ispkg in pkgutil.iter_modules(target.__path__):
            print("found in os package:", name, "ispkg:", ispkg)
    else:
        print("Target module (os) has no __path__ to iterate; try with a pure-Python package locally.")
    print()

#%% 6) Package import forms, aliasing and module hierarchy notes
def demo_package_notes() -> None:
    print("=== Package import forms & notes ===")
    print("Examples of import forms:")
    print("  import package                      # imports top-level package")
    print("  import package.module               # imports package and package.module")
    print("  from package import subpackage      # brings subpackage name into scope")
    print("  from package.subpackage import mod  # imports submodule into scope")
    print("Aliasing: from numpy.linalg import linalg as lin (example for long names)")
    print("Avoid: from package import *   # pollutes namespace and is discouraged")
    print()

#%% 7) Correspondence between folders and module/package hierarchies (explanation)
def package_layout_doc() -> None:
    print("=== Package-folder correspondence (doc) ===")
    print("Example layout:")
    print("  a/")
    print("    __init__.py    -> makes 'a' a package")
    print("    b.py           -> module a.b")
    print("    c/")
    print("      __init__.py  -> subpackage a.c")
    print("      d.py         -> module a.c.d")
    print("      e.py         -> module a.c.e")
    print("Import behavior recap:")
    print("  import a           # executes a/__init__.py")
    print("  import a.b         # imports a then a.b")
    print("  from a.c import d  # imports a.c then loads a.c.d")
    print()

#%% 8) Best practices & notes about imports
def import_best_practices() -> None:
    print("=== Import best practices ===")
    print("- Prefer 'import module' for clarity.")
    print("- Use 'from module import name' when the imported name is unambiguous and improves readability.")
    print("- Avoid 'from module import *'.")
    print("- Use 'import x as y' sparingly (e.g., import numpy as np).")
    print("- Keep modules small and focused; use packages to group related modules.")
    print()

#%% 9) Module contents: attributes, globals(), module.__dict__, dir()
# Top-level attributes that become attributes of this module when imported
a = 5
__version__ = "0.1.0"
__author__ = "BeratTansu (example)"

def f(i: int) -> int:
    """Simple function attribute: increments its argument by 1."""
    return i + 1

def module_attributes() -> Dict[str, Any]:
    """
    Return a dictionary with a selection of useful module attributes.
    Demonstrates that modules store their attributes in a mapping (module.__dict__).
    """
    g = globals().copy()
    # Select a few attributes to show (may include None if undefined)
    keys = ["__name__", "__file__", "__package__", "__doc__", "__version__", "__author__", "a", "f"]
    return {k: g.get(k) for k in keys}

def show_dir() -> None:
    """
    Print a compact listing similar to what `dir(module)` would show.
    Useful when running the module as a script to inspect its attributes.
    """
    import sys
    mod_name = __name__
    try:
        mod = sys.modules[mod_name]
        names = sorted(name for name in dir(mod) if not name.startswith("__") or name in ("__name__", "__file__"))
    except KeyError:
        names = sorted(name for name in globals().keys())
    print("Attributes on module", mod_name, "->", names)

#%% 10) main() demo showing recommended pattern (no top-level side-effects)
def main() -> None:
    """
    Demo main function: shows how to provide top-level functionality without executing on import.
    """
    print("=== module_contents main() demo ===")
    demo_basic_imports()
    demo_from_imports()
    demo_module_lookup()
    demo_dynamic_import()
    demo_pkgutil()
    demo_package_notes()
    import_best_practices()

    print("=== module attribute snapshot ===")
    for k, v in module_attributes().items():
        print(f"    {k!s:12} -> {v!r}")
    print()
    show_dir()
    print()
    print("Calling f(10) ->", f(10))
    print()
    print("A short for-loop demonstrating code that would otherwise execute on import:")
    for _ in range(3):
        print(" Hello (inside main)")
    print()

#%% 11) If executed as script, run main(); if imported, nothing runs automatically.
if __name__ == "__main__":
    main()