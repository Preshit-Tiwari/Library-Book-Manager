#include <stdio.h>
#include <cs50.h>

void print_row(int spaces, int bricks);

int main(void)
{
    // prompt user for the pyramid height
    int n;
    do
    {
        n= get_int("Height: ");
    }
    while(n < 1);

    // print a pyramid of that height
    for(int i=0; i<n; i++)
    {
        print_row(n-1-i, i+1);
    }

}

void print_row(int spaces, int bricks)
{
    for(int j=0; j<spaces; j++)
    {
        printf(" ");
    }
    for(int j=0; j<bricks; j++)
    {
        printf("#");
    }
    printf("\n");
}
