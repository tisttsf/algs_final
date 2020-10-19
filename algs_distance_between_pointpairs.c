#include <stdio.h>
#include <limits.h>
#include <string.h>
#include <stdlib.h>
typedef struct graph_type * graph;
{
	struct edge
	{
		int u;
		int v;
		int w;		
	}
};
struct  vertex
{
	char str_vertex[256];
};
void vertex_ini(struct vertex *v)
{
	strcpy(v->str_vertext,"");
};
struct graph_type
{
	int **adj;
	struct vertext *vertex_array;
	int v_num;
	int e_num;
};