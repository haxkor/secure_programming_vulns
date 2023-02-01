#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

static char name[10] = {0};

void win() {
	execl("/bin/flag","/bin/flag", NULL);
}

void name_in() {
    fflush(stdout);
    fgets(name, 11, stdin);
}

void name_out() {
    char cool_name[10];
    strcpy(cool_name,name);
    printf(cool_name);
    fflush(stdout);
}

void do_yeet() {
    char buffer[8];
    printf("YEET!");
    gets(buffer); // The canary is saving us anyways, right?
}

int main() {
    printf("Give me your name: ");
    name_in();
    printf("What a cool name! :-) ");
    name_out();
    do_yeet();
}
