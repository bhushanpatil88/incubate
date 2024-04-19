from flask import Flask, jsonify
from flask_cors import CORS
import pandas as pd
import csv
from wmd import WMD
from LLM import LLM
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
def main(idea, designation):
    designations = getDesignations(designation)
    if len(designations)==0:
        return jsonify({"error":"Error has occured"})

    # LLM Prompter
    llm = LLM()
    res = llm.get_ideal_profiles(idea=idea,designations=designations)

    res = {
        "ceo": "At the helm of the organization, an exceptional leader emerged, a visionary with an unparalleled ability to guide the company towards uncharted horizons. Possessing an insatiable curiosity and an unwavering belief in the power of innovation, this leader forged a path marked by strategic thinking and bold decisions. With a keen eye for emerging trends and a deep understanding of the industry landscape, they anticipated market shifts and identified growth opportunities that propelled the company to new heights. Their unwavering determination and risk-taking spirit inspired a culture of excellence within the organization, empowering employees to embrace challenges and strive for continuous improvement. By fostering collaboration and open communication, they created an environment where ideas thrived and transformative solutions were born. This visionary leader's exceptional decision-making skills, informed by rigorous data analysis and a deep comprehension of stakeholder perspectives, ensured that the company remained agile and responsive to market dynamics. Their unwavering belief in the power of people and their ability to drive change fostered a loyal and highly motivated workforce, dedicated to delivering exceptional results. Under their visionary leadership, the company scaled unprecedented heights, establishing itself as an industry leader and a beacon of innovation, leaving an indelible mark on the business world and beyond.",
        "cmo": "",
        "cto": "",
    }

    # WMD Working
    final = {}
    for role,description in res.items():
        if description == "":
            continue

        # for person profiles
        wmd = WMD(description, f"./Profile/{role}")
        top_5_profiles = wmd.person_ranking()
        results = {}
        for i, (profile_path, similarity_score) in enumerate(top_5_profiles, 1):
            print(f"Top {i} Profile (Similarity Score: {similarity_score}): {profile_path}")
            results[profile_path] = similarity_score
            if role not in final:
                final[role] = []
            final[role].append([profile_path, similarity_score])
        
        results_csv = f"{role}_results.csv"
        fields = ["Name", "Score"]
        with open(results_csv, "w", encoding="utf-8") as f:
            csvwriter = csv.writer(f)
            csvwriter.writerow(fields)
            for name, score in results.items():
                csvwriter.writerow([name, score])
        # for community
        # wmd = WMD(description,f"./Communities/{role}_community")
        # top_community = wmd.wmd_community(role)
        # community_csv = f'{role}_community.csv'
        # fields = ["Name","Linkedin"]
        # print(top_community)
        # with open(community_csv, "w", encoding="utf-8") as f:
        #     csvwriter = csv.writer(f)
        #     csvwriter.writerow(fields)
        #     for arr in top_community[1]:
        #         for k,v in arr.items():
        #             csvwriter.writerow([k,v])
        # final[f'{role}_community'] = top_community
    print(final)
    return jsonify(final)

if __name__ == "__main__":
    # test("OSMO-DRAIN - the subsurface irrigation system", "100")
    app.run(host="0.0.0.0",debug=True)