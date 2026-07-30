#include<stdio.h>
#include<time.h>
int main()
{
	int a[100],n,key;
	int i,low,high,mid;
	clock_t start,end;
	double lineartime,binarytime;
	printf ("Enter the number of elements: ");
	scanf ("%d",&n);
	printf("Enter %d sorted element:\n",n);
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	printf("Enter the element to search: ");
	scanf("%d",&key);
	//Linear Search
	start = clock();
	for(i=0;i<n;i++)
	{
		if(a[i] == key)
		break;
	}
	end = clock();
    lineartime = (double)(end-start)/CLOCKS_PER_SEC;
	//Binary search
	start = clock();
	low = 0;
	high = n-1;
	while(low<=high)
    {
		mid = (low+high)/2;
		if(a[mid] == key)
		break;
		else if (a[mid]<key)
		low = mid+1;
		else
		high = mid-1;
    }
	end = clock();
	binarytime = (double)(end-start)/CLOCKS_PER_SEC;
	printf("\n Execution time: \n");
	printf("Linear search =%f seconds\n",lineartime);
	printf ("Binary search =%f seconds\n",binarytime);
	return 0;
}

