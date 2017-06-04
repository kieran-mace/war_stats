import numpy as np
import pandas as pd
from game import *

g = [Game(2) for i in range(0,10000)]
[i.play() for i in g]
all = [(i.winner, np.mean(i.p0_start), np.mean(i.p1_start), i.num_turns) for i in g]
all_df = pd.DataFrame.from_records(all)
all_df.to_csv('results.csv')
