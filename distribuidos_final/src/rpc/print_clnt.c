/*
 * Please do not edit this file.
 * It was generated using rpcgen.
 */

#include <memory.h> /* for memset */
#include "print.h"

/* Default timeout can be changed using clnt_control() */
static struct timeval TIMEOUT = { 25, 0 };

enum clnt_stat 
rpc_print_1(char *impresion, int *clnt_res,  CLIENT *clnt)
{
	return (clnt_call(clnt, rpc_print,
		(xdrproc_t) xdr_wrapstring, (caddr_t) &impresion,
		(xdrproc_t) xdr_int, (caddr_t) clnt_res,
		TIMEOUT));
}
