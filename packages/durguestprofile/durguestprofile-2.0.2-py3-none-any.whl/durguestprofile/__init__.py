__version__ = "1.1.8"

missing_python = []
try:
    import struct
    version = struct.calcsize("P") * 8
except ImportError as e:
    missing_python.append(f"{version}: {e}")


if version != 64:
    raise ImportError(
        f"Unable to use Python {version}bit version: "
        f"\n Create Python env using 64Bit version." + '\n'.join(missing_python)
    )

# Let users know if they're missing any of our hard dependencies
hard_dependencies = ("dateutil", "pandas", "xlsxwriter", "lxml")
missing_dependencies = []
for dependency in hard_dependencies:
    try:
        __import__(dependency)
    except ImportError as e:
        missing_dependencies.append(f"{dependency}: {e}")

if missing_dependencies:
    raise ImportError(
        "Unable to import required dependencies:\n" + "\n".join(missing_dependencies)
    )
del hard_dependencies, dependency, missing_dependencies

from .functions import properties_score

__all__ = [
    "__version__",
    "properties_score"

]