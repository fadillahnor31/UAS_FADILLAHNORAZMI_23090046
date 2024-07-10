class Queue:
    def _init_(self):
        self.queue = []

    def enqueue(self, order):
        self.queue.append(order)
        print(f"Order '{order}' di tambahkan.")

    def dequeue(self):
        if len(self.queue) < 1:
            return "Queue is empty"
        order = self.queue.pop(0)
        print(f"Order '{order}' dihapus.")
        return order

    def tampilan(self):
        print(f"Antrian saat ini: {self.queue}")