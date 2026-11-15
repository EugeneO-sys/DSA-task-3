/* Question 7 - Double ended queue (deque) in C using a circular array */
#include <stdio.h>
#define MAX 5

typedef struct {
    int data[MAX];
    int front;   /* index of front element */
    int rear;    /* index of rear element  */
    int size;
} Deque;

void init(Deque *d)          { d->front = 0; d->rear = MAX - 1; d->size = 0; }
int  isEmpty(const Deque *d) { return d->size == 0; }
int  isFull(const Deque *d)  { return d->size == MAX; }

/* 1. Front insertion */
int insertFront(Deque *d, int x) {
    if (isFull(d)) { printf("Overflow: deque full\n"); return 0; }
    d->front = (d->front - 1 + MAX) % MAX;
    d->data[d->front] = x;
    d->size++;
    return 1;
}

/* 2. Rear insertion */
int insertRear(Deque *d, int x) {
    if (isFull(d)) { printf("Overflow: deque full\n"); return 0; }
    d->rear = (d->rear + 1) % MAX;
    d->data[d->rear] = x;
    d->size++;
    return 1;
}

/* 3. Front deletion */
int deleteFront(Deque *d, int *out) {
    if (isEmpty(d)) { printf("Underflow: deque empty\n"); return 0; }
    *out = d->data[d->front];
    d->front = (d->front + 1) % MAX;
    d->size--;
    return 1;
}

/* 4. Rear deletion */
int deleteRear(Deque *d, int *out) {
    if (isEmpty(d)) { printf("Underflow: deque empty\n"); return 0; }
    *out = d->data[d->rear];
    d->rear = (d->rear - 1 + MAX) % MAX;
    d->size--;
    return 1;
}

void display(const Deque *d) {
    printf("Deque (front -> rear): ");
    for (int i = 0, idx = d->front; i < d->size; i++, idx = (idx + 1) % MAX)
        printf("%d ", d->data[idx]);
    printf("%s\n", d->size ? "" : "(empty)");
}

int main(void) {
    Deque d; init(&d); int v;
    insertRear(&d, 10);  insertRear(&d, 20);  display(&d);
    insertFront(&d, 5);  insertFront(&d, 1);  display(&d);
    insertRear(&d, 30);  display(&d);
    insertRear(&d, 40);                       /* overflow */
    if (deleteFront(&d, &v)) printf("Deleted front: %d\n", v);
    if (deleteRear(&d, &v))  printf("Deleted rear : %d\n", v);
    display(&d);
    while (deleteFront(&d, &v)) ;             /* drain, then underflow */
    display(&d);
    return 0;
}
