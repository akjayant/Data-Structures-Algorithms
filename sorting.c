//---------Let's cuddle with integer arrays make our way to sorting them (in O(nlogn)), searching them (in O(logn)), finding median (in O(n))//--------------------------
#include<stdlib.h>
#include<stdio.h>

/* Let's use Dynamic Array (because who wants static arrays!!!)*/
struct dyn_arr
{
	int capacity;
	int *arr;
		
};

void display(int a[],int n)
{
int i=0;
for	(i=0;i<n;i++)
printf("%d ",a[i]);
}

void swap(int *x,int *y)
{	
int t;
t=*x;
*x=*y;
*y=t;
}

/*Some functions will not have return type int* because arrays are passed as reference, no need to return them.) */


/* SHUFFLE ARRAY        */     
void shuffle(int a[],int n)
{
	
int i,j;
for (i=n-1;i>=0;i--)
{
j=rand()%(i+1);	
swap(&a[i],&a[j]);	
}	
	
}

/* BUBBLE SORT : 
Best case {all elements are already in increasing order in this case} (modified bubble sort with swap_flag)  - O(n)
Worst case = O(n^2)
Stable Algorithm - two elements with same key will have same order after sorting
Space complexity - No aux space required
*/
void bubblesort(int a[],int n)
{
	int i,j;
	int swap_flag=1;
	for (i=n-1;i>0&&swap_flag;i--)
	{
		swap_flag=0;
		for (j=0;j<i;j++)
		{
			if (a[j]>a[j+1])
			{swap(&a[j],&a[j+1]);
			swap_flag=1;
			}
		}
		
	}
	
}

/* SELECTION SORT : 
Best case - O(n^2)
Worst case = O(n^2)
Not a Stable Algorithm 
Least no of swaps - O(n)
Space complexity - No aux space required
*/


void selectionsort(int a[],int n)
{
int i,j,min;	
	for (i=0;i<n;i++)
	{
		min=i;
		for (j=i+1;j<n;j++)
		{
			if (a[j]<a[min])
			min=j;	
		}
		swap(&a[i],&a[min]);
		
	}
}

/* INSERTION SORT
Best case - O(n)
Worst case - O(n^2)
Stable Algorithm
Space complexity - No aux space reqd */

void insertionsort(int a[],int n)
{
int i,j,key;
	
for (i=1;i<n;i++)
{
key=a[i];	
	for (j=i;j>0&&a[j-1]>key;j--)
	a[j]=a[j-1];	
a[j]=key;	
}
}

/*QUICK SORT
Recursive Algorithm 
Best Case : (Every time partition happens in equal halves i.e, T(n) = 2T(n/2) + O(n))  = O(nlogn)  
Worst Case : (Unbalanced partition having 1 element in first half and n-1 in other i.e, T(n) = T(n-1) + O(n)) = O(n^2) e.g already sorted array, all equal elements etc.
Average Case: O(nlogn)
Not stable by default
Worst case Space Complexity : O(n) (stack space for recursive calls) + no aux space req_d

*/

int partition(int a[],int low,int high)
{
int left,right,pivot_item;	
left=low;
right=high;
pivot_item=a[low];	       // Replace this by pivot_item = median_of_array(a,low,high) and splits will be in equal halves: Time complexity = O(n) same as that of this method

while (left<right)
{
	while(a[left]<=pivot_item)
	left++;
	
	while(a[right]>pivot_item)
	right--;
	
	if (left<right)
	swap(&a[left],&a[right]);
}

a[low]=a[right];
a[right]=pivot_item;
return right;	
	
}	


void quicksort(int a[],int low,int high)
{
	int pivot;
	if (high>low)
	{
	pivot=partition(a,low,high);
	quicksort(a,low,pivot-1);
	quicksort(a,pivot+1,high);	
	}	
	
}
	

/* MERGE SORT
Recurrence Relation : T(n) = 2T(n/2) + O(n)
Best case, Average case, Worst case = O(nlogn)
Space complexity = O(n) aux space required + O(logn) stack space for recursive calls
Stable sorting algorithm
*/

void merge(int a[],int low,int mid,int high)
{
	int i,n1,n2,n;
	n1=mid-low+1;
	n2=high-mid;
	n=n1+n2;
	int *aux_left = (int *)malloc((n1)*sizeof(int));
	int *aux_right = (int *)malloc((n2)*sizeof(int));
	
	
	for (i=0;i<n1;i++)
	aux_left[i]=a[low+i];

	
	for (i=0;i<n2;i++)
	aux_right[i]=a[mid+i+1];

	
	int ptr_left=0,ptr_right=0;
	i=low;
	while(ptr_left<n1&&ptr_right<n2)
		{
		
			if (aux_left[ptr_left]<=aux_right[ptr_right])
				{
				a[i]=aux_left[ptr_left];
				ptr_left++;
				i++;
			}
			else
			{
			
				a[i]=aux_right[ptr_right];
				ptr_right++;
				i++;
			}
		}		
		while (ptr_right<n2)
			{
			a[i]=aux_right[ptr_right];
			ptr_right++;
			i++;
			}
		while (ptr_left<n1)
			{
			a[i]=aux_left[ptr_left];
			ptr_left++;
			i++;
			}
			
   }

void mergesort(int a[],int low,int high)
{
	int mid;
	
	if (high>low){
		mid = (high+low)/2;
		mergesort(a,low,mid);
		mergesort(a,mid+1,high);
		merge(a,low,mid,high);
	}
	
}	
	
	
	




int main()
{
struct dyn_arr *d = malloc(sizeof(struct dyn_arr));
printf("Enter size of array\n");
scanf("%d",&d->capacity);
d->arr=(int *)malloc(d->capacity*sizeof(int));
printf("Enter array elements\n");
int i=0;
for(i=0;i<d->capacity;i++)
scanf("%d",&d->arr[i]);



/* Interesting point to be noted - 
I am passing size of array as well because sizeof(array)/sizeof(int) may produce 
wrong result because malloc is very kind hearted function it allocates a bit more than you want (or whatever value you passed as arg)!!*/
												  
display(d->arr,d->capacity);   
                   
shuffle(d->arr,d->capacity);
printf("\nshuffled array\n");					  
display(d->arr,d->capacity);

//Sorting drivers

shuffle(d->arr,d->capacity);
bubblesort(d->arr,d->capacity);
printf("\nbubble sort result\n");
display(d->arr,d->capacity);

shuffle(d->arr,d->capacity);
selectionsort(d->arr,d->capacity);
printf("\nselection sort result\n");
display(d->arr,d->capacity);

shuffle(d->arr,d->capacity);
insertionsort(d->arr,d->capacity);
printf("\ninsertion sort result\n");
display(d->arr,d->capacity);


shuffle(d->arr,d->capacity);
quicksort(d->arr,0,d->capacity-1);
printf("\nquick sort result\n");
display(d->arr,d->capacity);



shuffle(d->arr,d->capacity);
mergesort(d->arr,0,d->capacity-1);
printf("\nmerge sort result\n");
display(d->arr,d->capacity);

												  
return 0;
}
