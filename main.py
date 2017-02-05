from ProjectDB import ProjectDB
import mmap

if __name__ == "__main__":
    #file = open("demo.pdb", "w+b")
    #db = ProjectDB(file)
    #db.start()

    print(mmap.PAGESIZE)

    with open('lorem.txt', 'r') as f:
        with mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ, offset=0 * mmap.PAGESIZE) as m:
            print('First 10 bytes via read :', m.read(10))
            print('First 10 bytes via slice:', m[:10])
            m.seek(mmap.PAGESIZE)
            print('2nd   10 bytes via read :', m.read(10))

