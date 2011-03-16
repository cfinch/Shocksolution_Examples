!*******************************************************
!* Solving a linear system AX = B by LU decomposition  *
!* with dynamic allocations                            *
!*                                                     *
!*                   F90 version by J-P Moreau, Paris  *
!* --------------------------------------------------- *
!* SAMPLE RUN:                                         *
!*                                                     *
!* Input file (test_lu.dat):                           *
!*                                                     *
!*  4                                                  *
!*  8  2    3  12     25.0                             *
!*  2  4    7   0.25  13.25                            *
!*  3  7    3   5     18.0                             *
!* 12  0.25 5   2     19.25                            *
!*                                                     *
!* Output file (test_lu.lst):                          *
!*                                                     *
!* --------------------------------------------------- *
!*  LINEAR SYSTEM TO BE SOLVED:                        *
!* --------------------------------------------------- *
!*  N=4                                                *
!*                                                     *
!*  8.000000  2.000000  3.000000  12.00000  25.00000   *
!*  2.000000  4.000000  7.000000  0.250000  13.25000   *
!*  3.000000  7.000000  3.000000  5.000000  18.00000   *
!*  12.00000  0.250000  5.000000  2.000000  19.25000   *
!*                                                     *
!*  System solution:                                   *
!*                                                     *
!*  X1=  1.000000                                      *
!*  X2=  1.000000                                      *
!*  X3=  1.000000                                      *
!*  X4=  1.000000                                      *
!* --------------------------------------------------- *
!*                                                     *
!* Uses: module LU                                     *
!*******************************************************
Program test_lu_solver
  USE LU
  implicit none

  real*8, pointer ::  A(:,:)   !real matrix (n x n)
  real*8, pointer ::  B(:)     !real vector (n)
  real*8, pointer ::  temp(:)  !real temporary vector (n+1)
  integer,pointer ::  INDX(:)  !integer vector (n)

  integer :: i, d, rc, n = 4
  
  !dynamic allocations
  allocate(A(n,n))
  allocate(B(n))
  allocate(temp(n+1))
  allocate(INDX(n))

  ! Fill matrix A
  ! 8  2    3  12     25.0
  ! 2  4    7   0.25  13.25
  ! 3  7    3   5     18.0
  ! 12  0.25 5   2     19.25

  A(1,1) = 8;   A(1,2) = 2;     A(1,3) = 3;     A(1,4) = 12
  A(2,1) = 2;   A(2,2) = 4;     A(2,3) = 7;     A(2,4) = 0.25
  A(3,1) = 3;   A(3,2) = 7;     A(3,3) = 3;     A(3,4) = 5
  A(4,1) = 12;   A(4,2) = 0.25;     A(4,3) = 5;     A(4,4) = 2

  ! Vector B
  B(1) = 25
  B(2) = 13.25
  B(3) = 18.0
  B(4) = 19.25

!call LU decomposition routine
  call LUDCMP(A,n,INDX,D,rc)

!call appropriate solver if previous return code is ok
  if (rc.eq.0) then
    call LUBKSB(A,n,INDX,B)
  endif

!print results or error message
  if (rc.eq.1) then
    write(*,*) ' The system matrix is singular, no solution !'
  else
    write(*,*) '  System solution:'
    do i=1, n 
      write(*,*) i,B(i) 
    end do
  end if

end program test_lu_solver
