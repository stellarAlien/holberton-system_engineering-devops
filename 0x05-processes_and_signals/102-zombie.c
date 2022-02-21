#include<stdlib.h>
#include<stdio.h>

/**
 *infinite_while - infinite
 *Return: always 0
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (0);
}
/**
 * main - forks 5 times
 * Return: Always 0
 */
int main(void)
{
	unsigned int i, p;

	for (i = 0; i < 5; i++)
	{
		p = fork();
		printf("Zombie process created, PID: %u\n", p);
		infinite_while();
	}
	return (0);
}

