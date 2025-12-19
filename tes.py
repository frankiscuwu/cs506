import os, subprocess

for x in os.listdir('.'):
    if x in [".DS_Store", "tes.py", ".gitignore"]:
        continue
    if not os.path.isdir(x):
        continue
    
    print(x)

    subprocess.run([
        "git", "submodule", "add",
        f"https://github.com/CS506-Boston-University/{x}", x
    ])
