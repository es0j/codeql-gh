#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vulns.h"

void double_free() {

    char *buf = malloc(32);
    strcpy(buf, "texto temporario");
    free(buf);          // libera memória
    free(buf);          // libera memória
    //puts(buf);
}