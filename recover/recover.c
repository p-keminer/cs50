#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

const int BUFFER_SIZE = 512;

int main(int argc, char *argv[])
{
    // check commandlinearguments
    if (argc != 2)
    {
        printf("open with ./recover [NAME_OF_MEMORY_CARD]\n");
        return 1;
    }

    // opening memory card
    FILE *memory_card = fopen(argv[1], "r");
    if (memory_card == 0)
    {
        printf("Cant open file!\n"); // secure check
        return 1;
    }

    // buffer for rw
    uint8_t buffer[BUFFER_SIZE]; // no & for adresses cs its *buffer itself
    char filename[8];            // string for filenames
    FILE *img = NULL;            // pointer
    int count_images = 0;        // counter for naming

    // while reading
    while (fread(buffer, 1, BUFFER_SIZE, memory_card) >= BUFFER_SIZE)
    {

        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0) // bitwise masking
        {                               // buffer [3] = 1110 **** & 1111 0000 = 1110 0000 = 0xe0
            if (img != NULL)            // actually writing ?
            {
                fclose(img);
            }
            sprintf(filename, "%03i.jpg",
                    count_images);      // print filenames in string %03i -> **i.jpg
            img = fopen(filename, "w"); // open data with writingpermission
            if (img == NULL)
            {
                printf("Couldnt open file.\n"); // secure check
                return 1;
            }
            int check2 = fwrite(buffer, 1, BUFFER_SIZE, img); // write data from buffer into img
            if (check2 < 1)
            {
                printf("couldnt start writing\n"); // secure check
                return 1;
            }
            count_images++; // counter for naming
        }
        else
        {
            if (img != NULL) // actually writing while found magic numbers ?
            {
                int check3 = fwrite(buffer, 1, BUFFER_SIZE, img); // go on writing
                if (check3 < 1)
                {
                    printf("couldnt continue writing\n"); // secure check
                    return 1;
                }
            }
        }
    }
    fclose(img);            // tidy up
    fclose(memory_card);
}
