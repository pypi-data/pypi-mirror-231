def get_mmu_kegggenes(keggname): 
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import os,sys
    os.getcwd()
    # help(os.chdir)
    #os.chdir(r"D:\AAAA_learning\Python_advanced_Learning")
    os.getcwd()

    data_dir="mmukegg_dataset"
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    else:
        print(data_dir,'directory already exists.')

    import urllib.request
    data_url="https://www.kegg.jp/kegg-bin/download_htext?htext=mmu00001&format=json&filedir=kegg/brite/mmu"
    data_file_path="mmukegg_dataset/mmu00001.json"
    if not os.path.isfile(data_file_path):
        result = urllib.request.urlretrieve(data_url,data_file_path)
    else:
        print(data_file_path,'data file already exists.')  
    
    import json
    import re

    with open("mmukegg_dataset/mmu00001.json") as f:
        ko_map_data = json.load(f)

    with open("mmukegg_dataset/KEGG_pathway_ko.txt", "w") as oh:
        line = "level1_pathway_id\tlevel1_pathway_name\tlevel2_pathway_id\tlevel2_pathway_name"
        line += "\tlevel3_pathway_id\tlevel3_pathway_name\tko\tko_name\tko_des\tec\n"
        oh.write(line)
        for level1 in ko_map_data["children"]:
            m = re.match(r"(\S+)\s+([\S\w\s]+)", level1["name"])
            level1_pathway_id = m.groups()[0].strip()
            level1_pathway_name = m.groups()[1].strip()
            for level2 in level1["children"]:
                m = re.match(r"(\S+)\s+([\S\w\s]+)", level2["name"])
                level2_pathway_id = m.groups()[0].strip()
                level2_pathway_name = m.groups()[1].strip()
                for level3 in level2["children"]:
                    m = re.match(r"(\S+)\s+([^\[]*)", level3["name"])
                    level3_pathway_id = m.groups()[0].strip()
                    level3_pathway_name = m.groups()[1].strip()
                    if "children" in level3:
                        for ko in level3["children"]:
                            m = re.match(r"(\S+)\s+(\S+);\s+([^\[]+)\s*(\[EC:\S+(?:\s+[^\[\]]+)*\])*", ko["name"])
                            if m is not None:
                                ko_id = m.groups()[0].strip()
                                ko_name = m.groups()[1].strip()
                                ko_des = m.groups()[2].strip()
                                ec = m.groups()[3]
                                if ec==None:
                                    ec = "-"
                            line = level1_pathway_id + "\t" + level1_pathway_name + "\t" + level2_pathway_id + "\t" + level2_pathway_name
                            line += "\t" + level3_pathway_id + "\t" + level3_pathway_name + "\t" + ko_id + "\t" + ko_name + "\t" + ko_des + "\t" + ec + "\n"
                            oh.write(line)
    import pandas as pd
    data = pd.read_csv("mmukegg_dataset/KEGG_pathway_ko.txt", sep="\t",dtype=str,index_col=False)
    data = data.drop_duplicates()
    #print(data)   
    data2=data[data['level3_pathway_name'] == keggname][['level3_pathway_id','level3_pathway_name','ko_name']]
    return data2,data
def get_hsa_kegggenes(keggname): 
    import matplotlib.pyplot as plt
    import numpy as np
    import pandas as pd
    import os,sys
    os.getcwd()
    # help(os.chdir)
    #os.chdir(r"D:\AAAA_learning\Python_advanced_Learning")
    os.getcwd()

    data_dir="hsakegg_dataset"
    if not os.path.isdir(data_dir):
        os.mkdir(data_dir)
    else:
        print(data_dir,'directory already exists.')

    import urllib.request
    data_url="https://www.kegg.jp/kegg-bin/download_htext?htext=hsa00001&format=json&filedir=kegg/brite/hsa"
    data_file_path="hsakegg_dataset/hsa00001.json"
    if not os.path.isfile(data_file_path):
        result = urllib.request.urlretrieve(data_url,data_file_path)
    else:
        print(data_file_path,'data file already exists.')  
    
    import json
    import re

    with open("hsakegg_dataset/hsa00001.json") as f:
        ko_map_data = json.load(f)

    with open("hsakegg_dataset/KEGG_pathway_ko.txt", "w") as oh:
        line = "level1_pathway_id\tlevel1_pathway_name\tlevel2_pathway_id\tlevel2_pathway_name"
        line += "\tlevel3_pathway_id\tlevel3_pathway_name\tko\tko_name\tko_des\tec\n"
        oh.write(line)
        for level1 in ko_map_data["children"]:
            m = re.match(r"(\S+)\s+([\S\w\s]+)", level1["name"])
            level1_pathway_id = m.groups()[0].strip()
            level1_pathway_name = m.groups()[1].strip()
            for level2 in level1["children"]:
                m = re.match(r"(\S+)\s+([\S\w\s]+)", level2["name"])
                level2_pathway_id = m.groups()[0].strip()
                level2_pathway_name = m.groups()[1].strip()
                for level3 in level2["children"]:
                    m = re.match(r"(\S+)\s+([^\[]*)", level3["name"])
                    level3_pathway_id = m.groups()[0].strip()
                    level3_pathway_name = m.groups()[1].strip()
                    if "children" in level3:
                        for ko in level3["children"]:
                            m = re.match(r"(\S+)\s+(\S+);\s+([^\[]+)\s*(\[EC:\S+(?:\s+[^\[\]]+)*\])*", ko["name"])
                            if m is not None:
                                ko_id = m.groups()[0].strip()
                                ko_name = m.groups()[1].strip()
                                ko_des = m.groups()[2].strip()
                                ec = m.groups()[3]
                                if ec==None:
                                    ec = "-"
                            line = level1_pathway_id + "\t" + level1_pathway_name + "\t" + level2_pathway_id + "\t" + level2_pathway_name
                            line += "\t" + level3_pathway_id + "\t" + level3_pathway_name + "\t" + ko_id + "\t" + ko_name + "\t" + ko_des + "\t" + ec + "\n"
                            oh.write(line)
    import pandas as pd
    data = pd.read_csv("hsakegg_dataset/KEGG_pathway_ko.txt", sep="\t",dtype=str,index_col=False)
    data = data.drop_duplicates()
    #print(data)   
    data2=data[data['level3_pathway_name'] == keggname][['level3_pathway_id','level3_pathway_name','ko_name']]
    return data2,data 
