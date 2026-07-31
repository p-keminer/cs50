
#include <cs50.h>
#include <ctype.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters_whole_text(string text);
double calculate_cli(double letters, double sentences, int words);
int count_sentences_whole_text(string text);
int count_words_whole_text(string text);

int main(void)
{
    string text;
    do
    {
        text = get_string("Prompt ur Text: ");
    }
    while (strlen(text) == 0);

    double cli = calculate_cli(count_letters_whole_text(text), count_sentences_whole_text(text),
                               count_words_whole_text(text));

    if (round(cli) < 1)
    {
        printf("Before Grade 1\n");
    }
    else if (round(cli) >= 16)
    {
        printf("Grade 16+\n");
    }
    else
    {
        printf("Grade %.0f\n", round(cli));
    }
}

// cli function
double calculate_cli(double letters, double sentences, int words)
{
    double cli = 0.0588 * (letters / words) * 100 - 0.296 * (sentences / words) * 100 - 15.8;
    return cli;
}

// calculator functions
//----------------------
int count_letters_whole_text(string text)
{
    int letter_counter = 0, len;
    len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        if (isalpha(text[i]))
            letter_counter++;
    }
    return letter_counter;
}

int count_sentences_whole_text(string text)
{
    int sentences_counter = 0, len;
    len = strlen(text);
    for (int i = 0; i < len; i++)
    {
        if (text[i] == '?' || text[i] == '!' || text[i] == '.')
            sentences_counter++;
    }
    return sentences_counter;
}

// counter functions
//------------------
int count_words_whole_text(string text)
{
    int word_counter = 1, len;
    len = strlen(text);
    for (int i = 0; i <= len; i++)
    {
        if (text[i] == ' ')
            word_counter++;
    }
    return word_counter;
}

/* printf("%lf\n%lf\n%i\n",count_letters_whole_text(text),
                        count_sentences_whole_text(text),
                        count_words_whole_text(text));*/
