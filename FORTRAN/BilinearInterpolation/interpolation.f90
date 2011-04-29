module interpolation

    contains

    function binarysearch(length, array, value, delta)
        ! Given an array and a value, returns the index of the element that
        ! is closest to, but less than, the given value.
        ! Uses a binary search algorithm.
        ! "delta" is the tolerance used to determine if two values are equal
        ! if ( abs(x1 - x2) <= delta) then
        !    assume x1 = x2
        ! endif

        implicit none
        integer, intent(in) :: length
        real, dimension(length), intent(in) :: array
        !f2py depend(length) array
        real, intent(in) :: value
        real, intent(in), optional :: delta

        integer :: binarysearch

        integer :: left, middle, right
        real :: d

        if (present(delta) .eqv. .true.) then
            d = delta
        else
            d = 1e-9
        endif
        
        left = 1
        right = length
        do
            if (left > right) then
                exit
            endif
            middle = nint((left+right) / 2.0)
            if ( abs(array(middle) - value) <= d) then
                binarySearch = middle
                return
            else if (array(middle) > value) then
                right = middle - 1
            else
                left = middle + 1
            end if
        end do
        binarysearch = right

    end function binarysearch

    real function interpolate(x_len, x_array, y_len, y_array, f, x, y, delta)
        ! This function uses bilinear interpolation to estimate the value
        ! of a function f at point (x,y)
        ! f is assumed to be sampled on a regular grid, with the grid x values specified
        ! by x_array and the grid y values specified by y_array
        ! Reference: http://en.wikipedia.org/wiki/Bilinear_interpolation
        implicit none
        integer, intent(in) :: x_len, y_len           
        real, dimension(x_len), intent(in) :: x_array
        real, dimension(y_len), intent(in) :: y_array
        real, dimension(x_len, y_len), intent(in) :: f
        real, intent(in) :: x,y
        real, intent(in), optional :: delta
        !f2py depend(x_len) x_array, f
        !f2py depend(y_len) y_array, f

        real :: denom, x1, x2, y1, y2
        integer :: i,j

        i = binarysearch(x_len, x_array, x)
        j = binarysearch(y_len, y_array, y)

        x1 = x_array(i)
        x2 = x_array(i+1)

        y1 = y_array(j)
        y2 = y_array(j+1)
        
        denom = (x2 - x1)*(y2 - y1)

        interpolate = (f(i,j)*(x2-x)*(y2-y) + f(i+1,j)*(x-x1)*(y2-y) + &
            f(i,j+1)*(x2-x)*(y-y1) + f(i+1, j+1)*(x-x1)*(y-y1))/denom

    end function interpolate

end module interpolation
