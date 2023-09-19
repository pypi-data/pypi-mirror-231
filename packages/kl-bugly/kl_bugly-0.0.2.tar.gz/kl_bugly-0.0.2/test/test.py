import sys
sys.path.append("../../bugly")
from kl_bugly import BuglyHelper 


helper=BuglyHelper(379192283)
def Test():
    helper.get_appinfo_by_id()

if __name__ == "__main__":
    Test()