from pathlib import Path
from random import choice


datasets = [
"https://corgis-edu.github.io/corgis/json/video_games/",
"https://corgis-edu.github.io/corgis/json/tate/",
"https://corgis-edu.github.io/corgis/json/smoking/",
"https://corgis-edu.github.io/corgis/json/nuclear_explosions/",
"https://corgis-edu.github.io/corgis/json/earthquakes/",
"https://corgis-edu.github.io/corgis/json/food/",
"https://corgis-edu.github.io/corgis/json/covid/",
"https://corgis-edu.github.io/corgis/json/county_demographics/",
"https://corgis-edu.github.io/corgis/json/cars/",
"https://corgis-edu.github.io/corgis/json/coffee/",
"https://corgis-edu.github.io/corgis/json/classics/",
]

students = []
for name in sorted([p.name for p in Path(".").glob("*") if (p.is_dir() and p.name.find('_')>=0)]):
    if len(datasets) == 0:
        raise RuntimeError("задачи кончились")
    dataset = choice(datasets)
    datasets.remove(dataset)
    print(f"{name} {dataset}")
