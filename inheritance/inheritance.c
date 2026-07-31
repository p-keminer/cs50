// Simulate genetic inheritance of blood type
#define _DEFAULT_SOURCE
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

// Each person has two parents and two alleles
typedef struct person
{
    struct person *parents[2];
    char alleles[2];
} person;

const int GENERATIONS = 3;
const int INDENT_LENGTH = 4;

person *create_family(int generations);
void print_family(person *p, int generation);
void free_family(person *p);
char random_allele();

int main(void)
{
    // Seed random number generator
    srandom(time(0));

    // Create a new family with three generations
    person *p = create_family(GENERATIONS);

    // Print family tree of blood types
    print_family(p, 0);

    // Free memory
    free_family(p);
}

// Create a new individual with `generations`
person *create_family(int generations)
{
    person *philip = malloc(sizeof(person));    // free space for new person in size of struct person

    // If there are still generations left to create
    if (generations > 1)
    {
        person *parent0 = create_family(generations - 1);
        person *parent1 = create_family(generations - 1);

        philip->parents[0] = parent0;   // go to philip's adress find parents[x] put in adress of parentX
        philip->parents[1] = parent1;

        philip->alleles[0] = parent0->alleles[rand() % 2]; // go to philip's adress find alleles[x] put in a random number of alleles of his parentX
        philip->alleles[1] = parent1->alleles[rand() % 2];
    }

    // If there are no generations left to create
    else
    {
        philip->parents[0] = NULL;  // go to philip's adress find parents[x] put them to nothing
        philip->parents[1] = NULL;

        philip->alleles[0] = random_allele();
        philip->alleles[1] = random_allele();
    }

    return philip;
}

// Free `p` and all ancestors of `p`.
void free_family(person *p)
{
    if (p == NULL)
    {
        return;         // if pointer == NULL nothing to tidy up
    }

    free_family(p->parents[0]); // go to p's adress ...
    free_family(p->parents[1]);

    free(p);    
}

// Print each family member and their alleles.
void print_family(person *p, int generation)
{
    // Handle base case
    if (p == NULL)
    {
        return;
    }

    // Print indentation
    for (int i = 0; i < generation * INDENT_LENGTH; i++)
    {
        printf(" ");
    }

    // Print person
    if (generation == 0)
    {
        printf("Child (Generation %i): blood type %c%c\n", generation, p->alleles[0],
               p->alleles[1]);
    }
    else if (generation == 1)
    {
        printf("Parent (Generation %i): blood type %c%c\n", generation, p->alleles[0],
               p->alleles[1]);
    }
    else
    {
        for (int i = 0; i < generation - 2; i++)
        {
            printf("Great-");
        }
        printf("Grandparent (Generation %i): blood type %c%c\n", generation, p->alleles[0],
               p->alleles[1]);
    }

    // Print parents of current generation
    print_family(p->parents[0], generation + 1);
    print_family(p->parents[1], generation + 1);
}

// Randomly chooses a blood type allele.
char random_allele()
{
    int r = random() % 3;
    if (r == 0)
    {
        return 'A';
    }
    else if (r == 1)
    {
        return 'B';
    }
    else
    {
        return 'O';
    }
}
