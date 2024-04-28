
#include <stdbool.h>
#include <stdio.h> // For printf in main
#include <stdlib.h>
#include <assert.h> // For assert in test

struct llist_head { 
    struct llist_node *first; 
}; 
struct llist_node { 
    struct llist_node *next; 
}; 

struct node { 
    struct llist_node node;
    int value;
};

#define llist_for_each(pos, node) \
    for (typeof(*(node)) *(pos) = (node); (pos); (pos) = (pos)->next)
#define llist_for_each_safe(pos, node) \
    for (typeof(*(node)) *(pos) = (node), *n; (pos) && (n = (pos)->next), 1; (pos) = n)

static inline void llist_add(struct llist_node *new, struct llist_head *head) {
    new->next = head->first;
    head->first = new;
}

static inline bool node_add(struct llist_head *list, int value) {
    struct node *node;
    node = malloc(sizeof(*node));
    if (!node)
        return false;
    node->value = value;
    llist_add((struct llist_node *)node, list);
    return true;
}

int test(void) { 
    struct llist_head *list;
    int r = 0;

    list = calloc(1, sizeof(*list));
    if (!list)
        return 1;
    
    if (!node_add(list, 1))
        return 1;
    if (!node_add(list, 2))
        return 1;
    
    // verify order and value
    int expected_value = 2; // The last value added should be first in the list
    llist_for_each(pos, list->first) {
        struct node *node = (struct node *)pos; // Casting to access 'value'
        assert(node->value == expected_value); // Verify the value is correct
        expected_value--; // Decrement to check the next expected value
    }

    // ensure we've checked both nodes
    assert(expected_value == 0);
    
    // free allocated nodes to prevent memory leaks
    struct node *current_node;

    struct llist_node *current_llist_node = list->first;
    while (current_llist_node != NULL) {
        current_node = (struct node *)current_llist_node; // Correct casting from llist_node to node
        current_llist_node = current_llist_node->next; // Move to next before freeing the current node
        free(current_node); // current_node is the actual struct we allocated
    }

    free(list);
    return r;
}

int main(void) {
    if (test() != 0) {
        printf("Test failed\n");
        return 1;
    }
    printf("Test passed\n");
    return 0;
}
