from soal_3 import Queue

def main():
    queue = Queue()
    print("\n=========================================")
    queue.enqueue("Order 1")
    queue.enqueue("Order 2")
    queue.enqueue("Order 3")

    print("\n=========================================")
    queue.tampilan()
    queue.dequeue()
    queue.dequeue()
    
 
    print("\n=========================================")
    queue.tampilan()
    

    main()