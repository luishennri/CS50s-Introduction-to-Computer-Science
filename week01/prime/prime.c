#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int min = get_int("min: ");
    int max = get_int("max: ");

    int count = 0;

    for(int i = min; i <= max; i++)
        {
            for(int j = 2; j < i; j++)
            {
                if(i % j == 0)
                {
                    count++;
                    break;
                }
            }
            if(count == 0 && i != 1)
                printf("%d\n", i);
            count = 0;
        }
}