# Autores (NIA): 100472092, 100472119
# Practica1-Ejercicio2

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


# ejercicio2
study_energy: 
	addi sp sp -4
    sw ra 0(sp)
	addi sp sp -16 # espacio para una cadena y tres enteros
    li t0 97 # t0 <- a
    sb zero 1(sp) # (sp) == 0 (caracter fin de cadena)
    sw a0 4(sp)
    li t6 123
    sw t6 12(sp)
	while_study_energy:
    	lw t6 12(sp)
    	bge t0 t6 end_study_energy # while t0 < 123 
        sb t0 0(sp) # cabeza de pila <- a 
		mv a1 sp # a1 <- &'a'
        
    	rdcycle t1
        sw t1 8(sp) # ciclos antes de string_compare, conservamos antes de la llamada a string_compare
        jal ra, string_compare
        
        rdcycle t1
        lw t2 8(sp) # recuperamos el nÃÂÃÂºmero de ciclos previo
        sub t1 t1 t2 # ciclos totales
        lbu t0 0(sp) #recuperamos caracter current
        
        # print
        li a7 11
        mv a0 t0
        ecall
	    li a0 ':'
		ecall
        li a0 ' '
        ecall
        li a7 1
        mv a0 t1
        ecall
        li a7 11
        li a0 10
        ecall
        
        # siguiente caracter
        addi t0 t0 1
        lw a0 4(sp)
        j while_study_energy

end_study_energy: 
lw ra 16(sp)
addi sp sp 20 # reajustar el valor de la pila 
jr ra
