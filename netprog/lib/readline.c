#include "unp.h"
#include "declare.h"

/**
  ��̬(�ֲ�/ȫ��)������������(���庯����/���к���)������������������ֻ��ʼ��һ�Σ��Ժ�ֵ����ֱ�����̽���
  **/
static int read_cnt;
static char* read_ptr;
static char read_buf[MAXLINE];

/**
  ��̬������ֻ�ڱ��ļ��е��ã������ļ��޷����ã������ļ���ʹ�ͱ��ļ��ĺ���ͬ��Ҳ�������
  ʱ�䣺2015-2-13 15:46:46
  ���ܣ�ÿ�δ��ļ��������ж���һ���ַ��浽��̬ȫ�ֱ�����
  �½ڣ�5.3 5.4
  ������netprog/lib/readline.c|readline
  **/
static ssize_t my_read( int fd, char* ptr )
{
again:
	if ( read_cnt <= 0 )
	{
		if ( ( read_cnt = read(fd, read_buf, sizeof(read_buf) ) ) < 0 )
		{
			if ( errno == EINTR )
			{
				printf("EINTR\n");
				goto again;
			}
			return -1;
		}
		else if ( read_cnt == 0 )
			return 0;
		read_ptr = read_buf;
	}

	read_cnt--;
	*ptr++ = *read_ptr++;

	return 1;
}

/**
  ʱ�䣺2015-2-13 15:35:25
  ���ܣ�����ַ���ȡһ���ַ��������ֻ�ܶ�ȡmaxlen��ֵ
  �½ڣ�5.3 5.5
  ������netprog/lib/readline.c|Readline
  **/
ssize_t readline( int fd, void* vptr, size_t maxlen )
{
	ssize_t n, rc;
	char c, *ptr;

	ptr = vptr;
	for ( n = 1; n < maxlen; n++ )
	{
		if ( ( rc = my_read(fd, &c) ) == 1 )
		{
			*ptr++ = c;
			if ( c == '\n' )
				break;
		}
		else if ( rc == 0 )
		{
			*ptr = 0;
			return n - 1;
		}
		else
		{
			return -1;
		}
	}

	*ptr = 0;
	return n;
}

ssize_t Readline( int fd, void* vptr, size_t maxlen )
{
	ssize_t n;
	
	if ( ( n = readline(fd, vptr, maxlen) ) < 0 )
		err_sys( "readline error" );

	return n;
}
