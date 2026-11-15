"""
Question 1 - Circular Queue (array based)

A circular queue reuses freed slots by letting `front` and `rear`
wrap around the end of the array using the modulo operator.

We keep a separate `size` counter so that ALL `capacity` slots are usable
(the classic "one empty slot" trick is not needed) and so that the
full / empty tests are unambiguous.
"""


class CircularQueue:
    def __init__(self, capacity: int):
        if capacity <= 0:
            raise ValueError("capacity must be positive")
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0      # index of the first element
        self.rear = -1      # index of the last element
        self.size = 0       # number of stored elements

    def is_empty(self) -> bool:
        return self.size == 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def enqueue(self, item) -> None:
        if self.is_full():
            raise OverflowError("Queue Overflow: circular queue is full")
        self.rear = (self.rear + 1) % self.capacity   # wrap-around
        self.data[self.rear] = item
        self.size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue Underflow: circular queue is empty")
        item = self.data[self.front]
        self.data[self.front] = None                  # free the slot
        self.front = (self.front + 1) % self.capacity # wrap-around
        self.size -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        return self.data[self.front]

    def __str__(self) -> str:
        items = [self.data[(self.front + i) % self.capacity] for i in range(self.size)]
        return f"front -> {items} <- rear"

    def show_array(self) -> str:
        return f"array={self.data}  front={self.front}  rear={self.rear}  size={self.size}"


def linear_queue_demo():
    """Shows the weakness of a LINEAR queue: space is wasted after dequeues."""
    cap = 5
    arr, front, rear = [None] * cap, 0, -1
    for x in (10, 20, 30, 40, 50):          # fill it
        rear += 1
        arr[rear] = x
    for _ in range(3):                      # remove 3 elements
        arr[front] = None
        front += 1
    print("LINEAR queue after 5 enqueues and 3 dequeues:", arr)
    print(f"  front={front}, rear={rear} -> rear == cap-1, so it reports FULL")
    print("  even though 3 of the 5 slots are empty (wasted memory).")


if __name__ == "__main__":
    print("=== Linear queue weakness ===")
    linear_queue_demo()

    print("\n=== Circular queue ===")
    q = CircularQueue(5)
    for x in (10, 20, 30, 40, 50):
        q.enqueue(x)
    print("After 5 enqueues :", q.show_array())
    print("Dequeued         :", q.dequeue(), q.dequeue(), q.dequeue())
    print("After 3 dequeues :", q.show_array())
    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)                      # these reuse the freed slots (wrap-around)
    print("After 3 enqueues :", q.show_array())
    print("Logical order    :", q)
    print("Full?", q.is_full(), "| Empty?", q.is_empty())
    try:
        q.enqueue(99)
    except OverflowError as e:
        print("Expected error   :", e)
