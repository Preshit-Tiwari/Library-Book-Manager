#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>

char rotate(char c, int n);

int main(int argc, string argv[])
{
    // Make sure program was run with just one command-line argument

    if(argc != 2)
    {
        printf("Usage: ./caesar key\n");
        return 1;
    }

    for (int i=0, len= strlen(argv[1]); i < len; i++)
    {
        if(!(isdigit(argv[1][i])))
        {
            printf("Usage: ./caesar key\n");
            return 1;
        }
    }

    int key = 0;

    for (int i=0, len= strlen(argv[1]); i < len; i++)
    {
        char a = argv[1][i] - '0';
        key *= 10;
        key += a;
    }

    key %= 26;

    string text = get_string("plaintext: ");

    for (int i = 0, len = strlen(text); i < len; i++)
    {
        text[i] = rotate(text[i], key);
    }

    printf("ciphertext: %s\n", text);

    return 0;
}

char rotate(char c, int n)
{
    if ( c >= 'A' && c <= 'Z')
    {
        return 'A' + ((int)(c - 'A' + n))%26;
    }
    else if (c >= 'a' && c <= 'z')
    {
        return 'a' + ((int)(c - 'a' + n))%26;
    }
    else
    {
        return c;
    }
}
