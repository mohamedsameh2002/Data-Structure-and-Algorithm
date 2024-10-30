from collections import deque
import queue as q
from multiprocessing import Queue

coll_queue=deque(maxlen=4)
coll_queue.append(1)
coll_queue.append(2)
coll_queue.append(3)
coll_queue.append(4)








queue_q=q.Queue(maxsize=4)
queue_q.put(1)
queue_q.task_done()
queue_q.put(2)
queue_q.task_done()
queue_q.join()#make lock until all task_done is done







multipr_queue=Queue(maxsize=4)
multipr_queue.put(1)
multipr_queue.put(2)
multipr_queue.put(3)










