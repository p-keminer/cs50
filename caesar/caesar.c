#include <cs50.h>
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, string argv[])
{

    if (argc != 2) // only entry if 2 comandarguments are the input
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    string arg = argv[1];                        // storage the string
    for (int i = 0, n = strlen(arg); i < n; i++) // go over the string
    {
        if (isdigit(arg[i]) == 0)
        {                                    // if anything else than a digit is in the string
            printf("Usage: ./caesar key\n"); // throw them out
            return 1;                        // closed
        }
    }

    int key = atoi(arg); // store the digits in an integer
    string plaintext;
    int check;

    plaintext = get_string("plaintext: "); // get the plaintext
    for (int i = 0, n = strlen(plaintext); i < n; i++)
    {
        if (isalpha(plaintext[i]) || plaintext[i] == ',' || plaintext[i] == '.' || plaintext[i] == '!' )
        {
            check = 1;
        }
        else
        {
            check = 0;
        }
    }

   while (check == 0) // only letters
    {
        plaintext = get_string("plaintext: ");
    }

    for (int i = 0, n = strlen(plaintext); i < n; i++) // iterate over the array
    {
        if (isupper(plaintext[i]) ) // uppercase
        {
            int p = plaintext[i] -= 65; // get it to base
            int c = (p + key) % 26;     // roll it over
            plaintext[i] = c + 65;      // back to ASCII
        }
        else if (islower(plaintext[i]) )// lowercase
        {
            int p = plaintext[i] -= 97;
            int c = (p + key) % 26;
            plaintext[i] = c + 97;
        }
    }
    printf("ciphertext: %s\n", plaintext);
}
