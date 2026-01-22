#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vulns.h"

char *create_and_free() {
    char *buf = malloc(32);
    if (!buf) return NULL;
    strcpy(buf, "texto temporario");
    free(buf);          // libera memória
    return buf;         // retorna ponteiro já liberado -> USE-AFTER-FREE
}