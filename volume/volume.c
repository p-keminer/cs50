// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    // storage for the 44Bytes Header metadata to give that to functions below
    uint8_t header[HEADER_SIZE];

    /* read datas, after fopen(commandlineelement1, "readpermission")
    to string/array of chars "header", one by one in opened adress *input  */
    int check_1 = fread(header, HEADER_SIZE, 1, input);
    if (check_1 < 1)
    {
        return 1; // check for memory
    }
    /* read datas, after fopen(commandlineelement2, "writepermission")
    from string/array of chars "header", one by one in opened adress *output  */
    int check_2 = fwrite(header, HEADER_SIZE, 1, output);
    if (check_2 < 1)
    {
        return 1; // check for memory
    }

    // build storage for single 2 bytes of volumedata
    int16_t buffer;

    /* read datas from the adress of the storage, every time 2 bytes
    (same as the buffer), single one per time, from file opened by
    fopen(commandlinelement1, "readpermission")  until its over and fread
    has a return value of 0 */
    while (fread(&buffer, sizeof(int16_t), 1, input) != 0)
    {
        buffer *= factor; // modify buffer
        /* write datas from the adress of the storage, every time 2 bytes
        (same as the buffer), single one per time, from file opened by
        fopen(commandlinelement2, "writeermission")  until its over and fread
        has a return value of 0 */
        int check_3 = fwrite(&buffer, sizeof(int16_t), 1, output);
        if (check_3 < 1)
        {
            return 1; // check for memory
        }
    }

    // Close files
    fclose(input);
    fclose(output);
}
