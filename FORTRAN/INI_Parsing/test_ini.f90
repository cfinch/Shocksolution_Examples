! PARSER - parse an ini file
!     V1.0 6 AUG 03
PROGRAM MAIN
    IMPLICIT NONE
    CHARACTER str*256
    external setIniFilename, getValue
    logical error, simulate
    real pi

    call setIniFilename('test.ini')

    call getValue('constants', 'pi', str, error)
    if (error .eqv. .false.) then
        write(*,'(a,a)') 'str = ', trim(str)
        read(str, '(f7.5)') pi
        write(*,'(a,f7.5)') 'pi = ', pi
    endif

    call getValue('setup', 'simulate', str, error)
    if (error .eqv. .false.) then
        write(*,'(a,a)') 'str = ', trim(str)
        read(str, '(L7)') simulate
        write(*,'(a,L1)') 'simulate = ', simulate

    endif

    ! Test error handling.  This SHOULD print the error message.
    call getValue('doesnotexist', 'dummy', str, error)
    if (error .eqv. .false.) then
        write(*,'(a,a)') 'dummy = ', trim(str)
    else
        write(*,'(a)') 'Error: section or keyword not found'
    endif

end program

