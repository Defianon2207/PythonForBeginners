from multiprocessing import Process, Pipe

def f(conn):
    conn.send([42, None, 'hello'])
    conn.close()

if __name__ == '__main__':
    parent_conn, child_conn = Pipe()

    p = Process(target=f, args=(child_conn,))
    p.start()

    print(parent_conn.recv())
    p.join()

    #By default pipes are duplex i.e 2 ways 
    # You can make it one way by using this receiving_conn, sending_conn = Pipe(duplex=False)