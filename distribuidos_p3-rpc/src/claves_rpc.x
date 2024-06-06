typedef double vector_value2<>;
struct get_exit_args {
    char value1[256];
    int N_value2;
    double value2[32];
    int result;

};


program CLAVES {
    version CLAVESVER {
        int rpc_init() = 0;
        int rpc_set_value(int key, string value1, int N_value2, vector_value2 value2) = 1;
        get_exit_args rpc_get_value(int key) = 2;
        int rpc_modify_value(int key, string value1, int N_value2, vector_value2 value2) = 3;
        int rpc_delete_key(int key) = 4; 
        int rpc_exist(int key) = 5; 
    } = 1;
} = 99; 
