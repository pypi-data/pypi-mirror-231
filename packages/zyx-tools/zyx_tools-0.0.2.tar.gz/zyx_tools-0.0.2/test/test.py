import sys
sys.path.append("../../tools")
from zyx_tools import FileTool
def Test():
    FileTool.copy_file("dd","dd")

if __name__ == "__main__":
    Test()