import rasterio, numpy as np
from rasterio.windows import from_bounds
d=np.load("hopebay_window.npz"); x0,y0,half=float(d["x0"]),float(d["y0"]),float(d["half"])
win=(x0-half,y0-half,x0+half,y0+half)
U={"v21":"https://its-live-data.s3.amazonaws.com/velocity_mosaic/v2.1/static/cog/ITS_LIVE_velocity_120m_RGI19A_0000_V02.1_v.tif",
   "v_amp":"https://its-live-data.s3.amazonaws.com/velocity_mosaic/v2/static/cog/ITS_LIVE_velocity_120m_RGI19A_0000_v02_v_amp.tif",
   "dv_dt":"https://its-live-data.s3.amazonaws.com/velocity_mosaic/v2/static/cog/ITS_LIVE_velocity_120m_RGI19A_0000_v02_dv_dt.tif"}
out={}
with rasterio.Env(GDAL_DISABLE_READDIR_ON_OPEN="EMPTY_DIR",CPL_VSIL_CURL_ALLOWED_EXTENSIONS=".tif",GDAL_HTTP_MAX_RETRY="3"):
    for k,u in U.items():
        try:
            with rasterio.open("/vsicurl/"+u) as ds:
                w=from_bounds(*win,transform=ds.transform)
                out[k]=ds.read(1,window=w,boundless=True,fill_value=ds.nodata)
                print(k,ds.shape,ds.res,ds.nodata,"tags:",{kk:vv for kk,vv in list(ds.tags().items())[:6]})
        except Exception as e: print(k,"FAILED",repr(e)[:200])
np.savez("hopebay_extra.npz",**out)
