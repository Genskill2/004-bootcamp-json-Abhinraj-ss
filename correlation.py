import json
import math

def load_journal(journal):
        f = open (journal)
        json_array = json.load(f)
        return json_array

def compute_phi(journal,k):
    list=load_journal(journal)
    n11=0
    n00=0
    n10=0
    n01=0
    n1_=0
    n0_=0
    n_1=0
    n_0=0
    for item in list:
        if k in item['events'] and item['squirrel']:
            n11+=1
            n1_+=1
            n_1+=1
        elif k not in item['events'] and item['squirrel']==False:
            n00+=1
            n0_+=1
            n_0+=1
        elif k in item['events'] and item['squirrel']==False:
            n10+=1
            n1_+=1
            n_0+=1
        elif k not in item['events'] and item['squirrel']==True:
            n01+=1
            n0_+=1
            n_1+=1
    phi = (n11* n00 - n10* n01) / (math.sqrt(n1_ * n0_ * n_1 * n_0))

    return phi

def compute_correlations(journal):
    list=load_journal(journal)
    dict={}
    for item in list:
        for event in item["events"]:
            dict[event]=compute_phi(journal,event)
    return dict


def diagnose(journal):
    dict=compute_correlations(journal)
    event_max=0.00
    event_min=0.00
    for key in dict:
        if dict[key] > event_max:
            event_max=dict[key]
            event_max_key=key
        if dict[key] < event_min:
            event_min=dict[key]
            event_min_key=key
    return event_max_key,event_min_key
