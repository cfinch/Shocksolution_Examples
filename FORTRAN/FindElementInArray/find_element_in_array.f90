program find_element_in_array
    implicit none

    integer :: i, num_elements = 10000000, target_value = 9000000
    integer, dimension(:), allocatable :: array1, array2
    real :: t1, t2
    integer :: loc

    allocate(array1(num_elements), array2(num_elements))

    ! Create array
    do i = 1, num_elements
        array1(i) = i
    end do

    ! Search array, method 1
    call cpu_time(t1)
    do i = 1, num_elements
        if (array1(i) .eq. target_value) then
            loc = i
            exit
        endif
    end do
    call cpu_time(t2)
    write(*,*) "Value ", target_value, " found at ", loc
    write(*,*) "CPU time: ", t2-t1

    ! Search array, method 2
    call cpu_time(t1)
    forall (i=1:num_elements) array2(i) = abs(array1(i) - target_value)
    loc = minloc(array2, 1)
    call cpu_time(t2)
    write(*,*) "Value ", target_value, " found at ", loc
    write(*,*) "CPU time: ", t2-t1

    ! Search array, method 3
    call cpu_time(t1)    
    loc = minloc(abs(array1 - target_value), 1)
    call cpu_time(t2)
    write(*,*) "Value ", target_value, " found at ", loc
    write(*,*) "CPU time: ", t2-t1

end program find_element_in_array
