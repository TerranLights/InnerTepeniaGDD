import rasterio, numpy as np, pyproj, time
from rasterio.windows import from_bounds
u="/vsicurl/https://pgc-opendata-dems.s3.us-west-2.amazonaws.com/rema/mosaics/v2.0/32m_dem_tiles.vrt"
d=np.load("hopebay_window.npz"); x0,y0,half=float(d["x0"]),float(d["y0"]),float(d["half"])
t=time.time()
with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",CPL_VSIL_CURL_ALLOWED_EXTENSIONS=".tif,.vrt",GDAL_HTTP_MAX_RETRY="3",AWS_NO_SIGN_REQUEST="YES",AWS_REGION="us-west-2",VSI_CACHE="TRUE",VSI_CACHE_SIZE="100000000"):
    with rasterio.open(u) as ds:
        print(ds.crs, ds.res, ds.shape, ds.nodata, ds.dtypes)
        # 60x60 km window at 32 m is ~1875 px each way -> read at half resolution (64 m) for speed
        win=(x0-30000,y0-30000,x0+30000,y0+30000)
        w=from_bounds(*win,transform=ds.transform)
        a=ds.read(1,window=w,out_shape=(1000,1000),boundless=True,fill_value=ds.nodata,resampling=rasterio.enums.Resampling.average)
        print("read in %.0fs"%(time.time()-t), a.shape, np.nanmin(a[a>-9000]) if (a>-9000).any() else None, a.max())
        np.savez("rema_win.npz",dem=a.astype("float32"),x0=x0,y0=y0)
