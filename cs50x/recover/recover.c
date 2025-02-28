#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cs50.h>

int main(int argc, char *argv[])
{
    // Accept a single command-line argument
    if (argc != 2)
    {
        printf("Usage: ./recover FILE\n");
        return 1;
    }

    // Open the memory card
    FILE *card = fopen(argv[1], "r");
    if (card == NULL)
    {
        printf("memory card not opened!\n");
        return 1;
    }

    // Create a buffer for a block of data
    uint8_t buffer[512];

    // While there's still data left to read from the memory card
    int num = 0;
    FILE *img = NULL;
    string filename;

    while (fread(buffer, 1, 512, card) == 512)
    {
        // Create JPEGs from the data
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {

            if (num == 0)
            {
                filename = malloc(8);
                sprintf(filename, "%03i.jpg", num);
                img = fopen(filename, "w");
                num++;
                fwrite(buffer, 1, 512, img);
            }
            else
            {
                free(filename);
                fclose(img);

                filename = malloc(8);
                sprintf(filename, "%03i.jpg", num);
                img = fopen(filename, "w");
                num++;
                fwrite(buffer, 1, 512, img);
            }
        }
        else
        {
            if (num != 0)
                fwrite(buffer, 1, 512, img);
        }
    }
    free(filename);
    fclose(img);
    fclose(card);
}
