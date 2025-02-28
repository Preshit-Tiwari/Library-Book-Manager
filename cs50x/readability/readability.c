#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>

int count_letters(string text);
int count_words(string text);
int count_sentences(string text);

int main(void)
{
    // Prompt the user for some text
    string text = get_string("Text: ");

    // Count the number of letters, words, and sentences in the text
    int letters = count_letters(text);
    int words = count_words(text);
    int sentences = count_sentences(text);

    // Comput the Coleman-Liau index
    float L = (float)letters / (float)words * 100;
    float S = (float)sentences / (float)words * 100;

    float index = 0.0588 * L - 0.296 * S - 15.8 ;

    int index2 = (int) round(index);

    // Print the grade level
    if( index2 >= 16)
        printf("Grade 16+\n");
    else if( index2 < 1)
        printf("Before Grade 1\n");
    else
        printf("Grade %d\n",index2);
}

int count_letters(string text)
{
    int l_count = 0;
    // Return the number of letters in text

    for (int i = 0 , len = strlen(text); i < len; i++)
    {
        if((text[i] >= 'A' && text[i] <= 'Z')||(text[i] >= 'a' && text[i] <= 'z'))
        {
            l_count++;
        }
    }
    return l_count;
}

int count_words(string text)
{
    int w_count = 1;
    // Return the number of words in text

    for (int i = 0 , len = strlen(text); i < len; i++)
    {
        if( isspace(text[i]) )
        {
            w_count++;
        }
    }
    return w_count;
}

int count_sentences(string text)
{
    int s_count = 0;
    // Return the number of sentences in text

    for (int i = 0 , len = strlen(text); i < len; i++)
    {
        if(text[i] == '.' || text[i] ==  '!' || text[i] == '?')
        {
            s_count++;
        }
    }
    return s_count;
}
