#include <cs50.h>
#include <stdio.h>

// declaration functions
int get_int_between_1_and_8(void);
void draw_pyramid(int n);

int main(void)
{
    draw_pyramid(get_int_between_1_and_8());
}

//------------
// Functions
//------------

int get_int_between_1_and_8(void)
{
    int input; // userinput storage
    do
    {
        input = get_int("Give me a number between 1 and 8: ");
    }
    while (input < 1 || input > 8); // only between 1 and 8
    printf("\n");

    return input; // not necessesary but useful
}

void draw_pyramid(int height)
{
    for (int i = 0; i < height; i++) // loop over every row
    {
        // here happens what every line should pe printed
        for (int line = 0; line < height - 1 - i; line++) // print ' ' exact 1 time less the height
        {
            printf(" ");
        }
        for (int line = 0; line < i + 1; line++) // print # exact one time more than line number
        {
            printf("#");
        }
        printf("  ");
        for (int line = 0; line < i + 1; line++) // print ' ' exact 1 time less the height
        {
            printf("#");
        }
        printf("\n");
    }
}
