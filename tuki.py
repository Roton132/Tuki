import platform
import sys

arch = platform.architecture()[0]

if arch != "64bit":
    print("32bit Not Supported! Sorry")
    sys.exit(0)

try:
    import p1_XD
except Exception as e:
    print("Failed to load module:", e)
    sys.exit(1)

# Try common entry points
called = False
for fn in ("main", "run", "start", "menu", "init"):
    if hasattr(p1_XD, fn) and callable(getattr(p1_XD, fn)):
        print(f"Starting: p1_XD.{fn}()")
        getattr(p1_XD, fn)()
        called = True
        break

if not called:
    print("Module loaded but no callable entry point found.")
    print("This module may be locked / demo-only / premium.")
