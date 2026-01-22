#ifndef VULNS_H
#define VULNS_H

char *create_and_free();
void oob(int a,int b);
void stackover(char *input);
char* get_aws_keys();
void do_cmd_exec(char *cmd);
void do_format_bug(char *fmt);
void double_free();
int integer_underflow();
#endif
