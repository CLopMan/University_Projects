# Autores (NIA): 100472092, 100472119
# Practica1-Ejercicio3

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



attack:
	# STACK STRUCTURE
#  0   dummy_len
#  4   &dummy
#  8   &password
#  12  ra

    addi sp sp -4 # stack <- ra
    sw ra 0(sp)
    addi sp sp -4 # &password in the stack
    sw a0 0(sp)
    mv t0 a1 # t0 <- &dummy
    addi sp sp -4 # space for &dummy
    sw t0 0(sp)
    addi sp sp -4 # dummy len
    sw zero 0(sp)
    
    
    # MAIN BLOCK (do...while)
    while_attack: 
    lw a0 8(sp) # a0 <- &password
    lw a1 4(sp) # a1 <- &dummy
    lw a2 0(sp) # a2 <- &dummy_len
    jal ra study_energy_attack # study_energy_attack(password) -> char
    lw t0 4(sp) # t0 <- &dummy
    lw t1 0(sp) # t1 <- dummy_len
    add t0 t0 t1 # t0 <- t0 + t1 == &dummy + dummy_len
    addi t1 t1 1 # actualizamos dummy_len
    sw t1 0(sp) # dummy_len <- t1
    sb a0 0(t0) # dummy[dummy_len] <- a0 (metemos en dummy el caracter descubierto en esta llamada)

    beq a0 zero end_attack # password discovered 
    j while_attack
    
    
end_attack: 
lw ra 12(sp)
lw a0 4(sp)
addi sp sp 16 # reajuste de pila 
jr ra


study_energy_attack:
	
	# STACK STRUCTURE
#0	   dummy_len
#4     &password
#8     123 (z code + 1) 4
#12    &dummy 4
#16    prev_cycles 4
#20    cycles_max 4
#24    char_out 4
#28    ra  4

	addi sp sp -32 # space needed
    sw a2 0(sp)
    sw a0 4(sp) # stack.head <- &password
    li t0 123 # t0 <- z code + 1
    sw t0 8(sp)
    sw a1 12(sp) # 8(sp) <- &dummy
    sw zero 16(sp) # prev_cycles = 0
    sw zero 20(sp) # cylces_max = 0
    sw ra 28(sp)    
    
    # check de que hemos encontrado ya la contraseÃÂ±a? 
	lw a0 4(sp)
    lw t4 12(sp)
    lw a2 0(sp)
    add t4 t4 a2
    sb zero 0(t4)
    lw a1 12(sp)
    jal ra string_compare
    li t0 1
    beq t0 a0 end0_study_energy_attack
    
    
    li t0 'a' # first char

    # Main Block 
    while_study_energy_attack:
    	lw t6 8(sp)
        bge t0 t6 end_study_energy_attack #while t0 < 123
        
        lw t1 12(sp) #dummy[dummy_len] <- t0
        add t1 t1 a2
        sb t0 0(t1)
        
        # Set up para string_compare
        lw a0 4(sp) 
        lw a1 12(sp)
        
        rdcycle t1
        sw t1 16(sp)  #ciclos antes de string_compare
        jal ra string_compare
        rdcycle t1
        lw t2 16(sp) 
        sub t1 t1 t2 # ciclos totales
        
        lw t3 12(sp) # recuperamos en t0 el caracter de esta iteracion
        lw a2 0(sp)
        add t3 t3 a2
        lbu t0 0(t3)
        
        # actulize max
        lw t2 20(sp) # t2 <- max cycles
        ble t1 t2 not_actualize
        
        # max_cycles < cycles
        sw t1 20(sp) 
        sb t0 24(sp)
        
        not_actualize: 
        	# next char (siempre se ejecuta)
        	addi t0 t0 1
            lw a0 4(sp)
        	j while_study_energy_attack   
    
end_study_energy_attack:
    # si no hemos encontrado la contraseÃ±a devolvemos el caracter que hemos descubierto en esta iteraciÃ³n
	lbu a0 24(sp)
    lw ra 28(sp)
	addi sp sp 32
    jr ra
    
end0_study_energy_attack:
	# si hemos encontrado la contraseÃ±a salimos con un 0
	li a0 0
    lw ra 28(sp)
	addi sp sp 32
    jr ra
