from functools import partial
from IPython.core import page
from skbio import DNA
page.page = print
import matplotlib.pyplot as plt

seq_lengths = range(25)
s2_times = [t ** 2 for t in range(25)]

plt.plot(range(25), s2_times)
plt.xlabel('Sequence Length')
plt.ylabel('Runtime (s)')
s3_times = [t ** 3 for t in range(25)]

plt.plot(range(25), s3_times)
plt.xlabel('Sequence Length')
plt.ylabel('Runtime (s)')
plt.plot(range(25), s2_times)
plt.plot(range(25), s3_times)
plt.xlabel('Sequence Length')
plt.ylabel('Runtime (s)')
s4_times = [t ** 4 for t in range(25)]

plt.plot(range(25), s2_times)
plt.plot(range(25), s3_times)
plt.plot(range(25), s4_times)
plt.xlabel('Sequence Length')
plt.ylabel('Runtime (s)')
from skbio import DNA
psource DNA.iter_kmers