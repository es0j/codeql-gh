#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vulns.h"

void do_cmd_exec(char *cmd) {

    system(cmd);
}