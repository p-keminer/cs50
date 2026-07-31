#include <cs50.h>
#include <stdio.h>

int calculate_count(int change);
int give_me_my_change(void);

int main(void)
{
    printf("%i\n", calculate_count(give_me_my_change()));
}

int give_me_my_change(void)
{
    int change;
    // user input
    do
    {
        change = get_int("Give me my Change! My Change is: ");
    }
    while (change < 0); // rejecting negatives
    return change;
}

int calculate_count(int change)
{
    // contants for readability
    const int quarter = 25;
    const int dime = 10;
    const int nickel = 5;
    const int cent = 1;

    int quarters = 0, dimes = 0, nickels = 0, cents = 0; // counters

    // calculate quarters
    while (change >= quarter)
    {
        quarters++;
        change -= quarter;
    }
    // calculate dimes
    while (change >= dime)
    {
        dimes++;
        change -= dime;
    }
    // calculate nickels
    while (change >= nickel)
    {
        nickels++;
        change -= nickel;
    }
    // calculate cents
    while (change >= cent)
    {
        cents++;
        change -= cent;
    }

    int sum = quarters + dimes + nickels + cents;
    return sum;
}
