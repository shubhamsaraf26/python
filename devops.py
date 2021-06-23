import os

cwd=os.getcwd()
print(cwd)

os.chdir('../')
print(os.getcwd())

os.chdir('F:\devops\python')

directory="a"
parent='F:\devops\python'

path=os.path.join(parent,directory)

os.mkdir(path)

print(os.listdir())
