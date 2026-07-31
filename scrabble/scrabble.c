#include <cs50.h>
#include <stdio.h>
#include <string.h>

const int SIZE_OF_LETTERS = 53, SIZE_OF_POINTS = 52; // no magic numbers
const char LETTERS[SIZE_OF_LETTERS] = {
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
    'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', // decoder tables
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'};
const int POINTS[SIZE_OF_POINTS] = {1, 3, 3, 2, 1, 4, 2,  4,  1, 8, 5, 1, 3, 1, 1, 3, 10, 1,
                                    1, 1, 1, 4, 4, 8, 4,  10, 1, 3, 3, 2, 1, 4, 2, 4, 1,  8,
                                    5, 1, 3, 1, 1, 3, 10, 1,  1, 1, 1, 4, 4, 8, 4, 10};

int calculate_points(string word);

int main(void)
{
    string word_one;
    string word_two;

    // error handling
    do
    {
        word_one = get_string("Player 1 - What's your word? ");
        word_two = get_string("Player 2 - What's your word? ");
    }
    while (word_one[0] == '\0' && word_two[0] == '\0');

    int points_player1 = calculate_points(word_one);
    int points_player2 = calculate_points(word_two);

    // printf("Player 1 - u got %d points!\n", points_player1);
    // printf("Player 2 - u got %d points!\n", points_player2);

    if (points_player1 > points_player2)
    {
        printf("Player 1 wins!\n");
    }
    else if (points_player1 == points_player2)
    {
        printf("It's a tie!\n");
    }
    else
    {
        printf("Player 2 wins!\n");
    }
}

// calculates points
int calculate_points(string word)
{
    const int SIZE_OF_POINTS1 = 100;
    char temp;        // temporary storage
    int len, sum = 0; // counter

    len = strlen(word);
    for (int i = 0; i < len; i++) // iterates over letters of "input"
    {
        temp = word[i];
        for (int j = 0; j < SIZE_OF_LETTERS; j++) // iterates over decoder letter table
        {
            if (temp == LETTERS[j]) // if letters are same
            {
                sum += POINTS[j];
                break;
            }
        }
    }
    return sum;
}
