#include <stdio.h>
#include <string.h>
void bubble_sort(int a[], int n)
{
    int i, j, temp;
    for (j = 0; j < n - 1; j++)
        for (i = 0; i < n - 1 - j; i++)
        {
            if(a[i] > a[i + 1])
            {
                temp = a[i];
                a[i] = a[i + 1];
                a[i + 1] = temp;
            }
        }
}

int mysss(char* temp)
{
    int nresult = strlen(temp);
    int n, m;
    char temp1[8];
    for(n=0;n<nresult;n++)
    {
        for(m=0;m<nresult-n-1;m++)
        {
            if(temp[m]>temp[m+1]){
                temp1[0]=temp[m+1];
                temp[m+1]=temp[m];
                temp[m]=temp1[0];
            }
        }
    }

}

int main()
{
    int a[5] = {1, 2, 3, 4, 5};
    char s[5]="Hajhk";
    int i = 0;

    bubble_sort( a, 5 );
    mysss(s);

    for (i=0; i<5; i++){
        printf("%d", a[i]);
        printf("%c", s[i]);
    }
}
