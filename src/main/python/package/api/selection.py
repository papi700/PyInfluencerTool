from package.api.influencer import *


class Selection :
    def __init__(self, name="", followers_range=None, engagement_rate_range=None, countries=None,
                 with_email_address=False, contacted_by=None) :
        if name == "" :
            pass
        else :
            self.name = name
        self.followers_range = followers_range
        self.engagment_rate_range = engagement_rate_range
        self.countries = countries
        self.with_email_address = with_email_address
        self.contacted_by = contacted_by
        self.creation_date = ""
        self.lenght = 0
        self.uuid = None
        self.child = []
        self.create()

    def get_criterias(self) :
        criterias = []
        all_criterias = [self.followers_range, self.engagment_rate_range, self.countries, self.with_email_address,
                         self.contacted_by]
        for criteria in criterias :
            if criteria :
                criterias.append(criteria)
        return criterias

    def call_right_function(self, criteria) :
        if criteria == self.followers_range :
            return get_influencers_by_followers(criteria[0], criteria[1])
        elif criteria == self.engagment_rate_range :
            return get_influencers_by_engagement_rate(criteria[0], criteria[1])
        elif criteria == self.countries :
            influencers = []
            for country in self.countries :
                influencers += get_influencers_by_country(country)
            return influencers
        elif criteria == self.with_email_address :
            return get_influencers_with_email_address()
        elif criteria == self.contacted_by :
            get_influencers_contacted_by(criteria)

    def get_matching_influencers(self) :
        self.list = []
        criterias = self.get_criterias()
        for criteria in criterias:
            self.list += self.call_right_function(criteria)
        return self.list

    def is_matching_criterias(self, influencer):
        pass

    def update(self):
        pass

    def save(self):
        pass

    def delete(self):
        pass


if __name__ == '__main__' :
    pass
