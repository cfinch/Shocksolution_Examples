lu_solver.so : lu_solver.f90
	f2py2.6 -c -m lu_solver lu_solver.f90

test_lu_solver : test_lu_solver.o lu_solver.o
	gfortran -o test_lu_solver test_lu_solver.o lu_solver.o

test_lu_solver.o : test_lu_solver.f90
	gfortran -c test_lu_solver.f90

lu_solver.o : lu_solver.f90
	gfortran -c lu_solver.f90

clean :
	rm test_lu_solver.o lu_solver.o lu_solver.so
