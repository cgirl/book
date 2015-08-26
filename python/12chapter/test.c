#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int SplitStr( char** ppSource, char* psDelim, int iDelimLen, char* psBuf )
{
    char *psSrcTmp;
    char *sTmp = NULL;

    sTmp = malloc( iDelimLen+1 );
    if ( sTmp == NULL )
    {
        printf( "ÄÚ´æ·ÖÅä³ö´í" );
        return -1;
    }
    psSrcTmp = *ppSource;

    for (; *psSrcTmp != '\0'; psSrcTmp++ )
    {
        memset( sTmp, 0x00, sizeof(sTmp) );
        strncpy( sTmp, psSrcTmp, iDelimLen );
        sTmp[iDelimLen+1] = '\0';
        if ( strcmp( sTmp, psDelim ) == 0 )
        {
            break;
        }
    }

    memcpy( psBuf, *ppSource, psSrcTmp - *ppSource );
    psBuf[psSrcTmp - *ppSource] = '\0';

    if ( *psSrcTmp != '\0' )
    {
        *ppSource = psSrcTmp + iDelimLen;
    }
    else
    {
        *ppSource = NULL;
    }

    return 0;
}
int main()
{
    int i = 0;
    char *AnsFileList[]={"123~|~456~|~789"};
    char sBuf[3] = {0};
    while ( AnsFileList[i] != '\0' )
    {
        SplitStr(AnsFileList, "~|~", 3, sBuf );
        printf( "[%s]\n", sBuf );
    }

    return 0;
}
