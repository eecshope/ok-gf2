import ok
from config import config

if __name__ == '__main__':
    config = config
    ok = ok.OK(config)
    ok.start()
