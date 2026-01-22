#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vulns.h"

void stackover(char *input) {
    char buf[32];
    strcpy(buf,input);
}