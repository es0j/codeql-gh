#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vulns.h"

void oob(int a,int b) {
    char *buf = malloc(32);
    buf[a] = b;
}