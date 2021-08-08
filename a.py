import os
print("before: %s"%os.getcwd())
os.chdir("/work_dir")
print("after: %s"%os.getcwd())