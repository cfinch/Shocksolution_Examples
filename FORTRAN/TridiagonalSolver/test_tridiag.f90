program fortran_linear_solver
use tri
implicit none

integer , parameter :: N = 5
real, dimension(N) :: A,B,C,R,U
integer :: CODE

A = (/10.0, 10.0, 10.0, 10.0, 0.0/)
B = (/-40.0, -30.0, -30.0, -30.0, 40.0/)
C = (/10.0, 10.0, 10.0, 10.0, 0.0/)
R = (/-10.0, -10.0, -10.0, -10.0, -30.0/)

CALL TRIDIAG(A,B,C,R,N,U,CODE)

print *, U
print *, CODE

end program fortran_linear_solver
