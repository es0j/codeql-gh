#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vulns.h"



char *cut_prefix_vuln(const char *s, size_t len, size_t prefix) {
    /* underflow: se prefix > len, remaining wrapa para um valor grande */
    size_t remaining = len - prefix;
    char *out = malloc(remaining + 1);   /* possivelmente aloca muito pouco/errado */
    if (!out) return NULL;
    memcpy(out, s + prefix, remaining);  /* leitura fora do buffer se prefix>len */
    out[remaining] = '\0';
    return out;
}

int integer_underflow() {
    const char *s = "abc";          /* len = 3 */
    /* chamada com prefix maior que len -> causa underflow e uso errado */
    char *t = cut_prefix_vuln(s, strlen(s), 10);

    printf("resultado: %s\n", t);
    free(t);
    
    return 0;
}