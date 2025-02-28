#include "helpers.h"
#include <math.h>

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    // Loop over all pixels
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            // Take average of red, green, and blue
            int val = round( (float)( image[i][j].rgbtRed + image[i][j].rgbtGreen + image[i][j].rgbtBlue ) / 3.0 );

            // Update pixel values
            if (val > 255)
            {
                image[i][j].rgbtRed = 255;
                image[i][j].rgbtGreen = 255;
                image[i][j].rgbtBlue = 255;
            }
            else
            {
                image[i][j].rgbtRed = val;
                image[i][j].rgbtGreen = val;
                image[i][j].rgbtBlue = val;
            }
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
    int sepiaRed = round ( .393 * image[i][j].rgbtRed + .769 * image[i][j].rgbtGreen + .189 * image[i][j].rgbtBlue );
    int sepiaGreen = round ( .349 * image[i][j].rgbtRed + .686 * image[i][j].rgbtGreen + .168 * image[i][j].rgbtBlue );
    int sepiaBlue = round ( .272 * image[i][j].rgbtRed + .534 * image[i][j].rgbtGreen + .131 * image[i][j].rgbtBlue );

    if (sepiaRed > 255) sepiaRed = 255;
    if (sepiaGreen > 255) sepiaGreen = 255;
    if (sepiaBlue > 255) sepiaBlue = 255;

    image[i][j].rgbtRed = sepiaRed;
    image[i][j].rgbtGreen = sepiaGreen;
    image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width/2; j++)
        {
            // Swap pixels
            RGBTRIPLE temp = image[i][j];
            image[i][j] = image[i][width - j -1];
            image[i][width - j -1] = temp;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // Create a copy of image
    RGBTRIPLE copy[height][width];
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            copy[i][j] = image[i][j];
        }
    }
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int red = copy[i][j].rgbtRed;
            int green = copy[i][j].rgbtGreen;
            int blue = copy[i][j].rgbtBlue;

            int number = 1;

            if (i-1 >= 0)
            {
                number++;

                red += copy[i-1][j].rgbtRed;
                blue += copy[i-1][j].rgbtBlue;
                green += copy[i-1][j].rgbtGreen;

                if (j-1 >= 0)
                {
                    number++;

                    red += copy[i-1][j-1].rgbtRed;
                    blue += copy[i-1][j-1].rgbtBlue;
                    green += copy[i-1][j-1].rgbtGreen;
                }
                if (j+1 <= width-1)
                {
                    number++;

                    red += copy[i-1][j+1].rgbtRed;
                    blue += copy[i-1][j+1].rgbtBlue;
                    green += copy[i-1][j+1].rgbtGreen;
                }
            }
            if (i+1 <= height-1)
            {
                number++;

                red += copy[i+1][j].rgbtRed;
                blue += copy[i+1][j].rgbtBlue;
                green += copy[i+1][j].rgbtGreen;

                if (j-1 >= 0)
                {
                    number++;

                    red += copy[i+1][j-1].rgbtRed;
                    blue += copy[i+1][j-1].rgbtBlue;
                    green += copy[i+1][j-1].rgbtGreen;
                }
                if (j+1 <= width-1)
                {
                    number++;

                    red += copy[i+1][j+1].rgbtRed;
                    blue += copy[i+1][j+1].rgbtBlue;
                    green += copy[i+1][j+1].rgbtGreen;
                }
            }

            if (j-1 >= 0)
            {
                number++;

                red += copy[i][j-1].rgbtRed;
                blue += copy[i][j-1].rgbtBlue;
                green += copy[i][j-1].rgbtGreen;
            }
            if (j+1 <= width-1)
            {
                number++;

                red += copy[i][j+1].rgbtRed;
                blue += copy[i][j+1].rgbtBlue;
                green += copy[i][j+1].rgbtGreen;
            }

           red = round((float)(red)/(float)number);
           blue = round((float)(blue)/(float)number);
           green = round((float)(green)/(float)number);

           if (red > 255) red = 255;
           if (green > 255) green = 255;
           if (blue > 255) blue = 255;

           image[i][j].rgbtRed = red;
           image[i][j].rgbtBlue = blue;
           image[i][j].rgbtGreen = green;
        }
    }
    return;
}
