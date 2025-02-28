// Implements a dictionary's functionality
#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <strings.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
} node;

unsigned int NO_of_Nodes = 0;

// TODO: Choose number of buckets in hash table
const unsigned int N = LENGTH;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    unsigned int pos = hash(word);
    node* cursor = table[pos];
    while(cursor != NULL)
    {
        if(strcasecmp(cursor->word, word) == 0)
            return true;
        cursor = cursor->next;
    }
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    return (strlen(word) % N);
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
    // Open the dictionary file
    FILE *source = fopen(dictionary, "r");
    if(source == NULL)
        return false;

    // Read each word in the file
    char str[LENGTH] = "";
    while (fscanf(source, "%s", str) != EOF)
    {
        // Add each word to the hash table
        node *n = malloc(sizeof(node));
        if ( n == NULL) return false;
        strcpy(n->word, str);
        n->next = NULL;

        int position = hash(str);
        NO_of_Nodes ++;
        n->next = table[position];
        table[position] = n;
    }

    // Close the dictionary file
    fclose(source);
    return true;
}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    return NO_of_Nodes;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    for(int i=0; i < N; i++)
    {
        node* cursor = table[i];
        while(cursor != NULL)
        {
            node* temp = cursor;
            cursor = cursor->next;
            free(temp);
            NO_of_Nodes--;
        }
    }
    if (NO_of_Nodes == 0)
    return true;
    return false;
}
