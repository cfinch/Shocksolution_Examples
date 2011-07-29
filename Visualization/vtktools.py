#!/usr/bin/env python
class VTK_XML_Serial_Unstructured:
    """
    USAGE:
    vtk_writer = VTK_XML_Serial_Unstructured()
    vtk_writer.snapshot("filename.vtu", x, y, z, optional arguments...)
    vtk_writer.writePVD("filename.pvd")
    """
    def __init__(self):
        self.fileNames = []

    def coords_to_string(self, x,y,z):
        string = str()
        for i in range(len(x)):
            string = string + repr(x[i]) + ' ' + repr(y[i]) \
                    + ' ' + repr(z[i]) + ' '
        return string

    def array_to_string(self, a):
        string = str()
        for i in range(len(a)):
            string = string + repr(a[i]) + ' '
        return string

    def snapshot(self, fileName, x,y,z, x_jump=[], y_jump=[], z_jump=[], x_force=[], \
            y_force=[], z_force=[], radii=[], colors=[]):
        """
        ARGUMENTS:
        fileName        file name and/or path/filename
        x               array of x coordinates of particle centers
        y               array of y coordinates of particle centers
        z               array of z coordinates of particle centers
        x_jump          optional array of x components of particle jump vectors
        y_jump          optional array of y components of particle jump vectors
        z_jump          optional array of z components of particle jump vectors
        x_force         optional array of x components of force vectors
        y_force         optional array of y components of force vectors
        z_force         optional array of z components of force vectors
        radii           optional array of particle radii
        colors          optional array of scalars to use to set particle colors 
                        The exact colors will depend on the color map you set up in Paraview.
        """
        import xml.dom.minidom
        #import xml.dom.ext # python 2.5 and later        

        # Document and root element
        doc = xml.dom.minidom.Document()
        root_element = doc.createElementNS("VTK", "VTKFile")
        root_element.setAttribute("type", "UnstructuredGrid")
        root_element.setAttribute("version", "0.1")
        root_element.setAttribute("byte_order", "LittleEndian")
        doc.appendChild(root_element)

        # Unstructured grid element
        unstructuredGrid = doc.createElementNS("VTK", "UnstructuredGrid")
        root_element.appendChild(unstructuredGrid)

        # Piece 0 (only one)
        piece = doc.createElementNS("VTK", "Piece")
        piece.setAttribute("NumberOfPoints", str(len(x)))
        piece.setAttribute("NumberOfCells", "0")
        unstructuredGrid.appendChild(piece)

        ### Points ####
        points = doc.createElementNS("VTK", "Points")
        piece.appendChild(points)

        # Point location data
        point_coords = doc.createElementNS("VTK", "DataArray")
        point_coords.setAttribute("type", "Float32")
        point_coords.setAttribute("format", "ascii")
        point_coords.setAttribute("NumberOfComponents", "3")
        points.appendChild(point_coords)

        string = self.coords_to_string(x, y, z)
        point_coords_data = doc.createTextNode(string)
        point_coords.appendChild(point_coords_data)

        #### Cells ####
        cells = doc.createElementNS("VTK", "Cells")
        piece.appendChild(cells)

        # Cell locations
        cell_connectivity = doc.createElementNS("VTK", "DataArray")
        cell_connectivity.setAttribute("type", "Int32")
        cell_connectivity.setAttribute("Name", "connectivity")
        cell_connectivity.setAttribute("format", "ascii")        
        cells.appendChild(cell_connectivity)

        # Cell location data
        connectivity = doc.createTextNode("0")
        cell_connectivity.appendChild(connectivity)

        cell_offsets = doc.createElementNS("VTK", "DataArray")
        cell_offsets.setAttribute("type", "Int32")
        cell_offsets.setAttribute("Name", "offsets")
        cell_offsets.setAttribute("format", "ascii")                
        cells.appendChild(cell_offsets)
        offsets = doc.createTextNode("0")
        cell_offsets.appendChild(offsets)

        cell_types = doc.createElementNS("VTK", "DataArray")
        cell_types.setAttribute("type", "UInt8")
        cell_types.setAttribute("Name", "types")
        cell_types.setAttribute("format", "ascii")                
        cells.appendChild(cell_types)
        types = doc.createTextNode("1")
        cell_types.appendChild(types)

        #### Data at Points ####
        point_data = doc.createElementNS("VTK", "PointData")
        piece.appendChild(point_data)

        # Points
        point_coords_2 = doc.createElementNS("VTK", "DataArray")
        point_coords_2.setAttribute("Name", "Points")
        point_coords_2.setAttribute("NumberOfComponents", "3")
        point_coords_2.setAttribute("type", "Float32")
        point_coords_2.setAttribute("format", "ascii")
        point_data.appendChild(point_coords_2)

        string = self.coords_to_string(x, y, z)
        point_coords_2_Data = doc.createTextNode(string)
        point_coords_2.appendChild(point_coords_2_Data)

        # Particle jump vectors
        if len(x_jump) > 0:
            jumps = doc.createElementNS("VTK", "DataArray")
            jumps.setAttribute("Name", "jumps")
            jumps.setAttribute("NumberOfComponents", "3")
            jumps.setAttribute("type", "Float32")
            jumps.setAttribute("format", "ascii")
            point_data.appendChild(jumps)

            string = self.coords_to_string(x_jump, y_jump, z_jump)
            jumpData = doc.createTextNode(string)
            jumps.appendChild(jumpData)

        # Force vectors
        if len(x_force) > 0:
            forces = doc.createElementNS("VTK", "DataArray")
            forces.setAttribute("Name", "forces")
            forces.setAttribute("NumberOfComponents", "3")
            forces.setAttribute("type", "Float32")
            forces.setAttribute("format", "ascii")
            point_data.appendChild(forces)

            string = self.coords_to_string(x_force, y_force, z_force)            
            forceData = doc.createTextNode(string)
            forces.appendChild(forceData)

        # Particle radii
        if len(radii) > 0:
            radiiNode = doc.createElementNS("VTK", "DataArray")
            radiiNode.setAttribute("Name", "radii")
            radiiNode.setAttribute("type", "Float32")
            radiiNode.setAttribute("format", "ascii")
            point_data.appendChild(radiiNode)

            string = self.array_to_string(radii)
            radiiData = doc.createTextNode(string)
            radiiNode.appendChild(radiiData)

        if len(colors) > 0:
            # Particle colors
            colorNode= doc.createElementNS("VTK", "DataArray")
            colorNode.setAttribute("Name", "colors")
            colorNode.setAttribute("type", "Float32")
            colorNode.setAttribute("format", "ascii")
            point_data.appendChild(colorNode)

            string = self.array_to_string(colors)
            color_Data = doc.createTextNode(string)
            colorNode.appendChild(color_Data)

        #### Cell data (dummy) ####
        cell_data = doc.createElementNS("VTK", "CellData")
        piece.appendChild(cell_data)

        # Write to file and exit
        outFile = open(fileName, 'w')
#        xml.dom.ext.PrettyPrint(doc, file)
        doc.writexml(outFile, newl='\n')
        outFile.close()
        self.fileNames.append(fileName)

    def writePVD(self, fileName):
        outFile = open(fileName, 'w')
        import xml.dom.minidom

        pvd = xml.dom.minidom.Document()
        pvd_root = pvd.createElementNS("VTK", "VTKFile")
        pvd_root.setAttribute("type", "Collection")
        pvd_root.setAttribute("version", "0.1")
        pvd_root.setAttribute("byte_order", "LittleEndian")
        pvd.appendChild(pvd_root)

        collection = pvd.createElementNS("VTK", "Collection")
        pvd_root.appendChild(collection)

        for i in range(len(self.fileNames)):
            dataSet = pvd.createElementNS("VTK", "DataSet")
            dataSet.setAttribute("timestep", str(i))
            dataSet.setAttribute("group", "")
            dataSet.setAttribute("part", "0")
            dataSet.setAttribute("file", str(self.fileNames[i]))
            collection.appendChild(dataSet)

        outFile = open(fileName, 'w')
        pvd.writexml(outFile, newl='\n')
        outFile.close()
