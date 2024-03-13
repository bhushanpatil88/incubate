from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import csv
from wmd import WMD
import re

app = Flask(__name__)
CORS(app)

def getDesignations(designation):
    designations = []
    if(designation[0] == '1'):
        designations.append("ceo")
    if(designation[1] == "1"):
        designations.append("cto")
    if(designation[2] == "1"):
        designations.append("cmo")
    return designations
    
def test(idea, designation):
    # designations = getDesignations(designation)
    
    # res = {}
    
    # for role in designations:
    #     print(role)
    #     file = open(f"./resources/Ideas/{idea}/{idea}_{role}.txt", "r")
    #     res[role] = file.read()
    
    # print(res)

    # name = "PRAMOD GAIKWAD"
    # with open(f'./Profile/ceo/{name}.txt', 'r', encoding="utf-8") as f:
    #         profile = f.read()
    #         profile  = profile.replace("\n"," ")
    #         linkedin = re.search(r'Contact\s(.*?)\s\(LinkedIn\)', profile.strip()).group(1).replace(" ","")
    #         print(linkedin)
    role = "ceo"
    wmd = WMD("123",f"./Communities/{role}_community")
    wmd.wmd_community(role)

@app.route('/<idea>/<designation>')
def hello(idea, designation):
    designations = getDesignations(designation)
    if len(designations)==0:
        return jsonify({"error":"Error has occured"})
    res = {}
    
    for role in designations:
        file = open(f"./resources/Ideas/{idea}/{idea}_{role}.txt", "r")
        res[role] = file.read()
        

    # WMD Working
    final = {}
    for role,data in res.items():
        # for person profiles
        wmd = WMD(data, f"./Profile/{role}")
        top_5_profiles = wmd.wmd()
        results = {}
        print(role)
        for i, (profile_path, similarity_score, linkedin) in enumerate(top_5_profiles, 1):
            print(f"Top {i} Profile (Similarity Score: {similarity_score}): {profile_path}")
            results[profile_path] = [similarity_score, linkedin]
        final[role] = [top_5_profiles[0][0],top_5_profiles[0][1], top_5_profiles[0][2]]
        
        results_csv = f"{role}_results.csv"
        fields = ["Name", "Score","Linkedin"]
        with open(results_csv, "w", encoding="utf-8") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(fields)
            for name, value in results.items():
                csvwriter.writerow([name, value[0],value[1]])
        # for community
        wmd = WMD(data,f"./Communities/{role}_community")
        top_community = wmd.wmd_community(role)
        community_csv = f'{role}_community.csv'
        fields = ["Name","Linkedin"]
        print(top_community)
        with open(community_csv, "w", encoding="utf-8") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(fields)
            for arr in top_community[1]:
                for k,v in arr.items():
                    csvwriter.writerow([k,v])
        final[f'{role}_community'] = top_community
    print(final)
    return jsonify(final)

if __name__ == "__main__":
    # test("OSMO-DRAIN - the subsurface irrigation system", "100")
    app.run(host="0.0.0.0",debug=True)