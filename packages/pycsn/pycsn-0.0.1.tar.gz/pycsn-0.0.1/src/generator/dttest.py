import numpy as np

date = np.datetime64('2023-08-23')
newdate = date + np.timedelta64(480+15,'m')
print(newdate)