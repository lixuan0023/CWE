import struct
import math
import numpy as np
buf = bytearray()

ar = [[0.1,0.2,0.3],[1.11111,0.22222,9.9999],[11111.2222,2.33333,3.6666]]

for i in range(3):
	buf += struct.pack("=ddd",ar[i][0],ar[i][1],ar[i][2])

# dtype=np.dtype({"name":["id","sin","cos"],"formats":["h","d","d"]})
data = np.frombuffer(buf,dtype=np.float).reshape(3,3)
print(data)