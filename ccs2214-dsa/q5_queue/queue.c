/* Question 5 - Enqueue and Dequeue on a (linear, array based) Queue in C */
#include <stdio.h>
#define MAX 5

typedef struct {
    int data[MAX];
    int front;   /* index of first element */
    int rear;    /* index of last element  */
} Queue;

void init(Queue *q)            { q->front = 0; q->rear = -1; }
int  isEmpty(const Queue *q)   { return q->front > q->rear; }
int  isFull(const Queue *q)    { return q->rear == MAX - 1; }

void enqueue(Queue *q, int x) {
    if (isFull(q)) { printf("Queue Overflow: cannot insert %d\n", x); return; }
    q->data[++q->rear] = x;
    printf("Enqueued %d\n", x);
}

int dequeue(Queue *q) {
    if (isEmpty(q)) { printf("Queue Underflow\n"); return -1; }
    return q->data[q->front++];
}

void display(const Queue *q) {
    if (isEmpty(q)) { printf("Queue: (empty)\n"); return; }
    printf("Queue (front -> rear): ");
    for (int i = q->front; i <= q->rear; i++) printf("%d ", q->data[i]);
    printf("\n");
}

int main(void) {
    Queue q; init(&q);
    int choice, val;
    printf("1.Enqueue 2.Dequeue 3.Display 0.Exit\n");
    while (scanf("%d", &choice) == 1 && choice != 0) {
        switch (choice) {
            case 1: if (scanf("%d", &val) == 1) enqueue(&q, val); break;
            case 2: val = dequeue(&q);
                    if (val != -1) printf("Dequeued %d\n", val);
                    break;
            case 3: display(&q); break;
            default: printf("Invalid choice\n");
        }
    }
    return 0;
}
