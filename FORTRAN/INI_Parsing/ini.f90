! PARSER - parse an ini file
!     V1.0 6 AUG 03
!     Written by Douglas S. Elder elderdo@yahoo.com

!** common block that will contain the iniFile
BLOCK DATA iniFile
  LOGICAL initialized
  INTEGER num_lines
  CHARACTER LINES(100)*256
  CHARACTER iniFilename*256
  COMMON /Options/ num_lines, LINES, initialized, iniFilename
  DATA initialized, num_lines, iniFilename / .FALSE., 0, 'Options.ini' /
END

!** allow you to use a different iniFile or to switch to another
SUBROUTINE setIniFilename(value)
  CHARACTER value*(*)
  LOGICAL initialized
  INTEGER num_lines
  CHARACTER LINES(100)*256
  CHARACTER iniFilename*256
  COMMON /Options/ num_lines, LINES, initialized, iniFilename
  if (initialized .EQV. .TRUE.) then
    if (value .NE. iniFilename) then
        ! switching to a different ini file
        iniFilename = value
        call loadOptions
    end if
  else
    ! overriding the default ini file
    iniFilename = value
  end if
END

!**** read in the iniFile into the common Options block
SUBROUTINE loadOptions
    IMPLICIT NONE
    INTEGER num_lines
    LOGICAL initialized
    CHARACTER LINES(100)*256
    CHARACTER iniFilename*256
    COMMON /Options/ num_lines, LINES, initialized, iniFilename
    CHARACTER LINE*256 
    !  WRITE(*,*) 'loadOptions'
    num_lines = 0
    OPEN(UNIT=33, FILE=iniFilename)
1    READ(33,'(A)', END=10) LINE
    num_lines = num_lines + 1
    if (num_lines .GT. 100) then
        WRITE(0,*) 'Options.ini file > 100 lines.'
        STOP 16
    else
        LINES(num_lines) = LINE 
    end if
    GOTO 1

10    CONTINUE
    !  WRITE(*,*) 'num_lines = ',num_lines
    CLOSE (UNIT=33)
    initialized = .TRUE.
END

!*** try to find the Section and keyword, if found return its value
!*** otherwise return an empty string and an error
SUBROUTINE getValue(section, kwd, value, error)
  IMPLICIT NONE
  logical, intent(out) :: error
  CHARACTER section*(*)
  CHARACTER kwd*(*)
  CHARACTER value*(*)
  INTEGER I, STARTVAL
  INTEGER num_lines
  LOGICAL initialized
  CHARACTER LINES(100)*256
  CHARACTER iniFilename*256
  COMMON /Options/ num_lines, LINES, initialized, iniFilename
  INTEGER MAXLINE
  PARAMETER (MAXLINE = 256)
  CHARACTER LINE*256
  LOGICAL foundSection, foundKwd

  error = .false.

  if (initialized .EQV. .FALSE.) then
        call loadOptions
  end if
  foundSection = .FALSE.
  foundKwd = .FALSE.
  value = ''
!WRITE(*,*) 'Looking for ',section
    DO I=1, num_lines
        if (LINES(I)(1:1) .EQ. '[') then
            startval = index(lines(i), '[' // trim(section) // ']', .true.)
            if (startval > 0) then
                foundSection = .true.
            endif
        else
            if (foundSection .EQV. .TRUE.) then
                startval = index(lines(i), kwd, .true.)
                if (startval > 0) then
                    startval = index(lines(i), '=')
                    value = LINES(I)(STARTVAL+1:)
                end if
            end if
        end if
    ENDDO
    if (value .eq. '') then
        error = .true.
    endif
END

