import pyproj
from pyproj import CRS, Transformer, Proj

if __name__ == '__main__':
    crs_wgs84 = CRS.from_epsg('4326')  # WGS84
    crs_wgs84 = CRS.from_epsg('32632')  # WGS84
    crs_cathage = CRS.from_epsg('22332')  # Carthage / UTM zone 32N

    transfo_ll = Transformer.from_crs(crs_cathage.geodetic_crs, crs_wgs84.geodetic_crs, always_xy=True)
    transfo_xy = Transformer.from_crs(crs_cathage, crs_wgs84.geodetic_crs, always_xy=True)

    c_carthage = (23.13362105, 37.42805500)
    c_2 = transfo_ll.transform(c_carthage[0], c_carthage[1])
    print(c_carthage)
    print(c_2)
    xy_carthage = (1753780.989, 4237151.854)
    c_3 = transfo_xy.transform(xy_carthage[0], xy_carthage[1])
    print(xy_carthage)
    print(c_3)

    proj_ecef = Proj(proj='geocent', ellps='WGS84', datum='WGS84')
    proj_lla = Proj(proj='latlong', ellps='WGS84', datum='WGS84')
    #proj_carthage = crs_cathage.to_proj4()
    (x, y, z) = (23.13362105, 37.42805500, 35.931)
    #print(proj_carthage.transform(x, y, z))
    #print(pyproj.transform(proj_ecef, proj_lla, x, y, z))

    transformer = pyproj.Transformer.from_crs(
        {"proj":'geocent', "ellps":'WGS84', "datum":'WGS84'},
        {"proj":'latlong', "ellps":'WGS84', "datum":'WGS84'},
    )

    lon1, lat1, alt1 = transformer.transform(x,y,z,radians=False)
    print (lat1, lon1, alt1 )
