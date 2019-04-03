/*
    Héctor Mauricio González Coello
    A01328258
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
// Signals library
#include <errno.h>
#include <signal.h>
// Sockets libraries
#include <netdb.h>
#include <sys/poll.h>
// Posix threads library
#include <pthread.h>

#define MAX_ACCOUNTS 5
#define BUFFER_SIZE 4096
#define MAX_QUEUE 5

///// FUNCTION DECLARATIONS
void readData();


///// MAIN FUNCTION
int main(int argc, char * argv[])
{
    readData();
}

void readData()
{
    FILE *fp;
    char str[BUFFER_SIZE];
    char* filename = "sx-stackoverflow.txt";

    FILE * file_ptrOut = NULL;
    char buffer[BUFFER_SIZE];

    int nodeA, nodeB;
    long long int relationship;

    char * filename2 = "out.csv";
    file_ptrOut = fopen(filename2, "w");
 
    fp = fopen(filename, "r");
    if (fp == NULL){
        printf("Could not open file %s",filename);
        return;
    }

    fprintf(file_ptrOut, "nodeA,nodeB,relationship\n");
    while (fgets(str, BUFFER_SIZE, fp) != NULL)
    {
        sscanf(buffer, "%d %d %lld\n", &nodeA, &nodeB, &relationship); 
        printf("%d,%d,%lld",nodeA, nodeB, relationship);
        fprintf(file_ptrOut, "%d,%d,%lld\n", nodeA, nodeB, relationship); 
    }
    
    fclose(fp);
    fclose(file_ptrOut);
}