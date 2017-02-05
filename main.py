from ProjectDB import ProjectDB
from BPlusTree import BPlusTree
import mmap

if __name__ == "__main__":
    #file = open("demo.pdb", "w+b")
    #db = ProjectDB(file)
    #db.start()

    size = 4
    bptree = BPlusTree(size, 'demo.pdb')
    cases1 = [
        ('a', 'Value A'),
        ('b', 'Value B'),
        ('c', 'Value C'),
        ('d', 'Value D')
    ]

    for case in cases1:
        bptree[case[0]] = case[1]


    #with open('lorem.txt', 'r') as f:
    #    with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ, offset=0 * mmap.PAGESIZE) as m:
    #        print('First 10 bytes via read :', m.read(10))
    #        print('First 10 bytes via slice:', m[:10])
    #        m.seek(mmap.PAGESIZE)
    #        print('2nd   10 bytes via read :', m.read(10))

