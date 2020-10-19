#include<stdio.h>
#include<string.h>
#include<stdlib.h>
int Result[150];
int main(){
	int Substract(int *a, int *b, int len1, int len2);
	int Division(int *a, int *b, int len1, int len2);
	bool Initial(char *s, int *a, int len);
	void Print(int *a,int len);
	char num1[150], num2[150];
	int a1[150], a2[150];
	int len1, len2;
	memset(a1, 0, sizeof(a1));
	memset(a2, 0, sizeof(a2));
	memset(Result, 0, sizeof(Result));
	scanf("%s",num1);
	scanf("%s",num2);
	len1 = strlen(num1);
	len2 = strlen(num2);
	if(!Initial(num1, a1, len1))
		exit(0);
	if(!Initial(num2, a2, len2))
		exit(0);
	Division(a1, a2, len1, len2);
	Print(Result,len1-len2);
}

bool Initial(char *s, int *a, int len){
	int i, j=0;
	for(i=len-1; i>=0; i--)
		a[j++] = s[i] - '0';
	return true;
}

int Substract(int *a, int *b, int len1, int len2){
	int i;
	if(len1 < len2)
		return -1;
	else if(len1 = len2){
		for(i = len1-1; i>=0; i--){
			if(a[i] > b[i])
				break;
			else if(a[i] < b[i])
				return -1;
		}
	}
	else{
		for(i=0; i<len1; i++){
			a[i] -= b[i];
			
			if(a[i] < 0){
				a[i] += 10;
				a[i+1] -=1;
			}
		}
		for(i=len1-1; i>=0; i--){
			if(!a[i])
				return i+1;
		}
		return 0;
	}
}
	
int Division(int *a, int *b, int len1, int len2){
	int nTimes;
	if(len1 < len2){
		printf("0\n");
		exit(0);
	}
	else if (len1 == len2){
		if(Substract(a, b, len1, len2) < 0){
			printf("0\n");
            exit(0);
        }
        else if(Substract(a, b, len1, len2) == 0){
        	printf("1\n");
        	exit(0);
		}
	}
	else{
		len1 = Substract(a, b, len1, len2);
		Result[0]++;
		nTimes = len1-len2;
		if(nTimes < 0){
			printf("1\n");
			exit(0);
		}
		else if(nTimes > 0){
			for(int i=len1-1; i>=0; i--){
				if(i >= nTimes)
					b[i] = b[i-nTimes];
				else
					b[i] = 0;
			}
		}
		len2 = len1;
		for(int j = 0; j<nTimes; j++){
			int temp;
			while((temp = Substract(a, b+j, len1, len2+j)) >= 0){
				len1 = temp;
				Result[nTimes-j]++;
			}
		}
	}
}

void Print(int *a, int len){
	for(int i=0; i<len; i++){
		if(Result[i]>=10){
			Result[i+1] += Result[i]/10;
			Result[i] %= 10;
		}
	}
	for(int j=len; j>=0; j++){
		if(Result[j] == 0)  continue;
		else  printf("%d",Result[j]);
		printf("\n");
	}
}


 