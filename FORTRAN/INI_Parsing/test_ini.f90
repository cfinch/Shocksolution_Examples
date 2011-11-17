! PARSER - parse an ini file
!     V1.0 6 AUG 03
PROGRAM MAIN
    IMPLICIT NONE
    CHARACTER exe*256
    CHARACTER temp*256
    INTEGER lastChar
    external setIniFilename, getValue
    logical error

    call setIniFilename('test.ini')
    call getValue('constants', 'pi', temp, error)
    if (error .eqv. .false.) then
        write(*,*) 'temp = ', temp
    endif
    call getValue('setup', 'simulate', temp, error)
    if (error .eqv. .false.) then
        write(*,*) 'simulate = ', temp
    endif
    call getValue('doesnotexist', 'dummy', temp, error)
    if (error .eqv. .false.) then
        write(*,*) 'dummy = ', temp
    endif
end program

