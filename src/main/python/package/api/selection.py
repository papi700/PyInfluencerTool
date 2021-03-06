from glob import glob
from datetime import date
from uuid import uuid4
import json
import os

try:
    from package.api.influencer import *
except:
    pass

from package.api.constants import SELECTIONS_DIR


def get_selections() :
    selections = []
    files = glob(os.path.join(SELECTIONS_DIR, "*.json"))
    for file in files :
        with open(file, "r") as f :
            selection_data = json.load(f)
            selection_name = selection_data.get("name")
            selection_uuid = os.path.splitext(os.path.basename(file))[0]
            selection_followers_range = selection_data.get("followers_range")
            selection_engagement_rate_range = selection_data.get("engagement_rate_range")
            selection_countries = selection_data.get("countries")
            selection_with_email_address = selection_data.get("with_email_address")
            selection_contacted_by = selection_data.get("contacted_by")
            selection_creation_date = selection_data.get("creation_date")
            selection_influencers = selection_data.get("influencers")
            selection = Selection(name=selection_name,
                                  uuid=selection_uuid,
                                  followers_range=selection_followers_range,
                                  engagement_rate_range=selection_engagement_rate_range,
                                  countries=selection_countries,
                                  with_email_address=selection_with_email_address,
                                  contacted_by=selection_contacted_by,
                                  creation_date=selection_creation_date,
                                  influencers=selection_influencers)
            selections.append(selection)
    return selections


class Selection :
    def __init__(self, name="", uuid="", followers_range=None, engagement_rate_range=None, countries=None,
                 with_email_address=False, contacted_by=None, creation_date=None, influencers=None) :
        if name == "" :
            directory_lenght = len(glob(os.path.join(SELECTIONS_DIR, "*.json")))
            self.name = "Selection_" + str(directory_lenght + 1)
        else :
            self.name = name
        if uuid == "" :
            self.uuid = str(uuid4())
        else :
            self.uuid = uuid
        self.followers_range = followers_range
        self.engagement_rate_range = engagement_rate_range
        self.countries = countries
        self.with_email_address = with_email_address
        self.contacted_by = contacted_by
        if creation_date is None :
            d = str(date.today())
            d = d.split("-")
            self.creation_date = d[2]+"-"+d[1]+"-"+d[0]
        else :
            self.creation_date = creation_date
        self.child = []
        self.criterias = self.get_criterias()
        # print(self.criterias)
        if influencers :
            self.influencers = influencers
        else :
            self.influencers = self.get_matching_influencers()
        self.lenght = len(self.influencers)

    def get_criterias(self) :
        selection_criterias = []
        all_criterias = [self.followers_range, self.engagement_rate_range, self.countries, self.with_email_address,
                         self.contacted_by]
        for criteria in all_criterias :
            if criteria :
                selection_criterias.append(criteria)
        return selection_criterias

    def call_right_function(self, criteria) :
        if criteria == self.followers_range :
            return get_influencers_by_followers(criteria[0], criteria[1])
        elif criteria == self.engagement_rate_range :
            return get_influencers_by_engagement_rate(criteria[0], criteria[1])
        elif criteria == self.countries :
            influencers = []
            for country in self.countries :
                influencers += get_influencers_by_country(country)
            return influencers
        elif criteria == self.with_email_address :
            return get_influencers_with_email_address()
        elif criteria == self.contacted_by :
            influencers = []
            if isinstance(self.contacted_by, list) :
                for mean in self.contacted_by :
                    influencers += get_influencers_contacted_by(mean)
            else :
                influencers = get_influencers_contacted_by(self.contacted_by)
            return influencers

    def get_matching_influencers(self) :
        final_list = []
        list_of_lists = []
        criterias = self.get_criterias()
        for criteria in criterias :
            list_of_lists += self.call_right_function(criteria)
        for influencer in list_of_lists :
            if list_of_lists.count(influencer) == len(criterias) and influencer not in final_list :
                final_list.append(influencer)
        return final_list

    def is_matching_criterias(self, influencer) :
        list = self.get_matching_influencers()
        if influencer in list :
            return True
        else :
            return False

    def update(self, influencer) :
        if self.is_matching_criterias(influencer) :
            self.influencers.append(influencer)
        elif influencer in self.influencers :
            self.influencers.remove(influencer)
        self.save()

    def split(self, number_of_subselections) :
        if number_of_subselections % self.lenght == 0 :
            pass
        else :
            return False

    @property
    def path(self) :
        return os.path.join(SELECTIONS_DIR, self.uuid + ".json")

    def save(self) :
        if not os.path.exists(SELECTIONS_DIR) :
            os.makedirs(SELECTIONS_DIR)

        data = {"name" : self.name, "followers_range" : self.followers_range,
                "engagement_rate_range" : self.engagement_rate_range,
                "countries" : self.countries, "with_email_address" : self.with_email_address,
                "contacted_by" : self.contacted_by, "creation_date" : self.creation_date,
                "lenght" : self.lenght, "child" : self.child,
                "influencers" : self.influencers}

        with open(self.path, "w") as f :
            json.dump(data, f, indent=4)

    def delete(self) :
        os.remove(self.path)
        if os.path.exists(self.path) :
            return False
        else :
            return True


if __name__ == '__main__' :
    pass
    # s = Selection()
