def PairCorrelationFunction_2D(x,y,S,rMax,dr):
    """Compute the two-dimensional pair correlation function, also known 
    as the radial distribution function, for a set of circular particles 
    contained in a square region of a plane.  This simple function finds 
    reference particles such that a circle of radius rMax drawn around the 
    particle will fit entirely within the square, eliminating the need to 
    compensate for edge effects.  If no such particles exist, an error is
    returned. Try a smaller rMax...or write some code to handle edge effects! ;) 
    
    Arguments:
        x               an array of x positions of centers of particles
        y               an array of y positions of centers of particles
        S               length of each side of the square region of the plane
        rMax            outer diameter of largest annulus
        dr              increment for increasing radius of annulus

    Returns a tuple: (g, radii, interior_x, interior_y)
        g(r)            a numpy array containing the correlation function g(r)
        radii           a numpy array containing the radii of the
                        annuli used to compute g(r)
        interior_x      x coordinates of reference particles
        interior_y      y coordinates of reference particles
    """
    from numpy import zeros, sqrt, where, pi, average, arange, histogram
    # Number of particles in ring/area of ring/number of reference particles/number density
    # area of ring = pi*(r_outer**2 - r_inner**2)

    # Find particles which are close enough to the box center that a circle of radius
    # rMax will not cross any edge of the box
    bools1 = x>1.1*rMax
    bools2 = x<(S-1.1*rMax)
    bools3 = y>rMax*1.1
    bools4 = y<(S-rMax*1.1)
    interior_indices, = where(bools1*bools2*bools3*bools4)
    num_interior_particles = len(interior_indices)

    if num_interior_particles < 1:
        raise  RuntimeError ("No particles found for which a circle of radius rMax\
                will lie entirely within a square of side length S.  Decrease rMax\
                or increase the size of the square.")

    edges = arange(0., rMax+1.1*dr, dr)
    num_increments = len(edges)-1
    g = zeros([num_interior_particles, num_increments])
    radii = zeros(num_increments)
    numberDensity = len(x)/S**2

    # Compute pairwise correlation for each interior particle
    for p in range(num_interior_particles):
        index = interior_indices[p]
        d = sqrt((x[index]-x)**2 + (y[index]-y)**2)
        d[index] = 2*rMax

        (result,bins) = histogram(d, bins=edges, normed=False)
        g[p,:] = result/numberDensity
        
    # Average g(r) for all interior particles and compute radii
    g_average = zeros(num_increments)
    for i in range(num_increments):
        radii[i] = (edges[i] + edges[i+1])/2.        
        rOuter = edges[i+1]
        rInner = edges[i]
        g_average[i] = average(g[:,i])/(pi*(rOuter**2 - rInner**2))

    return (g_average, radii, interior_indices)
####

def PairCorrelationFunction_3D(x,y,z,S,rMax,dr):
    """Compute the three-dimensional pair correlation function for a set of
    spherical particles contained in a cube with side length S.  This simple 
    function finds reference particles such that a sphere of radius rMax drawn
    around the particle will fit entirely within the cube, eliminating the need
    to compensate for edge effects.  If no such particles exist, an error is 
    returned.  Try a smaller rMax...or write some code to handle edge effects! ;) 
    
    Arguments:
        x               an array of x positions of centers of particles
        y               an array of y positions of centers of particles
        z               an array of z positions of centers of particles
        S               length of each side of the cube in space
        rMax            outer diameter of largest spherical shell
        dr              increment for increasing radius of spherical shell

    Returns a tuple: (g, radii, interior_x, interior_y, interior_z)
        g(r)            a numpy array containing the correlation function g(r)
        radii           a numpy array containing the radii of the
                        spherical shells used to compute g(r)
        interior_x      x coordinates of reference particles
        interior_y      y coordinates of reference particles
        interior_z      z coordinates of reference particles
    """
    from numpy import zeros, sqrt, where, pi, average, arange, histogram

    # Find particles which are close enough to the cube center that a sphere of radius
    # rMax will not cross any face of the cube
    bools1 = x>rMax
    bools2 = x<(S-rMax)
    bools3 = y>rMax
    bools4 = y<(S-rMax)
    bools5 = z>rMax
    bools6 = z<(S-rMax)

    interior_indices, = where(bools1*bools2*bools3*bools4*bools5*bools6)
    num_interior_particles = len(interior_indices)

    if num_interior_particles < 1:
        raise  RuntimeError ("No particles found for which a sphere of radius rMax\
                will lie entirely within a cube of side length S.  Decrease rMax\
                or increase the size of the cube.")

    edges = arange(0., rMax+1.1*dr, dr)
    num_increments = len(edges)-1
    g = zeros([num_interior_particles, num_increments])
    radii = zeros(num_increments)
    numberDensity = len(x)/S**3

    # Compute pairwise correlation for each interior particle
    for p in range(num_interior_particles):
        index = interior_indices[p]
        d = sqrt((x[index]-x)**2 + (y[index]-y)**2 + (z[index]-z)**2)
        d[index] = 2*rMax

        (result,bins) = histogram(d, bins=edges, normed=False)
        g[p,:] = result/numberDensity
        
    # Average g(r) for all interior particles and compute radii
    g_average = zeros(num_increments)
    for i in range(num_increments):
        radii[i] = (edges[i] + edges[i+1])/2.        
        rOuter = edges[i+1]
        rInner = edges[i]
        g_average[i] = average(g[:,i])/(4./3.*pi*(rOuter**3 - rInner**3))

    return (g_average, radii, x[interior_indices], y[interior_indices], z[interior_indices])
    # Number of particles in shell/total number of particles/volume of shell/number density
    # shell volume = 4/3*pi(r_outer**3-r_inner**3)
####
