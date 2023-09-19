import os, re
from agent1c_metrics import read1c, settings
from pathlib import Path

def parse_1CV8Clst(cfg_file):
    cfgdata = {'cluster':[],'bases':[]}

    if not os.path.isfile(cfg_file):
        return cfgdata | {'message':f'File not exists: {cfg_file}'}
    
    try:
        data = read1c.lts(cfg_file)
    except read1c.ParseJSONException as e:
        return cfgdata | {'error':'Error when reading 1c file','file':cfg_file,'content':e.original_text}

    if data:
    
        cluster_fields = ['id','name','port','host']

        cfgdata['cluster'] = {cluster_fields[i]:data[1][i] for i in range(len(cluster_fields))}

        ib_fields = ['id','name','discription','dbtype','dbserver','dbname','dbuser','dbpasshash','dbstr','p1','block','block_tasks','p2','p3','p4','p5','p6','p7','p8']

        for ibdata in data[2][1:]:
            cfgdata['bases'].append({ib_fields[i]:ibdata[i] for i in range(len(ib_fields))})

    return cfgdata

def parse_1cv8wsrv(lst_file):
    lst_data = {'clusters':[]}

    if not os.path.isfile(lst_file):
        return lst_data | {'message':f'File not exists: {lst_file}'}
    
    try:
        data = read1c.lts(lst_file)
    except read1c.ParseJSONException as e:
        return lst_data | {'error':'Error when reading 1c file','file':lst_file,'content':e.original_text}

    cluster_fields = ['id','name','port','host']

    for cl_data in data[0][1:]:
        lst_data['clusters'].append({cluster_fields[i] if i<len(cluster_fields) else f'p{i}':cl_data[i] for i in range(len(cl_data))})
    
    return lst_data

def get_data():
    for path1c in settings['folders']:
        
        filepath_1cv8wsrv = os.path.join(path1c,'1cv8wsrv.lst')
        
        if not os.path.isfile(filepath_1cv8wsrv): # we are in reg_1541 or similar folder
            path1c = Path(path1c).parent.absolute()
            filepath_1cv8wsrv = os.path.join(path1c,'1cv8wsrv.lst')
        
        cluster_info = parse_1cv8wsrv(filepath_1cv8wsrv)
        
        for cluster_item in cluster_info['clusters']:
            filepath_1CV8Clst = os.path.join(path1c,f"reg_{cluster_item['port']}",'1CV8Clst.lst')
            cluster_item['data'] = parse_1CV8Clst(filepath_1CV8Clst)

            # add info of LOG size and type
            for ib in cluster_item['data']['bases']:
                ibpath = os.path.join(path1c,f"reg_{cluster_item['port']}",ib['id'],'1Cv8Log')

                # get log type
                ib['logtype'] = 'txt' if os.path.isfile(os.path.join(ibpath,'1Cv8.lgf')) else 'sqlite'
                
                # get size
                ib['logsize'] = 0
                if os.path.exists(ibpath):
                    for ele in os.scandir(ibpath):
                        #print('-',ele)
                        ib['logsize'] += os.path.getsize(ele)
    return cluster_info
