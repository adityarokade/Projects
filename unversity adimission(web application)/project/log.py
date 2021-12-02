import logging as lg
def log_info(info1):
    lg.basicConfig(filename="test.log",level=lg.INFO,format='%(asctime)s - %(message)s')
    lg.info(info1)
    return None