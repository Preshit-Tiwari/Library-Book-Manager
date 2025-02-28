#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int n;
    do
    {
        n = get_int("Change owed: ");
    }
    while (n < 0);

    int coins=0;
    coins+= n/25;
    n=n % 25;
    coins+= n/10;
    n=n % 10;
    coins+= n/5;
    n=n % 5;
    coins+=n;

    printf("%d\n",coins);
}
