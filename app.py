import pandas as pd
import csv
from wmd import WMD
#Get the idea
idea = "Tweetsourcing"

#TODO: OM's Task
descriptions = {}
ceo_description = "Visionary Leadership: Ability to envision the potential of Tweetsourcing and inspire teams to work towards achieving it. \
Strategic Thinking: Capacity to develop long-term plans and strategies for utilizing Tweetsourcing to achieve business objectives.\
Social Media Proficiency: Deep understanding of Twitter\'s platform, features, and dynamics.\
Communication Skills: Excellent written and verbal communication skills to engage with stakeholders effectively on Twitter.\
Relationship Building: Capacity to foster meaningful relationships with diverse stakeholders on social media platforms.\
Analytical Abilities: Strong data analytics skills to interpret Twitter data and derive actionable insights.\
Adaptability: Ability to navigate and adapt to the rapidly changing landscape of social media and technology.\
Decision-making: Capability to make data-driven decisions based on insights gathered from Tweetsourcing.\
Innovation: Willingness to explore and implement innovative approaches to maximize the potential of Tweetsourcing.\
Team Management: Proficiency in leading and managing teams to execute Tweetsourcing strategies effectively."

cmo_description = "Social Media Expertise: The ideal CMO is highly proficient in social media platforms, especially Twitter, with a deep understanding of its algorithms, features, and user behavior.\
Strategic Thinker: They possess strategic acumen to develop comprehensive marketing plans that leverage Tweetsourcing to achieve organizational goals, such as brand awareness, customer engagement, and lead generation.\
Data-driven Decision Making: Proficient in data analysis, the ideal CMO can extract meaningful insights from Tweetsourcing data to inform marketing strategies and campaigns, enabling them to make informed, data-driven decisions.\
Creative Storytelling: They have a knack for crafting compelling narratives and engaging content that resonates with Twitter users, driving brand visibility and fostering authentic connections.\
Customer-centric Approach: With a keen focus on understanding and meeting customer needs, the ideal CMO utilizes Tweetsourcing to gather feedback, understand sentiment, and tailor marketing efforts to the preferences of their target audience.\
Agile and Adaptive: In a fast-paced digital landscape, they are agile and adaptable, able to quickly pivot strategies based on real-time insights gleaned from Tweetsourcing.\
Collaboration and Leadership: Effective collaboration with cross-functional teams is crucial for success. The ideal CMO fosters collaboration and provides leadership to ensure alignment between marketing initiatives and overall business objectives.\
Brand Ambassadorship: They serve as a brand ambassador, effectively representing the company's values and vision on Twitter while engaging with followers and industry influencers to amplify brand messaging.\
Innovation and Experimentation: Embracing innovation, the ideal CMO is not afraid to experiment with new approaches and technologies within Tweetsourcing to stay ahead of competitors and drive continuous improvement.\
Measurement and Optimization: Lastly, they prioritize performance measurement and optimization, regularly evaluating the effectiveness of Tweetsourcing strategies and campaigns to refine and enhance marketing efforts over time."

cto_description = "Technical Proficiency: The ideal CTO is highly proficient in software development, data engineering, and machine learning, with expertise in building scalable and reliable systems to handle large volumes of Twitter data.\
Social Media Integration: They have a deep understanding of Twitter's API and ecosystem, enabling them to effectively integrate Twitter data into the platform and develop features that leverage the unique capabilities of the platform for Tweetsourcing.\
Data Architecture: Proficient in designing and implementing robust data architectures, the ideal CTO ensures efficient storage, processing, and analysis of Twitter data while maintaining data integrity and security.\
Machine Learning and Natural Language Processing (NLP): They possess expertise in machine learning and NLP techniques to extract insights, sentiment analysis, and trend detection from Twitter data, enhancing the value of Tweetsourcing for users.\
Real-time Processing: With a focus on real-time data processing, the ideal CTO implements technologies and frameworks that enable the platform to capture and analyze Twitter data in near real-time, providing users with up-to-date insights and trends.\
Scalability and Performance: They have experience in building scalable and high-performance systems that can handle spikes in traffic and accommodate the growing user base of the Tweetsourcing platform.\
Security and Privacy: Prioritizing security and privacy, the ideal CTO implements robust security measures to protect user data and ensures compliance with relevant regulations, such as GDPR and CCPA.\
Innovation and Experimentation: Embracing innovation, they continuously explore new technologies and methodologies to enhance the functionality and capabilities of the Tweetsourcing platform, driving innovation in the field of social media data analysis.\
Leadership and Collaboration: Effective leadership and collaboration with cross-functional teams are essential for success. The ideal CTO fosters a culture of collaboration, innovation, and excellence within the technology team, ensuring alignment with business goals and objectives.\
Continuous Learning and Improvement: Lastly, they prioritize continuous learning and improvement, staying abreast of emerging technologies and industry trends to drive ongoing innovation and evolution of the Tweetsourcing platform."\

descriptions['CEO'] = ceo_description
descriptions['CMO'] = cmo_description
descriptions['CTO'] = cto_description

with open('ceo_desc_tweet.txt', 'r') as f:
    ceo_desc_tweet = f.read()


profiles_directory = 'Profiles'


#TODO: Bhushan's Task
# community_data = pd.read_csv('communtiy_data.csv')

wmd = WMD(ceo_desc_tweet, profiles_directory)
top_5_profiles = wmd.wmd()
results = {}
for i, (profile_path, similarity_score) in enumerate(top_5_profiles, 1):
    print(f"Top {i} Profile (Similarity Score: {similarity_score}): {profile_path}")
    results[profile_path] = similarity_score

results_csv = "results.csv"
fields = ["Name", "Score"]
with open(results_csv, "w", encoding="utf-8") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(fields)
    for name, value in results.items():
        csvwriter.writerow([name, value])

# community_results = {}
# for role,desc in descriptions.items():
#     community_results[role] = community_data.apply(lambda row: apply_WMD(row,desc), axis = 1).tolist()
#
# total_score = 0
# people_score = 0
# for name, value in results.items():
#     people_score += value
#
# community_score = 0
# # for name,value in community_results.items():
# #     community_score += value
#
# total_score = 0.7 * people_score + 0.3 * community_score
#
# print(total_score)

# #  Closest community
# max_community = max(community_results, key=lambda x: community_results[x])

#TODO: Display the community
    