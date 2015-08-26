#include "unp.h"
#include "declare.h"
#include <time.h>

int main( int argc, char** argv )
{
    int listenfd, connfd;
    struct sockaddr_in sockaddr;
    time_t ticks;
    char buff[MAXLINE];

    bzero( &sockaddr, sizeof(sockaddr) );

    listenfd = socket( AF_INET, SOCK_STREAM, 0 );
    if ( listenfd < 0 )
    {
        err_sys( "socket error server" );
    }
    
    /* #define INADDR_ANY ((in_addr_t) 0x00000000)
     * INADDR_ANY-0.0.0.0,��ʾ�����ַ����ȷ���ĵ�ַ��htonl���޷��ų�����ת��Ϊ�����ֽ�˳�� */
    //sockaddr.sin_addr.s_addr = htonl( INADDR_ANY );
    sockaddr.sin_addr.s_addr = inet_addr( "192.168.16.121" );
    sockaddr.sin_family = AF_INET;
    /* htons���޷��Ŷ�����ת��Ϊ�����ֽ�˳�� */
    sockaddr.sin_port = htons(1122);
    
    /* �� */
    if ( bind( listenfd, (SA *)&sockaddr, sizeof(sockaddr) ) < 0 )
    {
        err_sys( "bind error" );
    }

    /* ���� */
    if ( listen( listenfd, LISTENQ ) < 0 )
    {
        err_sys( "listen error" );
    }

    /* ��� */
    while( 1 )
    {
        connfd = accept( listenfd, (SA *)NULL, NULL );
        if ( connfd < 0 )
        {
            err_sys( "accept error" );
        }
        ticks = time( NULL );
        snprintf( buff, sizeof(buff), "%.24s\r\n", ctime(&ticks) );
        if ( write( connfd, buff, strlen(buff) ) < 0 )
        {
            err_quit( "write error" );
        }
        close( connfd );
    }
    return 0;
}
