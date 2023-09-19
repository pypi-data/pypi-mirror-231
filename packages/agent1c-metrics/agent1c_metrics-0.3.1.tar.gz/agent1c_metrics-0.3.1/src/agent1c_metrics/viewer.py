from string import Template

from fastapi import FastAPI
from fastapi.responses import PlainTextResponse
import click, uvicorn
from agent1c_metrics.api import settings_api
from agent1c_metrics import __version__, settings

app = FastAPI(title="1C-agent metrics")
app.include_router(settings_api.router)
app.version = __version__

from agent1c_metrics.reader import get_data
from agent1c_metrics import settings

@app.get('/metrics', response_class=PlainTextResponse)
async def metrics():
    result = []
    result.append("# HELP agent1c_metrics_infobase_logsize Cumulative size of 1cv8log folder.")
    result.append("# TYPE agent1c_metrics_infobase_logsize gauge")
    #result.append("# TYPE logtype_by_infobase gauge")
    t_logsize = Template("agent1c_metrics_infobase_logsize{host=\"$host\",port=\"$port\",ibname=\"$ibname\",ibid=\"$ibid\",type=\"$type\"} $size")
    #t_logtype = Template("agent1c_metrics_logtype_by_infobase{host=\"$host\",port=\"$port\",ibname=\"$ibname\",ibid=\"$ibid\",type=\"$type\"} 1")
    data = get_data()
    for cluster_info in data['clusters']:
        for ib in cluster_info['data']['bases']:
            result.append(t_logsize.substitute(
                host=cluster_info['data']['cluster']['host'],
                port=cluster_info['data']['cluster']['port'],
                ibname=ib['name'],
                ibid=ib['id'],
                size=ib['logsize'],
                type=ib['logtype']
            ))
            '''
            result.append(t_logtype.substitute(
                host=cluster_info['data']['cluster']['host'],
                port=cluster_info['data']['cluster']['port'],
                ibname=ib['name'],
                ibid=ib['id'],
                type=ib['logtype']
            ))
            '''
    return PlainTextResponse('\n'.join(result))


@app.get("/")
async def root():

    result = get_data()
    
    return result

@click.command()
@click.option("--reload", is_flag=True, help="Reload if code changes")
@click.option("--host", default='0.0.0.0', type=str, required=False, help="Host for reading")
@click.option("--port", default='8144', type=str, required=False, help="Port for reading")
def run(reload:bool,host:str, port:str) -> None:
    uvicorn.run("agent1c_metrics:app", port=8144, log_level="info", host=host, reload=reload)

if __name__ == "__main__":
    run()
else:
    print(settings)