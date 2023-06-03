# Names

## PackageName

```python
# This is free and unencumbered software released into the public domain.
#
# Anyone is free to copy, modify, publish, use, compile, sell, or
# distribute this software, either in source code form or as a compiled
# binary, for any purpose, commercial or non-commercial, and by any
# means.

import os
import errno

def PackageNameToPath(cwd: str, name: list[str]) -> str:
    path: str = cwd
    start: int = 0
    end: int = len(name)

    while start < len(name):
        folder: str = ".".join(name[start:end])

        if os.path.isdir(path + "/" + folder):
            path += "/" + folder
            start = end
            end = len(name)
        else:
            end -= 1

            if end <= start:
                raise FileNotFoundError(errno.ENOENT, os.strerror(errno.ENOENT), path + "/" + folder)

    return path
```

## ImportName

## PackageOrTypeName
