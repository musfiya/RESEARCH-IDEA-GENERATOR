# this is your research topic generator 
import random
import time
domain={
    "healthcare technology":{
        "people assiociated":['doctors','patients',"elderly citizen"],
        "technolog":["cybersecurity","machine learning","artificial intelligence","patient monitoring"],
        "applications":["disease prediction","medical image analysis","patient monitoring"],
        "goals":["to imporve early diagnosis" "to reduce mortality rates"]
    },
    "Environmental science":{
        "people associated":["urban populations","government agencies","rural communities"],
        "technology":['IOT',"data analysis","predictive modelling"],
        "applications":["air quality monitoring","climate forecasting","water resource management"],
        "goals":["to support sustainability","to prevent environmental disasters"]
    },
    "education technology":{
        "people associated":["students","teachers","educational institutions"],
        "technology":["AI","natural language processing","learning analytics"],
        "applications":["personalized learning","automated grading","student engagement analysis"],
        "goals":["to improve learning outcomes","to increase accessibility"]
    },
    "cybersecurity":{
        "people associated":["financial institutions","online service provider","government organizations"],
        "technology":["blockchain","anamaly detection algorithms","behavioural analytics"],
        "applications":["fraud detection","secure digital identity managment","intrusion detection systems"],
        "goals":["to strenghten data security","to prevent cyber attacks","to protect user privacy"]
    }
}
while True:
    domains=random.choice(list(domain.keys()))
    target_users=random.choice(domain[domains]["people associated"])
    tech=random.choice(domain[domains]["technology"])
    uses=random.choice(domain[domains]["applications"])
    aim=random.choice(domain[domains]["goals"])
    print("="*50)
    print("THIS IS YOUR RESEARCH TOPIC GENERATOR")
    print("="*50)
    time.sleep(3)

    print(f" DOMAIN:{domains} ")
    print(f" STAKEHOLDERS: {target_users.title()}")
    print(f" METHADOLOGY: {tech.title()}")
    print(f" APPLICATIONS: {uses.title()}")
    print(f" OBJECTIVES: {aim.title()}")
    print("="*50)
    print(f"THE RESEARCH IDEA THAT HAS BEEN GENERATED IS")
    print("="*50)
    idea=print(f"Using {tech.title()} in {domains} for {uses.title()} among {target_users.title()}"
                 f" to improve  {aim.title()}")

    again=input("you wanna generate the idea for the research again(y/n)").strip().lower()
    if again!="y":
        break
    
