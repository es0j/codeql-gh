#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vulns.h"

void do_format_bug(char *fmt) {

    printf(fmt);
}