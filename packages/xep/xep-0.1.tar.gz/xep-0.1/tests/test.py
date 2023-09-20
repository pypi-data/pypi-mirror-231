from xep.new import make_report

import pickle

with open("3711551.pkl", "rb") as fd:
    stats = pickle.load(fd)

buffer = make_report("viewability.xlsx", stats)

with open("report.xlsx", "wb") as fd:
    fd.write(buffer.getvalue())
