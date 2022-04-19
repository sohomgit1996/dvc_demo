from genericpath import exists
import os

#for creating directories
dirs=[
     os.path.join("data","raw"),
     os.path.join("data","processed"),
     "notebooks",
     "saved_models",
     "src"

]

#we are making directory using above names and then creating a .gitkeepfile for each directory
for dir in dirs:
    os.makedirs(dir,exist_ok=True)
    with open(os.path.join(dir, ".gitkeep"),"w") as f:
        pass

#for creating files inside directories
files=[
    "dvc.yaml",
    "params.yaml",
    ".gitignore",
    os.path.join("src","__init__.py"),
    "README.md"
]

for f in files:
    with open(f,"w") as f1:
        pass

