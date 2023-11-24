#!/bin/sh

if [ "$1" != "local" ]; then
  #SBATCH --output=funcional-%j.out
  . /etc/profile
  module avail
  module load gcc/12.1.0
fi

for i in 1 2 3 4 5; do
	./build/fluid/fluid $i in/large.fld out.fld > /dev/null || exit
	 if diff -q "out/large-$i.fld" "out.fld" > /dev/null; then
	 	echo -e "$i iteraciones : \033[0;32m[SUCCESS]\033[0m"
	else
		echo -e "$i iteraciones : \033[0;31m[FAILURE]\033[0m"
	fi
done
