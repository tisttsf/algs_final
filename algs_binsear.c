#include <stdio.h>
#include <ctype.h>
#include <string.h>
#define M 100
struct poine{
	int x;
	int y;
}d1;
struct x{
	int d;
	int e;
}d2;
int main()
{
	d1.x=10;
	d1.y=20;
	putchar('c');
	struct poine *x=&d1;
	struct x *xx=&d2;
}