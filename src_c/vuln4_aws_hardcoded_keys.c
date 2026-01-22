#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "vulns.h"

char* get_aws_keys() {
    char *aws_key_id="AKIAFAKEEXAMPLE123456";
    char *aws_secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY";
    return aws_secret_key;
}