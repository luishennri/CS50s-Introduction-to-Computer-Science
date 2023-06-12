// Write a function to replace vowels with numbers
// Get practice with strings
// Get practice with command line
// Get practice with switch

#include <cs50.h>
#include <stdio.h>
#include <string.h>

string replace(string input);
int main(int argc, string argv[])

{
    if(argc == 2)
    {
        printf("%s \n", replace(argv[1]));
    }
    else
    {
        printf("Usage: %s Word\n", argv[0]);
    }
}
string replace(string input)
{
    int length = strlen(input);

    for (int i = 0, n = length; i < n; i++)
    {
        switch(input[i])
        {
            case 'a':
            input[i] = '6';
            break;

            case 'e':
            input[i] = '3';
            break;

            case 'i':
            input[i] = '1';
            break;

            case 'o':
            input[i] = '0';
            break;
        }
    }
    return input;
}