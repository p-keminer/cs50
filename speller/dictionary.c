// Implements a dictionary's functionality
#include "dictionary.h"
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// global variables
unsigned int count = 0;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    node *tmpc = table[hash(word)]; // gettin cursor with calculated index from word
    while (tmpc != NULL)
    {
        if (strcasecmp(tmpc->word, word) == 0) // right word ?
        {
            return 1;
        }
        else
        {
            tmpc = tmpc->next; // cursor goin deeper
        }
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    FILE *src;                    // pointer
    char tmp[LENGTH + 1];         // string for fscanf + NUL
    src = fopen(dictionary, "r"); // open argument given with readmpermissions
    if (src == NULL)
    {
        printf("Couldnt open file!\n");
        return 0; // secure check
    }
    while (fscanf(src, "%s", tmp) != EOF) // while scanning is returnvalue = EOF
    {
        node *new_n = malloc(sizeof(node)); // new node with size of struct "node"
        if (new_n == NULL)
        {
            printf("No Heap available1!"); // secure check
            return 0;
        }
        strcpy(new_n->word, tmp);       // building bridge between tmp and word
        unsigned int index = hash(tmp); // gettin index
        new_n->next = table[index];     // setin new beginning
        table[index] = new_n;
        count++;
    }
    fclose(src);
    return 1;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return count;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for (int i = 0; i < N; i++) // iterating over hash table
    {
        node *curs = table[i]; // gettin main cursor over table
        while (curs != NULL)
        {
            node *tmp = curs;  // gettin safe cursor
            curs = curs->next; // main cursor gettin deeper
            free(tmp);         // freeing safe cursor
        }
    }
    return true;
}
