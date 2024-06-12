# Autores (NIA): 100472092, 100472119
# Practica1-Ejercicio1

string_compare: 
	mv t0 a0 # direction of A
	mv t1 a1 # direction of B

	li a0 1 # equal 
    # CASO ERROR
    beq t0  zero error 
    beq t1 zero error
   	# main block 
    while_string_compare: 
    	lbu t2 0(t0) # t2 <- A[t0]
        lbu t3 0(t1) # t3 <- B[t1]
        bne t2 t3 not_equal # A[t0] != B[t1]
        beq t2 zero end_string_compare # A[t0] == '\0'? 
        addi t0 t0 1 # siguiente caracter
        addi t1 t1 1 # "
        j while_string_compare

error: 
	li a0 -1
	j end_string_compare
    
not_equal: li a0 0



end_string_compare: jr ra
