#include <stdio.h>
#include <cs50.h>

int getpopulation_size(void);
int getend_population_size(int population_size);
int calculate_years(int population_size, int end_population_size);

int main(void)
{
    int population_size = getpopulation_size();
    int end_population_size = getend_population_size(population_size);
    int years = calculate_years(population_size, end_population_size);
    printf("Years: %i\n",years);
}

int getpopulation_size(void)
{
    int n;
    do
    {
        n = get_int("What`s the population size: ");
    }
    while (n < 9);
    return n;
}
int getend_population_size(int population_size)
{
    int n;
    do
    {
        n = get_int("What`s the end population size: ");
    }
    while (n < population_size);
    return n;
}
int calculate_years(int population_size, int end_population_size)
{
    int years = 0;
    int x;
    int y;
    while (population_size < end_population_size)
    {
        x = population_size / 3;
        y = population_size / 4;
        population_size += x - y;
        years++;
    }
    return years;
}