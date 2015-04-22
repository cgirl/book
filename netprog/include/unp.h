#ifndef __unp_h_
#define __unp_h_

#include "config.h"
#include <errno.h>
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>
#include <signal.h>
#include <sys/wait.h>
#include <arpa/inet.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>

#ifndef INET_ADDRESTRLEN
#define INET_ADDRESTRLEN 16 /* ddd.ddd.ddd.ddd\0
							   1234567890123456*/

/* ϵͳͷ�ļ�<sys/socket.h>���ж���SOMAXCONN������Ĭ�ϵ�5����ʱ����ϣ���и���������� */
#define LISTENQ 1024 /* listen()�����ĵڶ������� */

/* miscellaneous constant */
#define MAXLINE 4096         /* max text line lenght */
#define	MAXSOCKADDR  128

/* following shortens all the types casts of pointer argument */
#define SA struct sockaddr
#define	SERV_PORT		 9877

typedef void Sigfunc(int);
#endif
#endif //__unp_h_
