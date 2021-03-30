import os

dirs = [
    os.path.join("data","raw"),   #this is same as "data\raw" we use 'os.path.join()' because everyone has different OS.
    os.path.join("data","processed"),
    "notebooks",
    "saved_models",
    "src"
]

for dir in dirs:
    os.makedirs(dir, exist_ok=True) #by making exist_ok=True if a folder is already present os.path.join will not create folder
    with open(os.path.join(dir,".gitkeep"), "w") as f: # creating gitkeep file in every folder
        pass

files = [
    "dvc.yaml",
    "params.yaml",
    "gitignore",
    os.path.join("src","__init__.py")
]

for file in files:
    with open(file,"w") as f: #creating all the files
        pass