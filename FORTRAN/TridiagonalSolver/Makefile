tridiag.so : tridiag.f90
	f2py2.6 -c -m tridiag tridiag.f90

test_tridiag : tridiag.o test_tridiag.o
	gfortran -o test_tridiag test_tridiag.o tridiag.o

test_tridiag.o : test_tridiag.f90
	gfortran -c test_tridiag.f90

tridiag.o : tridiag.f90
	gfortran -c tridiag.f90

clean :
	rm test_tridiag.o tridiag.o tridiag.so tri.mod test_tridiag
