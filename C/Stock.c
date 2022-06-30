#include <stdio.h>
#include <ws2tcpip.h>

#pragma comment (lib, "Ws2_32.lib")

int get_html(char *companyname){
    WSADATA wsaData;
    SOCKET hostSock = INVALID_SOCKET;
    struct addrinfo *hostAddrInfo = NULL, *attemptAddrInfo = NULL, hintsAddrInfo;
//    char *sendbuf = "GET /search?q=Microsoft+Stocks HTTP/1.1\n\n";
    char sendbuf[100];
    sprintf(sendbuf, "%s%s%s", "GET /search?q=",companyname,"+Stocks HTTP/1.1\n\n");
    char recvbuf[ 512 ];
    int recvbuflen = 512;
    int result;
    
    result = WSAStartup( MAKEWORD( 2,2 ), &wsaData );
    if ( result != 0 ) {
        printf( "WSAStartup failed with error: %d\n", result );
        return -1;
    }

    ZeroMemory( &hintsAddrInfo, sizeof(hintsAddrInfo) );
    hintsAddrInfo.ai_family = AF_UNSPEC;
    hintsAddrInfo.ai_socktype = SOCK_STREAM;
    hintsAddrInfo.ai_protocol = IPPROTO_TCP;

    result = getaddrinfo( "google.com", "80", &hintsAddrInfo, &hostAddrInfo );
    if ( result != 0 ) {
        printf( "getaddrinfo failed with error: %d\n", result );
        WSACleanup( );
        return -2;
    }

    for( attemptAddrInfo = hostAddrInfo; attemptAddrInfo != NULL ; attemptAddrInfo = attemptAddrInfo->ai_next ) {

        hostSock = socket( attemptAddrInfo->ai_family, attemptAddrInfo->ai_socktype, 
            attemptAddrInfo->ai_protocol );
        if( hostSock == INVALID_SOCKET ) {
            printf( "socket failed with error: %ld\n", WSAGetLastError( ) );
            WSACleanup( );
            return -3;
        }

        result = connect( hostSock, attemptAddrInfo->ai_addr, (int)attemptAddrInfo->ai_addrlen);
		printf( "hostAddrInfo: %d\n", result );
        if( result == SOCKET_ERROR ) {
            closesocket( hostSock );
            hostSock = INVALID_SOCKET;
            continue;
        }
        break;
    }

    freeaddrinfo( hostAddrInfo );

    if( hostSock == INVALID_SOCKET ) {
        printf( "Unable to connect to server!\n" );
        WSACleanup( );
        return -4;
    }

    result = send( hostSock, sendbuf, (int)strlen(sendbuf), 0 );
    if( result == SOCKET_ERROR ) {
        printf( "send failed with error: %d\n", WSAGetLastError( ) );
        closesocket( hostSock );
        WSACleanup( );
        return -5;
    }

    printf("Bytes Sent: %ld\n", result);

    result = shutdown( hostSock, SD_SEND );
    if( result == SOCKET_ERROR ) {
        printf( "shutdown failed with error: %d\n", WSAGetLastError( ) );
        closesocket( hostSock );
        WSACleanup( );
        return -6;
    }

	int preview = 0, total = 0;
    FILE *fp;
    fp = fopen( "file.txt", "w");
    do {

        result = recv( hostSock, recvbuf, recvbuflen, 0 );
        if ( result > 0 ) {
			total += result;
			if( preview < 166900 ) { fwrite( recvbuf, 1, result, fp ); preview += result; }
        } else if( result == 0 )
            printf( "Connection closed\n" );
        else
            printf( "recv failed with error: %d\n", WSAGetLastError( ) );

    } while( result > 0 );
    fclose(fp);
    printf( "\n\nBytes received: %d\n", total );

    closesocket( hostSock );
    WSACleanup( );
    printf("file.txt successfully updated\n");
    return 0;
}

char find_data() {
    FILE* fp;
    fp = fopen("file.txt", "r");
    char iter;
    char* diter = "BNeawe iBp4i AP7Wnd";
    int count = 0;
    int count2 = 55;
    int flag = 0;
    int kill = 0;
    char num[55];
    while (1) {
        iter = fgetc(fp);
        if (iter == *diter) {
            //printf("\n\n%c found\n\n", *diter);
            count++;
            diter++;
        }
        else {
            diter = diter - count;
            count = 0;
        }
        
        if (*diter == 'd') {
            printf("%c", iter);
            flag = 1;
        }
        if (flag) {
            printf("%c", iter);
            if (count2 == 0){
                kill = 1;
            }
            else {
                count2 = count2 - 1;
                num[55] = num[55] + iter;
            }
        }
        if (kill) {
            break;
        }
    }

    

    return num[55];
}

int main(){
    get_html("Tesla");
    char data = find_data();
    for (int i; i < 20; i++) {
        printf("%c", data[i]);
    }
}