from pathlib import Path
from random import choice

mockups = [str(m) for m in Path('mockups').glob('*')]

students = []
for name in [p.name for p in Path(".").glob("*") if (p.is_dir() and p.name.find('_')>=0)]:
    if len(mockups) == 0:
        raise RuntimeError("задачи кончились")
    mockup = choice(mockups)
    mockups.remove(mockup)
    print(f"{name} [{mockup}](https://github.com/alexanderustinov/ui-test/tree/main/{mockup})")
