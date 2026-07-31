#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int n = 0; n < width; n++)
        {
            float sum = image[i][n].rgbtBlue + image[i][n].rgbtGreen + image[i][n].rgbtRed;
            float aver = round(sum / 3);
            image[i][n].rgbtBlue = aver;
            image[i][n].rgbtGreen = aver;
            image[i][n].rgbtRed = aver;
        }
    }
    return;
}

// capping values over 255
int capp(int sep_rgb)
{
    if (sep_rgb > 255)
    {
        sep_rgb = 255;
    }
    return sep_rgb;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int n = 0; n < width; n++)
        {
            int orig_blue = image[i][n].rgbtBlue;
            int orig_green = image[i][n].rgbtGreen; // values for formula
            int orig_red = image[i][n].rgbtRed;

            int sep_red = round(.393 * orig_red + .769 * orig_green + .189 * orig_blue);
            image[i][n].rgbtRed = capp(sep_red);
            int sep_green =round(.349 * orig_red + .686 * orig_green + .168 * orig_blue); // formula of cs50
            image[i][n].rgbtGreen = capp(sep_green);
            int sep_blue = round(.272 * orig_red + .534 * orig_green + .131 * orig_blue);
            image[i][n].rgbtBlue = capp(sep_blue);
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE tmp;
    for (int i = 0; i < height; i++)
    {
        for (int n = 0; n < width / 2; n++)
        {
            tmp = image[i][n];
            image[i][n] = image[i][width - n - 1]; // easy swapping algorh
            image[i][width - n - 1] = tmp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE working_copy[height][width]; // get working copy
    for (int i = 0; i < height; i++)       // iterating over all pixels
    {
        for (int n = 0; n < width; n++)
        {
            working_copy[i][n] = image[i][n]; // write pixels in working copy
        }
    }
    for (int i = 0; i < height; i++) // iterating over all pixels
    {
        for (int n = 0; n < width; n++)
        {
            // summing for neighbors
            int counter = 0;
            float sum_red = 0;
            float sum_green = 0;
            float sum_blue = 0;             // initializing caused by reset for every pixel
            for (int ii = -1; ii < 2; ii++) // iterating over possible neighbours in row
            {
                for (int nn = -1; nn < 2; nn++) // iterating over possible neighbours in collumn
                {
                    int n_row = i + ii, n_col = n + nn; // helpers e.g i(50) + ii(-1) = 49 or 50 + 1
                    if (n_row >= 0 && n_row < height && n_col >= 0 &&
                        n_col < width) // only possible neighbours
                    { // e.g. n_col smaller 0 [ 0+(-1) ] # <- | px0 px1 .. pswd-1 pxwd | -> # n_col bigger width


                        counter++;
                        sum_red += working_copy[n_row][n_col].rgbtRed;
                        sum_green +=working_copy[n_row][n_col].rgbtGreen; // sum all neighbor colors
                        sum_blue += working_copy[n_row][n_col].rgbtBlue;
                    }
                }
            }
            image[i][n].rgbtGreen = round(sum_green / counter);
            image[i][n].rgbtBlue = round(sum_blue / counter); // write averages of neighbours in pixels
            image[i][n].rgbtRed = round(sum_red / counter);
        }
    }
    return;
}
