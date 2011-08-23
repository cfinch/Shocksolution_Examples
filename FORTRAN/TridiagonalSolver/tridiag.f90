MODULE TRI
CONTAINS
SUBROUTINE TRIDIAG(A,B,C,R,N,U,CODE)
  !*****************************************************************
  ! Solves for a vector U of length N the tridiagonal linear set
  ! M U = R, where A, B and C are the three main diagonals of matrix
  ! M(N,N), the other terms are 0. R is the right side vector.
  !*****************************************************************
  implicit none
!  integer, parameter :: NMAX=100

  real, dimension(N), intent(in) :: A,B,C,R
  !f2py depend(N) A,B,C,R

  real, dimension(N), intent(out) :: U
  integer, intent(in) :: N
  integer, intent(out) :: CODE

  REAL BET,GAM(N)
  integer J

  IF(B(1).EQ.0.D0) THEN
    CODE=1
    RETURN
  END IF

  BET=B(1)
  U(1)=R(1)/BET
  DO J=2,N                    !Decomposition and forward substitution
    GAM(J)=C(J-1)/BET
    BET=B(J)-A(J)*GAM(J)
    IF(BET.EQ.0.D0) THEN            !Algorithm fails
      CODE=2
      RETURN
    END IF
    U(J)=(R(J)-A(J)*U(J-1))/BET
  END DO

  DO J=N-1,1,-1                     !Back substitution
    U(J)=U(J)-GAM(J+1)*U(J+1)
  END DO
  
  CODE=0
  RETURN
end subroutine tridiag

END MODULE TRI
