#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include "vulns.h"



int main(int argc,char **argv) {
    int a = atoi(argv[1]);
    switch (a)
    {
    case 1:
        char *a = create_and_free();
        puts(a);
        break;

    case 2:
        oob(atoi(argv[2]),atoi(argv[3]));
        break;
    
    case 3:
        stackover(argv[2]);
        break;

    case 4:
        puts(get_aws_keys());
        break;

    case 5:
        do_cmd_exec(argv[2]);
        break;

    case 6:
        do_format_bug(argv[2]);
        break;

    case 7:
        double_free();
        break;
        
    case 8:
        integer_underflow();
        break;

    default:
        break;
    }
    return 0;
}
